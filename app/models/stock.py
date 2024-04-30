from config import db

class Stock(db.Model):
    __tablename__ = 'stocks'

    ticker = db.Column(db.String(10), primary_key=True)
    companyid = db.Column(db.String(80))
    companyname = db.Column(db.String(255))
    price = db.Column(db.Float)
    p_l = db.Column(db.Float)
    dy = db.Column(db.Float)
    p_vp = db.Column(db.Float)
    p_ebit = db.Column(db.Float)
    p_ativo = db.Column(db.Float)
    ev_ebit = db.Column(db.Float)
    margembruta = db.Column(db.Float)
    margemebit = db.Column(db.Float)
    margemliquida = db.Column(db.Float)
    p_sr = db.Column(db.Float)
    p_capitalgiro = db.Column(db.Float)
    p_ativocirculante = db.Column(db.Float)
    giroativos = db.Column(db.Float)
    roe = db.Column(db.Float)
    roa = db.Column(db.Float)
    roic = db.Column(db.Float)
    dividaliquidapatrimonioliquido = db.Column(db.Float)
    dividaliquidaebit = db.Column(db.Float)
    pl_ativo = db.Column(db.Float)
    passivo_ativo = db.Column(db.Float)
    liquidezcorrente = db.Column(db.Float)
    peg_ratio = db.Column(db.Float)
    receitas_cagr5 = db.Column(db.Float)
    vpa = db.Column(db.Float)
    lpa = db.Column(db.Float)
    valormercado = db.Column(db.Float)
    segmentid = db.Column(db.Integer)
    sectorid = db.Column(db.Integer)
    subsectorid = db.Column(db.Integer)
    subsectorname = db.Column(db.String(255))
    segmentname = db.Column(db.String(255))
    sectorname = db.Column(db.String(255))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"<Stock(companyname={self.companyname}, ticker={self.ticker}, price={self.price})>"

    def to_json(self):
        return {
            'ticker': self.ticker,
            'companyid': self.companyid,
            'companyname': self.companyname,
            'price': self.price,
            'p_l': self.p_l,
            'dy': self.dy,
            'p_vp': self.p_vp,
            'p_ebit': self.p_ebit,
            'p_ativo': self.p_ativo,
            'ev_ebit': self.ev_ebit,
            'margembruta': self.margembruta,
            'margemebit': self.margemebit,
            'margemliquida': self.margemliquida,
            'p_sr': self.p_sr,
            'p_capitalgiro': self.p_capitalgiro,
            'p_ativocirculante': self.p_ativocirculante,
            'giroativos': self.giroativos,
            'roe': self.roe,
            'roa': self.roa,
            'roic': self.roic,
            'dividaliquidapatrimonioliquido': self.dividaliquidapatrimonioliquido,
            'dividaliquidaebit': self.dividaliquidaebit,
            'pl_ativo': self.pl_ativo,
            'passivo_ativo': self.passivo_ativo,
            'liquidezcorrente': self.liquidezcorrente,
            'peg_ratio': self.peg_ratio,
            'receitas_cagr5': self.receitas_cagr5,
            'vpa': self.vpa,
            'lpa': self.lpa,
            'valormercado': self.valormercado,
            'segmentid': self.segmentid,
            'sectorid': self.sectorid,
            'subsectorid': self.subsectorid,
            'subsectorname': self.subsectorname,
            'segmentname': self.segmentname,
            'sectorname': self.sectorname
        }
