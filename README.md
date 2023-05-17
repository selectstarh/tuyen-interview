# Set Up
Check out the code. 

At root folder

1. Install requirements `pipenv install`
2. Start the server with: `pipenv run python -m flask run`
3. Run indexing script with `pipenv run python script/index.py`

Visit `http://127.0.0.1:5000/api/index/them` for the indexing api
Visit `http://127.0.0.1:5000/apidocs` for swagger

# Tests
Run
`pipenv run python -m unittest`

# What could be done Better
1. Unit Test
2. Better abstraction for future scaling and maintaining
3. Use a real database instead of hashmap in memory
4. Dockerize with `docker-compose`
5. When indexing, if errors out remember where left off and retry instead of indexing everything from beginning.
