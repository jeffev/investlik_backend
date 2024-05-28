Aqui está o README do backend atualizado com as rotas fornecidas:

# InvestLink Backend

Welcome to the InvestLink API! This project serves as the backend for InvestLink, a website designed to help investors make informed decisions by providing easy and practical access to information.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jeffev/investlink_backend.git
   ```

2. Install dependencies:

   ```bash
   cd investlink_backend
   pip install -r requirements.txt
   ```

3. Start the server:

   ```bash
   python app.py
   ```

## Endpoints

### Stocks

- `GET /stocks`: Get all stocks.
- `POST /stocks`: Create a new stock.
- `GET /stocks/{ticker}`: Get details of a stock with the specified ticker.
- `PUT /stocks/{ticker}`: Edit an existing stock with the specified ticker.
- `DELETE /stocks/{ticker}`: Delete an existing stock with the specified ticker.

### FIIs

- `GET /fiis`: Get all FIIs.
- `POST /fiis`: Create a new FII.
- `GET /fiis/{ticker}`: Get details of an FII with the specified ticker.
- `PUT /fiis/{ticker}`: Edit an existing FII with the specified ticker.
- `DELETE /fiis/{ticker}`: Delete an existing FII with the specified ticker.

### Users

- `GET /users`: Get all users.
- `POST /users`: Create a new user.

### Favorites

- `GET /favorites/stocks`: Get all favorite stocks.
- `POST /favorites/stocks`: Add a stock to favorites.
- `DELETE /favorites/stocks/{ticker}`: Remove a stock from favorites.
- `GET /favorites/fiis`: Get all favorite FIIs.
- `POST /favorites/fiis`: Add an FII to favorites.
- `DELETE /favorites/fiis/{ticker}`: Remove an FII from favorites.

### Sentiment Analysis

- `GET /sentiment`: Get the market sentiment analysis.

### Machine Learning Predictions

- `GET /predictions/stocks`: Get ML-based predictions for all stocks.

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
curl http://localhost:5000/stocks/ABC
```

### Edit an existing stock

```bash
curl -X PUT http://localhost:5000/stocks/ABC -H "Content-Type: application/json" -d '{"price": 20.0}'
```

### Delete an existing stock

```bash
curl -X DELETE http://localhost:5000/stocks/ABC
```

### Get all FIIs

```bash
curl http://localhost:5000/fiis
```

### Create a new FII

```bash
curl -X POST http://localhost:5000/fiis -H "Content-Type: application/json" -d '{"companyid": 1, "companyname": "Company FII", "ticker": "FIIABC", "price": 100.0}'
```

### Get details of an FII

```bash
curl http://localhost:5000/fiis/FIIABC
```

### Edit an existing FII

```bash
curl -X PUT http://localhost:5000/fiis/FIIABC -H "Content-Type: application/json" -d '{"price": 200.0}'
```

### Delete an existing FII

```bash
curl -X DELETE http://localhost:5000/fiis/FIIABC
```

### Get all users

```bash
curl http://localhost:5000/users
```

### Create a new user

```bash
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{"username": "newuser", "email": "newuser@example.com"}'
```

### Get all favorite stocks

```bash
curl http://localhost:5000/favorites/stocks
```

### Add a stock to favorites

```bash
curl -X POST http://localhost:5000/favorites/stocks -H "Content-Type: application/json" -d '{"ticker": "ABC"}'
```

### Remove a stock from favorites

```bash
curl -X DELETE http://localhost:5000/favorites/stocks/ABC
```

### Get all favorite FIIs

```bash
curl http://localhost:5000/favorites/fiis
```

### Add an FII to favorites

```bash
curl -X POST http://localhost:5000/favorites/fiis -H "Content-Type: application/json" -d '{"ticker": "FIIABC"}'
```

### Remove an FII from favorites

```bash
curl -X DELETE http://localhost:5000/favorites/fiis/FIIABC
```

### Get market sentiment analysis

```bash
curl http://localhost:5000/sentiment
```

### Get ML-based predictions for all stocks

```bash
curl http://localhost:5000/predictions/stocks
```