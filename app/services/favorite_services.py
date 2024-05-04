from flask import jsonify

from config import db
from models.favorite import Favorite
from models.stock import Stock
from models.user import User

def list_favorites(user_id):
    try:
        user_favorites = Favorite.query.filter_by(user_id=user_id).all()
        favorites_json = [favorite.to_json() for favorite in user_favorites]
        return jsonify(favorites_json)
    except Exception as e:
        print(f"Error listing favorites: {e}")
        return jsonify({'message': 'Error listing favorites'}), 500

def view_favorite(favorite_id):
    try:
        favorite = Favorite.query.get(favorite_id)
        if favorite is None:
            return jsonify({'message': 'Favorite not found'}), 404
        return jsonify(favorite.to_json())
    except Exception as e:
        print(f"Error viewing favorite: {e}")
        return jsonify({'message': 'Error viewing favorite'}), 500

def new_favorite(favorite_data):
    try:
        user_id = favorite_data.get('user_id')
        stock_ticker = favorite_data.get('stock_ticker')

        if not User.query.get(user_id):
            return jsonify({'message': 'User not found'}), 404

        if not Stock.query.get(stock_ticker):
            return jsonify({'message': 'Stock not found'}), 404

        existing_favorite = Favorite.query.filter_by(user_id=user_id, stock_ticker=stock_ticker).first()
        if existing_favorite:
            return jsonify({'message': 'This stock is already favorited by this user'}), 400

        new_favorite = Favorite(**favorite_data)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error adding favorite: {e}")
        return jsonify({'message': 'Error adding favorite'}), 500


def edit_favorite(favorite_id, favorite_data):
    try:
        user_id = favorite_data.get('user_id')
        stock_ticker = favorite_data.get('stock_ticker')

        if not User.query.get(user_id):
            return jsonify({'message': 'User not found'}), 404

        if not Stock.query.get(stock_ticker):
            return jsonify({'message': 'Stock not found'}), 404

        favorite = Favorite.query.get(favorite_id)
        if favorite is None:
            return jsonify({'message': 'Favorite not found'}), 404
        
        for key, value in favorite_data.items():
            setattr(favorite, key, value)

        db.session.commit()

        return jsonify({'message': 'Favorite edited successfully'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error editing favorite: {e}")
        return jsonify({'message': 'Error editing favorite'}), 500

def delete_favorite(favorite_id):
    try:
        favorite = Favorite.query.get(favorite_id)
        if favorite is None:
            return jsonify({'message': 'Favorite not found'}), 404
        
        db.session.delete(favorite)
        db.session.commit()

        return jsonify({'message': 'Favorite deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting favorite: {e}")
        return jsonify({'message': 'Error deleting favorite'}), 500

def add_favorite(user_id, ticker):
    try:
        existing_favorite = Favorite.query.filter_by(user_id=user_id, stock_ticker=ticker).first()
        if existing_favorite:
            return jsonify({'message': 'This stock is already favorited by this user'}), 400

        new_favorite = Favorite(user_id=user_id, stock_ticker=ticker)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error adding favorite: {e}")
        return jsonify({'message': 'Error adding favorite'}), 500

def remove_favorite(user_id, ticker):
    try:
        favorite = Favorite.query.filter_by(user_id=user_id, stock_ticker=ticker).first()
        if not favorite:
            return jsonify({'message': 'Favorite not found'}), 404
        
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting favorite: {e}")
        return jsonify({'message': 'Error deleting favorite'}), 500