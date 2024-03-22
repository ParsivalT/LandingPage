# Importa a classe Flask do módulo flask
from flask import Flask

# Importa o blueprint 'webui' do módulo api.blueprints
from landpage.ext import configuration


def minimal_app(**config):
    app = Flask(__name__, static_url_path="/static")

    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app
