from flask import Flask, render_template, request, redirect, flash, session, jsonify
from src.recognize_text import RecognizeTheText
import time
from src.identify_action import IdentifyAction
import ast
import src.db as db
import secrets
from src.manage_list import ManageList
from src.categories import display_user_category, display_all_categories
import warnings
from sklearn.exceptions import InconsistentVersionWarning
from src.auth import register, login

# create flask app
app=Flask(__name__)
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
app.secret_key = secrets.token_hex(16)

# default page
@app.route('/')
def home_page():
    print(session)
    if "user_id" not in session:
        return redirect('/login')
    return render_template('home.html')


# open login page
@app.route('/login')
def login_page():
    return render_template('login.html')


# login the user
@app.route('/login_user', methods=['POST'])
def login_user():
    response = login(request.form)

    if response['status'] == 'success':
        print(session)
        return redirect('/')
    else:
        flash(response['message'])
        print(response)
        return redirect('/login')


# open register page
@app.route('/register')
def register_page():
    return render_template('register.html')


# register user
@app.route('/register_user', methods=['POST'])
def register_user():
    response = register(request.form)

    if response['status'] == 'success':
        return redirect('/login')
    else:
        flash("All fields are required!", "error")
        return redirect('/register')


# logout
@app.route('/logout')
def logout():
    session.pop("user_id", None)
    return redirect('/')


# open your list item
@app.route('/list')
def open_your_list():
    if 'user_id' not in session:
        return redirect('/login')
    try:
        manage_list = ManageList()
        user_lists, reco_items = manage_list.view_list()

        if user_lists and reco_items:
            return render_template('list.html', lists=user_lists, reco_items=reco_items)
        else:
            return render_template('list.html', lists=None, reco_items=None)
    except:
        return render_template('list.html', lists=None, reco_items=None)



# delete full list
@app.route('/delete_list', methods=['POST'])
def delete_entire_list():
    manage_lst = ManageList()
    list_id = request.json.get("list_id")
    res = manage_lst.delete_full_list(list_id)
    return res


# categories page
@app.route('/categories')
def categories():
    if 'user_id' not in session:
        return redirect('/login')
    else:
        try:
            user_cate_lst = display_user_category()
            return render_template('categories.html', user_cate=user_cate_lst)
        except:
            return render_template('categories.html', user_cate=None)


# recognize text
@app.route('/recognize_text', methods=['POST'])
def recognize_text():
    reco_text = RecognizeTheText()
    data = request.json.get('speech_text')

    text = reco_text.recognize_text()
    cleaned_text = reco_text.process_input(text)
    time.sleep(3)

    return cleaned_text


# perform specific task
@app.route('/idenify_action', methods=['POST'])
def perform_task():
    idf_act = IdentifyAction()
    user_ipt = request.json.get('user_input')

    res = idf_act.identify_action(user_ipt)
    res = ast.literal_eval(res)
    return res


# save the action in database
@app.route("/save_item", methods=['POST'])
def save_item():
    manage_lst = ManageList()
    action = request.json.get('action')
    item = request.json.get('item')

    if action == 'add':
        response = manage_lst.add_item(item)
    elif action == "remove":
        response = manage_lst.remove_item(item)
    elif action == "view":
        response = manage_lst.view_list()
    else:
        return ("Invalid action"), 500

    return jsonify(response), 200


if __name__=='__main__':
    app.run(debug=True)
