from flask import request
from services.stock_services import list_stocks, view_stock, new_stock, edit_stock, delete_stock, update_all_stocks

def list_stocks_json():
    try:
        return list_stocks()
    except Exception as e:
        print(f"Error listing all stocks: {e}")
        return {'message': 'Error listing all stocks'}, 500

def view_stock_json(ticker):
    try:
        return view_stock(ticker.upper())
    except Exception as e:
        print(f"Error viewing stock: {e}")
        return {'message': 'Error viewing stock'}, 500
    
def new_stock_json():
    try:
        stock_data = request.get_json()
        return new_stock(stock_data)
    except Exception as e:
        print(f"Error adding stock: {e}")
        return {'message': 'Error adding stock'}, 500

def edit_stock_json(ticker):
    try:
        stock_data = request.get_json()
        return edit_stock(ticker.upper(), stock_data)
    except Exception as e:
        print(f"Error editing stock: {e}")
        return {'message': 'Error editing stock'}, 500

def delete_stock_json(ticker):
    try:
        return delete_stock(ticker.upper())
    except Exception as e:
        print(f"Error deleting stock: {e}")
        return {'message': 'Error deleting stock'}, 500

def update_stocks():
    try:
        return update_all_stocks()
    except Exception as e:
        print(f"Error updating all stocks: {e}")
        return {'message': 'Error updating all stocks'}, 500
