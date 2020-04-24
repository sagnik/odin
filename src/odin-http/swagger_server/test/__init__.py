import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../specs/')
        app.app.json_encoder = JSONEncoder
        app.add_api('odin.yaml')
        return app.app
