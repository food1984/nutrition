import sys
from os.path import (join, abspath, dirname)
from json import loads, dumps
import unittest
from graphene.test import Client
from flask_fixtures import FixturesMixin
from testclass.testclass import TestClass
from app import (app, db)
from app.schema import schema


""""
@pytest.fixture(scope='module')
def init_database():
    fixtures = [
            'branded_food.json',
            'food.json',
            'food_calorie_conversion_factor.json',
            'food_category.json',
            'food_component.json',
            'food_attribute.json',
            'food_attribute_type.json'
        ]

    dir_name = join(abspath(dirname(__file__)), 'files')

    db.drop_all()
    db.create_all()

    yield db  # this is where the testing happens!

    db.drop_all()
"""


class TestSchema(unittest.TestCase, FixturesMixin):
    fixtures = [
            'branded_food.json',
            'food.json',
            'food_calorie_conversion_factor.json',
            'food_category.json',
            'food_component.json',
            'food_attribute.json',
            'food_attribute_type.json'
        ]

    app = app
    db = db
    dir_name = join(abspath(dirname(__file__)), 'files')
    client = Client(schema)

    @classmethod
    def setup_class(cls):
        db.drop_all()
        db.create_all()

#    @classmethod
#    def teardown_class(cls):
#        db.drop_all()

    def test_food_query(self):
        test_data = TestClass(self.dir_name,
                              sys._getframe(  ).f_code.co_name)
        test_data.load_files()

        executed = self.client.execute(test_data.get_send_request())
        self.assertEqual(loads(dumps(executed['data'])),
                         test_data.get_expected_result()['data'])

    def test_food_attribute_query(self):
        test_data = TestClass(self.dir_name,
                              sys._getframe(  ).f_code.co_name)
        test_data.load_files()

        executed = self.client.execute(test_data.get_send_request())
        self.assertEqual(loads(dumps(executed['data'])),
                         test_data.get_expected_result()['data'])

    def test_food_category_query(self):
        test_data = TestClass(self.dir_name,
                              sys._getframe(  ).f_code.co_name)
        test_data.load_files()

        executed = self.client.execute(test_data.get_send_request())
        self.assertEqual(loads(dumps(executed['data'])),
                         test_data.get_expected_result()['data'])

    def test_branded_food_query(self):
        test_data = TestClass(self.dir_name,
                              sys._getframe(  ).f_code.co_name)
        test_data.load_files()

        executed = self.client.execute(test_data.get_send_request())
        self.assertEqual(loads(dumps(executed['data'])),
                         test_data.get_expected_result()['data'])


if __name__ == '__main__':
    unittest.main()
