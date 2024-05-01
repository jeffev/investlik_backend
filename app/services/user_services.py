from flask import jsonify
import bcrypt

from models.user import User
from config import db

def list_users():
    all_users = User.query.all()
    users_json = [user.to_json() for user in all_users]
    return jsonify(users_json)

def view_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.to_json())

def new_user(user_data):
    try:
        if 'user_name' not in user_data or not user_data['user_name']:
            return jsonify({'message': 'User name is required'}), 400

        existing_user = User.query.filter_by(user_name=user_data['user_name']).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        password = user_data.pop('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user_data['password'] = hashed_password.decode('utf-8')

        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        print(f"Error adding user: {e}")
        return jsonify({'message': 'Error adding user'}), 500

def edit_user(user_id, user_data):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    try:
        for key, value in user_data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify({'message': 'User edited successfully'}), 200
    except Exception as e:
        print(f"Error editing user: {e}")
        return jsonify({'message': 'Error editing user'}), 500

def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        print(f"Error deleting user: {e}")
        return jsonify({'message': 'Error deleting user'}), 500
