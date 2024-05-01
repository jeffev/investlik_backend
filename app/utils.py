from routes.stock_routes import list_stocks_json, view_stock_json, new_stock_json, edit_stock_json, delete_stock_json, update_all_stocks
from routes.user_routes import list_users_json, view_user_json, new_user_json, edit_user_json, delete_user_json

def setup_routes(app):
    # Stock routes
    app.add_url_rule('/stocks', methods=['GET'], view_func=list_stocks_json)
    app.add_url_rule('/stock/<string:ticker>', methods=['GET'], view_func=view_stock_json)
    app.add_url_rule('/stocks', methods=['POST'], view_func=new_stock_json)
    app.add_url_rule('/stock/<string:ticker>', methods=['PUT'], view_func=edit_stock_json)
    app.add_url_rule('/stock/<string:ticker>', methods=['DELETE'], view_func=delete_stock_json)
    app.add_url_rule('/stocks/update-stocks', methods=['PUT'], view_func=update_all_stocks)

    # User routes
    app.add_url_rule('/users', methods=['GET'], view_func=list_users_json)
    app.add_url_rule('/user/<int:user_id>', methods=['GET'], view_func=view_user_json)
    app.add_url_rule('/users', methods=['POST'], view_func=new_user_json)
    app.add_url_rule('/user/<int:user_id>', methods=['PUT'], view_func=edit_user_json)
    app.add_url_rule('/user/<int:user_id>', methods=['DELETE'], view_func=delete_user_json)
