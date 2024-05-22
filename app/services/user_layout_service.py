from flask import jsonify
import json

from models.user_layout import UserLayout
from config import db

def get_user_layout(user_id, layout):
    try:
        user_layout = UserLayout.query.filter_by(user_id=user_id, layout=layout).first()
        if user_layout is None:
            return jsonify(None), 400
        return jsonify(user_layout.estado)
    except Exception as e:
        print(f"Error fetching user layout: {e}")
        return jsonify({'message': 'Error fetching user layout'}), 500

def save_user_layout(user_id, layout, estado):
    try:
        user_layout = UserLayout.query.filter_by(user_id=user_id, layout=layout).first()

        if user_layout:
            user_layout.estado = estado
            message = 'User layout updated successfully'
        else:
            user_layout = UserLayout(user_id=user_id, layout=layout, estado=estado)
            db.session.add(user_layout)
            message = 'User layout added successfully'

        db.session.commit()
        return jsonify({'message': message}), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error saving user layout: {e}")
        return jsonify({'message': 'Error saving user layout'}), 500
