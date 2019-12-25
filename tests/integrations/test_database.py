import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_fixtures import FixturesMixin
from app import (app, db)

from database import (Base, FoodAttribute, FoodCategory, FoodComponent,
                      FoodPortion, MeasureUnit, Nutrient, FoodNutrient,
                      FoodNutrientConversionFactor, FoodNutrientDerivation,
                      FoodNutrientSource, Food, NutrientIncomingName,
                      FoodUpdateLogEntry, FoodCalorieConversionFactor,
                      FoodProteinConversionFactor, FoodAttributeType,
                      WWIEAFoodCategory)


FixturesMixin.init_app(app, db)


class TestDatabase(unittest.TestCase):
    fixtures = [
            'food.json'
        ]

    @classmethod
    def setup_class(self):
        db.drop_all()
        db.create_all()

    @classmethod
    def teardown_class(self):
        db.drop_all()

    def test_001_owners(self):
        owners = db.session.query(Owner).all()
        assert len(owners) == 2, "Not equal to two owners"

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
