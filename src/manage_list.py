import json
from uuid import uuid4
from flask import session
from src.db import db_obj
from datetime import datetime
from src.categories import put_in_category
from src.recommendation import recommend
from datetime import datetime


class ManageList:
    def __init__(self):
        with open("data/words_map.json", "rb") as f:
            self.file = json.loads(f.read())


    # find the action
    def find_action(self, query):
        queries = query.split(" ")

        for key, value in self.file.items():
            for word in queries:
                if word in value:
                    return key
                else:
                    return None
    

    # add item in list
    def add_item(self, item: str):
        user_id = session['user_id']

        user_list = db_obj['lists'].find_one({"user_id": user_id})
        if user_list:
            db_obj['lists'].update_one(
                {"user_id": user_id},
                {
                    "$addToSet": {"item": item},
                    "$set": {"updated_at": datetime.now()}
                }
            )
            # add categories
            db_obj['categories'].update_one(
                {"list_id": user_list['list_id']},
                {
                    "$push": {"category": put_in_category(item)},
                    "$set": {"updated_at": datetime.now()}
                }
            )
        else:
            l_id = str(uuid4())
            db_obj['lists'].insert_one({
                "list_id": l_id,
                "user_id": user_id,
                "item": [item.lower()],
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            })

            # add category
            db_obj['categories'].insert_one({
                "list_id": l_id,
                "category": [put_in_category(item)],
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            })

        response = db_obj['lists'].find_one({"user_id": user_id})

        response['_id'] = str(response['_id'])
        response['created_at'] = response['created_at'].isoformat()
        response['updated_at'] = response['updated_at'].isoformat()

        return response


    # remove the item from db
    def remove_item(self, item):
        user_id = session['user_id']
        user_list = db_obj['lists'].find_one({"user_id": user_id})

        if item in user_list['item']:
            item_index = user_list['item'].index(item)

            db_obj['lists'].update_one(
                {"user_id": user_id},
                {
                    "$pull": {"item": item},
                    "$set": {"updated_at": datetime.now()}
                }
            )
        
            # update category
            cate_obj = db_obj['categories'].find_one({"list_id": user_list['list_id']})
            target_cate = cate_obj['category'][item_index]
            if target_cate:
                db_obj['categories'].update_one(
                    {"list_id": user_list['list_id']},
                    {
                        "$pull": {"category": target_cate},
                        "$set": {"updated_at": datetime.now()}
                    }
                )
            else:
                print("no category found")
        else:
            print("no item found")

        response = user_list

        response['_id'] = str(response['_id'])
        response['created_at'] = response['created_at'].isoformat()
        response['updated_at'] = response['updated_at'].isoformat()

        return response

    
    # view the lists
    def view_list(self):
        user_id = "d6cfa49e-093c-4048-8366-e9a286cfe306"
        user_id = session['user_id']
        response = db_obj['lists'].find_one({"user_id": user_id})

        if response:
            recommend_list = []
            for item in response['item']:
                reco_item_lst = recommend(item)
                recommend_list.append(reco_item_lst)

            response_items_set = set(response['item'])
            recommend_list = [item for item_list in recommend_list for item in item_list if item not in response_items_set]

            response['_id'] = str(response['_id'])
            response['created_at'] = response['created_at'].strftime("%d %B %Y, %I:%M %p")
            response['updated_at'] = response['updated_at'].strftime("%d %B %Y, %I:%M %p")

            return response, recommend_list
        else:
            None
