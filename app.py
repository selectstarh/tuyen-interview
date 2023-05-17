def create_app():
    import sys
    import os
    import db

    current = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current)
    sys.path.append(parent)

    from flask import Flask
    from flasgger import Swagger
    from api.route.index import index_api

    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Select Star',
    }

    swagger = Swagger(app)

    app.config.from_pyfile('config.py')
    app.register_blueprint(index_api, url_prefix='/api')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
