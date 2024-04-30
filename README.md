# InvestLink Backend

Welcome to the LinkInvest API! This project serves as the backend for LinkInvest, a website designed to help investors make informed decisions by providing easy and practical access to information. With this API, you can manage stocks and users, accessing and updating data quickly and efficiently.

Feel free to explore the endpoints and integrate this API into your own projects to enhance the investment experience for your users. If you have any questions or feedback, please don't hesitate to reach out. Happy investing!

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/seu-usuario/investlink-api.git
   ```

2. Install dependencies:

   ```bash
   cd investlink-api
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   # Run the following commands in a Python shell
   from app import db
   db.create_all()
   ```

4. Start the server:

   ```bash
   python app.py
   ```

## Endpoints

### Stocks

- `GET /stocks`: Get all stocks.
- `POST /stocks`: Create a new stock.
- `GET /stock/{ticker}`: Get details of a stock with the specified ticker.
- `PUT /stock/{ticker}`: Edit an existing stock with the specified ticker.
- `DELETE /stock/{ticker}`: Delete an existing stock with the specified ticker.

### Users

- `GET /users`: Get all users.
- `POST /users`: Create a new user.

## Usage

### Get all stocks

```bash
curl http://localhost:5000/stocks
```

### Create a new stock

```bash
curl -X POST http://localhost:5000/stocks -H "Content-Type: application/json" -d '{"companyid": 1, "companyname": "Company Inc.", "ticker": "ABC", "price": 10.0}'
```

### Get details of a stock

```bash
curl http://localhost:5000/stock/ABC
```

### Edit an existing stock

```bash
curl -X PUT http://localhost:5000/stock/ABC -H "Content-Type: application/json" -d '{"price": 20.0}'
```

### Delete an existing stock

```bash
curl -X DELETE http://localhost:5000/stock/ABC
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/MyFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/MyFeature`)
5. Create a new Pull Request
