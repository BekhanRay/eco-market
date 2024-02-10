The ECO-Market API is an online store api whose features include 
the admin panel, 
shopping cart, 
product cards, 
order history and all can be expanded through Docker.
SSL version is written and works.
To run the code at home:
```
  git clone https://github.com/BekhanRay/eco-market.git
```
write your own .env :
```
SECRET_KEY=Your_secret_key
DEBUG=True
PRODUCTION=False


PG_NAME=examle_db
PG_USER=your_user
PG_PASSWORD=password
PG_HOST=postgres
PG_PORT=5432
```
enter :
```
  cd eco-market/
```
docker-compose :
```
  docker-compose up -d --build
```
and so the project goes on your pc/server
