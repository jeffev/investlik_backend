from flask import jsonify, request
from config import db
from models.stock import Stock

def list_stocks_json():
    all_stocks = Stock.query.all()
    stocks_json = [stock.to_json() for stock in all_stocks]
    return jsonify(stocks_json)

def view_stock_json(id):
    stock = Stock.query.get(id)
    if stock is None:
        return jsonify({'message': 'Stock not found'}), 404
    return jsonify(stock.to_json())

def new_stock_json():
    try:
        stock_data = request.get_json()
        new_stock = Stock(
            companyid=stock_data['companyid'],
            companyname=stock_data['companyname'],
            ticker=stock_data['ticker'],
            price=float(stock_data['price']),
            p_l=float(stock_data['p_l']),
            p_vp=float(stock_data['p_vp']),
            p_ebit=float(stock_data['p_ebit']),
            p_ativo=float(stock_data['p_ativo']),
            ev_ebit=float(stock_data['ev_ebit']),
            margembruta=float(stock_data['margembruta']),
            margemebit=float(stock_data['margemebit']),
            margemliquida=float(stock_data['margemliquida']),
            p_sr=float(stock_data['p_sr']),
            p_capitalgiro=float(stock_data['p_capitalgiro']),
            p_ativocirculante=float(stock_data['p_ativocirculante']),
            giroativos=float(stock_data['giroativos']),
            roe=float(stock_data['roe']),
            roa=float(stock_data['roa']),
            roic=float(stock_data['roic']),
            dividaliquidapatrimonioliquido=float(stock_data['dividaliquidapatrimonioliquido']),
            dividaliquidaebit=float(stock_data['dividaliquidaebit']),
            pl_ativo=float(stock_data['pl_ativo']),
            passivo_ativo=float(stock_data['passivo_ativo']),
            liquidezcorrente=float(stock_data['liquidezcorrente']),
            peg_ratio=float(stock_data['peg_ratio']),
            receitas_cagr5=float(stock_data['receitas_cagr5']),
            vpa=float(stock_data['vpa']),
            lpa=float(stock_data['lpa']),
            valormercado=float(stock_data['valormercado']),
            segmentid=stock_data['segmentid'],
            sectorid=stock_data['sectorid'],
            subsectorid=stock_data['subsectorid'],
            subsectorname=stock_data['subsectorname'],
            segmentname=stock_data['segmentname'],
            sectorname=stock_data['sectorname']
        )
        db.session.add(new_stock)
        db.session.commit()
        return jsonify({'message': 'Stock added successfully'})
    except Exception as e:
        print(f"Error adding stock: {e}")
        return jsonify({'message': 'Error adding stock'}), 500

def edit_stock_json(id):
    stock = Stock.query.get(id)
    if stock is None:
        return jsonify({'message': 'Stock not found'}), 404
    try:
        stock_data = request.get_json()
        stock.companyid=stock_data['companyid'],
        stock.companyname=stock_data['companyname'],
        stock.ticker=stock_data['ticker'],
        stock.price=float(stock_data['price']),
        stock.p_l=float(stock_data['p_l']),
        stock.p_vp=float(stock_data['p_vp']),
        stock.p_ebit=float(stock_data['p_ebit']),
        stock.p_ativo=float(stock_data['p_ativo']),
        stock.ev_ebit=float(stock_data['ev_ebit']),
        stock.margembruta=float(stock_data['margembruta']),
        stock.margemebit=float(stock_data['margemebit']),
        stock.margemliquida=float(stock_data['margemliquida']),
        stock.p_sr=float(stock_data['p_sr']),
        stock.p_capitalgiro=float(stock_data['p_capitalgiro']),
        stock.p_ativocirculante=float(stock_data['p_ativocirculante']),
        stock.giroativos=float(stock_data['giroativos']),
        stock.roe=float(stock_data['roe']),
        stock.roa=float(stock_data['roa']),
        stock.roic=float(stock_data['roic']),
        stock.dividaliquidapatrimonioliquido=float(stock_data['dividaliquidapatrimonioliquido']),
        stock.dividaliquidaebit=float(stock_data['dividaliquidaebit']),
        stock.pl_ativo=float(stock_data['pl_ativo']),
        stock.passivo_ativo=float(stock_data['passivo_ativo']),
        stock.liquidezcorrente=float(stock_data['liquidezcorrente']),
        stock.peg_ratio=float(stock_data['peg_ratio']),
        stock.receitas_cagr5=float(stock_data['receitas_cagr5']),
        stock.vpa=float(stock_data['vpa']),
        stock.lpa=float(stock_data['lpa']),
        stock.valormercado=float(stock_data['valormercado']),
        stock.segmentid=stock_data['segmentid'],
        stock.sectorid=stock_data['sectorid'],
        stock.subsectorid=stock_data['subsectorid'],
        stock.subsectorname=stock_data['subsectorname'],
        stock.segmentname=stock_data['segmentname'],
        stock.sectorname=stock_data['sectorname']
        db.session.commit()
        return jsonify({'message': 'Stock edited successfully'})
    except Exception as e:
        print(f"Error editing stock: {e}")
        return jsonify({'message': 'Error editing stock'}), 500

def delete_stock_json(id):
    stock = Stock.query.get(id)
    if stock is None:
        return jsonify({'message': 'Stock not found'}), 404
    try:
        db.session.delete(stock)
        db.session.commit()
        return jsonify({'message': 'Stock deleted successfully'})
    except Exception as e:
        print(f"Error deleting stock: {e}")
        return jsonify({'message': 'Error deleting stock'}), 500
