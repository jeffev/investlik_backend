from flask import jsonify
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity

from routes.stock_routes import list_stocks_json, view_stock_json, new_stock_json, edit_stock_json, delete_stock_json, update_all_stocks
from routes.user_routes import list_users_json, view_user_json, new_user_json, edit_user_json, delete_user_json, login_user_json

def protected_route(view_func):
    @wraps(view_func)
    @jwt_required()
    def decorated_view(*args, **kwargs):
        current_user_id = get_jwt_identity()

        # Verifica se o identificador do usuário foi obtido
        if current_user_id is None:
            return jsonify({'message': 'Invalid token'}), 401

        # Lógica para verificar perfil vai aqui

        # Chama a função da rota original
        return view_func(*args, **kwargs)

    return decorated_view

def setup_routes(app):
    # Stock routes
    app.add_url_rule('/stocks', methods=['GET'], view_func=protected_route(list_stocks_json))
    app.add_url_rule('/stock/<string:ticker>', methods=['GET'], view_func=protected_route(view_stock_json))
    app.add_url_rule('/stocks', methods=['POST'], view_func=protected_route(new_stock_json))
    app.add_url_rule('/stock/<string:ticker>', methods=['PUT'], view_func=protected_route(edit_stock_json))
    app.add_url_rule('/stock/<string:ticker>', methods=['DELETE'], view_func=protected_route(delete_stock_json))
    app.add_url_rule('/stocks/update-stocks', methods=['PUT'], view_func=protected_route(update_all_stocks))

    # User routes
    app.add_url_rule('/users', methods=['GET'], view_func=protected_route(list_users_json))
    app.add_url_rule('/user/<int:user_id>', methods=['GET'], view_func=protected_route(view_user_json))
    app.add_url_rule('/users', methods=['POST'], view_func=new_user_json)
    app.add_url_rule('/user/<int:user_id>', methods=['PUT'], view_func=protected_route(edit_user_json))
    app.add_url_rule('/user/<int:user_id>', methods=['DELETE'], view_func=protected_route(delete_user_json))
    app.add_url_rule('/user/login', methods=['POST'], view_func=login_user_json)