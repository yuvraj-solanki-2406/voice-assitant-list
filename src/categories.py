import pickle
from flask import session
from src.db import db_obj

# load model and vectorizer
with open("notebooks/random_forest.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("notebooks/vectorizer.pkl", "rb") as vect_file:
    vectorizer = pickle.load(vect_file)


# function to find category
def put_in_category(item: str):
    item_vect = vectorizer.transform([item])
    response = model.predict(item_vect)
    return list(response)[0]


# display user category
def display_user_category():
    """
        {"item_anme": "item_category"}
    """
    user_id = session['user_id']
    # user_id = "5081534c-2524-4b1e-8393-6bc6a9042be6"
    output_dict = {}

    user_list = db_obj['lists'].find_one({'user_id': user_id})
    user_cate = db_obj['categories'].find_one({'list_id': user_list['list_id']})

    for index in range(len(user_list['item'])):
        try:
            output_dict[user_list['item'][index]] = user_cate['category'][index]
        except:
            output_dict[user_list['item'][index]] = put_in_category(user_list['item'][index])

    return output_dict

# display all categories
def display_all_categories():
    all_categories = db_obj['categories'].find()
    return all_categories


if __name__ == "__main__":
    print(display_user_category())