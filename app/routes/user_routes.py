from flask import request
from services.user_services import list_users, view_user, new_user, edit_user, delete_user, login_user

def list_users_json():
    return list_users()

def view_user_json(user_id):
    try:
        return view_user(user_id)
    except Exception as e:
        print(f"Error viewing user: {e}")
        return {'message': 'Error viewing user'}, 500

def new_user_json():
    try:
        user_data = request.get_json()
        return new_user(user_data)
    except Exception as e:
        print(f"Error adding user: {e}")
        return {'message': 'Error adding user'}, 500

def edit_user_json(user_id):
    try:
        user_data = request.get_json()
        return edit_user(user_id, user_data)
    except Exception as e:
        print(f"Error editing user: {e}")
        return {'message': 'Error editing user'}, 500

def delete_user_json(user_id):
    try:
        return delete_user(user_id)
    except Exception as e:
        print(f"Error deleting user: {e}")
        return {'message': 'Error deleting user'}, 500

def login_user_json():
    try:
        login_data = request.get_json()
        return login_user(login_data)
    except Exception as e:
        print(f"Error loging user: {e}")
        return {'message': 'Error loging user'}, 500
