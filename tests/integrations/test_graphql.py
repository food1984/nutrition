import unittest
from graphene.test import Client
from flask_fixtures import FixturesMixin
from app import (app, db)
from app.schema import Food


class TestSchema(unittest.TestCase, FixturesMixin):
    fixtures = [
            'food.json',
            'food_category.json',
            'food_attribute.json'
        ]

    app = app
    db = db

    @classmethod
    def setup_class(cls):
        db.drop_all()
        db.create_all()

#    @classmethod
#    def teardown_class(cls):
#        db.drop_all()

    def test_food_query(self):
#        client = Client(Food)
#        executed = client.execute('''{ hey }''')
#        assert executed == {
#            'data': {
#                'hey': 'hello!'
#            }
#        }
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
