from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model.index import IndexModel
from api.schema.index import IndexSchema
from helper.normalize_text import normalize_word
from db import indexing_db

index_api = Blueprint('api', __name__)

@index_api.route('/index/<word>')
@swag_from({
    'parameters': [
        {
            "name": "word",
            "in": "path",
            "type": "string",
            "required": "true",
        }
    ],
    "responses": {
        HTTPStatus.OK.value: {
            "description": 'Return indexing line for a word',
            "schema": IndexSchema
        }
    }
})
def index(word):
    word = normalize_word(word)
    result = IndexModel()
    print(word)
    # print('======', indexing_db, '++++++++')
    if word in indexing_db:
        result = IndexModel(indexing_db[word]["count"], indexing_db[word]["lines"])

    return IndexSchema().dump(result), 200
