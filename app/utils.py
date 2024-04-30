from routes.stock_routes import list_stocks_json, view_stock_json, new_stock_json, edit_stock_json, delete_stock_json, update_all_stocks

def setup_routes(app):
    app.add_url_rule('/stocks', methods=['GET'], view_func=list_stocks_json)
    app.add_url_rule('/stock/<string:ticker>', methods=['GET'], view_func=view_stock_json)
    app.add_url_rule('/stocks', methods=['POST'], view_func=new_stock_json)
    app.add_url_rule('/stock/<string:ticker>', methods=['PUT'], view_func=edit_stock_json)
    app.add_url_rule('/stock/<string:ticker>', methods=['DELETE'], view_func=delete_stock_json)
    app.add_url_rule('/stocks/update-stocks', methods=['PUT'], view_func=update_all_stocks)