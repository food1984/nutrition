import unittest
from graphene.test import Client
from flask_fixtures import FixturesMixin
from app import (app, db)
from app.schema import schema


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
        client = Client(schema)
        query = """{
  allFood {
    edges {
      node {
        description
        id
        fdcId
        dataType
        foodCategoryId
        publicationDate
      }
    }
  }
}"""
        expected_result = {
  "data": {
    "allFood": {
      "edges": [
        {
          "node": {
            "description": "WOLF Chili Without Beans",
            "id": "Rm9vZDozNDY0NjQ=",
            "fdcId": "346464",
            "dataType": "branded_food",
            "foodCategoryId": 0,
            "publicationDate": "2019-04-01 00:00:00"
          }
        },
        {
          "node": {
            "description": "SANALAC Non Fat Dry Milk, 1 QT",
            "id": "Rm9vZDozNDY0NzA=",
            "fdcId": "346470",
            "dataType": "branded_food",
            "foodCategoryId": 0,
            "publicationDate": "2019-04-01 00:00:00"
          }
        },
        {
          "node": {
            "description": "SWISS MISS Hot Cocoa Mix Dark Chocolate Sensation Envelopes, 10 OZ",
            "id": "Rm9vZDozNDY1MTk=",
            "fdcId": "346519",
            "dataType": "branded_food",
            "foodCategoryId": 0,
            "publicationDate": "2019-04-01 00:00:00"
          }
        },
        {
          "node": {
            "description": "SWISS MISS Creamy Vanilla Pudding, 24 OZ",
            "id": "Rm9vZDozNDY1MzI=",
            "fdcId": "346532",
            "dataType": "branded_food",
            "foodCategoryId": 0,
            "publicationDate": "2019-04-01 00:00:00"
          }
        },
        {
          "node": {
            "description": "SWISS MISS Creamy Milk Chocolate Pudding, 24 OZ\"",
            "id": "Rm9vZDozNDY1MzM=",
            "fdcId": "346533",
            "dataType": "branded_food",
            "foodCategoryId": 0,
            "publicationDate": "2019-04-01 00:00:00"
          }
        }
      ]
    }
  }
}
        executed = client.execute(query)
        self.assertEqual(executed, dict(expected_result))


if __name__ == '__main__':
    unittest.main()
