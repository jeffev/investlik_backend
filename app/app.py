from utils import setup_routes
from config import app, db

# Cria todas as tabelas
with app.app_context():
    db.create_all()

setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
