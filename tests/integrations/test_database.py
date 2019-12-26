import unittest
from flask_fixtures import FixturesMixin
from app import (app, db)
from app.database import (
    FoodAttribute, FoodCategory, FoodComponent, FoodPortion, MeasureUnit,
    Nutrient, FoodNutrient, FoodNutrientConversionFactor,
    FoodNutrientDerivation, FoodNutrientSource, Food, NutrientIncomingName,
    FoodUpdateLogEntry, FoodCalorieConversionFactor,
    FoodProteinConversionFactor, FoodAttributeType, WWIEAFoodCategory
)


class TestDatabase(unittest.TestCase, FixturesMixin):
    fixtures = [
            'fixtures/food.json',
            'fixtures/food_category.json'
        ]

    app = app
    db = db

    @classmethod
    def setup_class(cls):
        db.drop_all()
        db.create_all()

    @classmethod
    def teardown_class(cls):
        db.drop_all()

    def test_food_all(self):
        food = db.session.query(Food).all()
        assert len(food) == 5, "Not equal to five food rows"

    def test_food_id(self):
        id = 346532
        data_type = 'branded_food'
        description = 'SWISS MISS Creamy Vanilla Pudding, 24 OZ'
        publication_date ='2019-04-01 00:00:00'
        food = db.session.query(Food).get(id)
        self.assertEqual(food.fdc_id, id, "Food.fdc_id doesn't match")
        self.assertEqual(food.data_type, data_type,
                         "Food.data_type doesn't match")
        self.assertEqual(food.description, description,
                         "Food.description doesn't match")
        self.assertEqual(food.publication_date, publication_date,
                         "Food.publication date doesn't match")

    def test_food_category_all(self):
        food = db.session.query(FoodCategory).all()
        assert len(food) == 4, "Not equal to four food category rows"

    def test_food_category_id(self):
        id = 6
        code = 600
        description = 'Soups, Sauces, and Gravies'
        food = db.session.query(FoodCategory).get(id)
        self.assertEqual(food.id, id, "FoodCategory.id doesn't match")
        self.assertEqual(food.code, code,
                         "FoodCategory.code doesn't match")
        self.assertEqual(food.description, description,
                         "FoodCategory.description doesn't match")


if __name__ == '__main__':
    unittest.main()
