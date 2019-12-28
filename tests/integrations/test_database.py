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

    @classmethod
    def teardown_class(cls):
        db.drop_all()

    def test_food_all(self):
        food = db.session.query(Food).all()
        self.assertEqual(len(food), 5, "Not equal to five food rows")

    def test_food_id(self):
        test_id = 346532
        data_type = 'branded_food'
        description = 'SWISS MISS Creamy Vanilla Pudding, 24 OZ'
        publication_date ='2019-04-01 00:00:00'
        food = db.session.query(Food).get(test_id)
        self.assertEqual(food.fdc_id, test_id, "Food.fdc_id doesn't match")
        self.assertEqual(food.data_type, data_type,
                         "Food.data_type doesn't match")
        self.assertEqual(food.description, description,
                         "Food.description doesn't match")
        self.assertEqual(food.publication_date, publication_date,
                         "Food.publication date doesn't match")

    def test_food_category_all(self):
        food = db.session.query(FoodCategory).all()
        self.assertEqual(len(food), 4, "Not equal to four food category rows")

    def test_food_category_id(self):
        test_id = 6
        code = 600
        description = 'Soups, Sauces, and Gravies'
        food = db.session.query(FoodCategory).get(test_id)
        self.assertEqual(food.id, test_id, "FoodCategory.id doesn't match")
        self.assertEqual(food.code, code,
                         "FoodCategory.code doesn't match")
        self.assertEqual(food.description, description,
                         "FoodCategory.description doesn't match")

    def test_food_attribute_all(self):
        food = db.session.query(FoodAttribute).all()
        self.assertEqual(len(food), 4, "Not equal to four food attribute rows")

    def test_food_attribute_id(self):
        test_id = 66690
        fdc_id = 605282
        food_name = 'Food Category'
        food_value = "1"
        food = db.session.query(FoodAttribute).get(test_id)
        self.assertEqual(food.id, test_id, "FoodAttribute.id doesn't match")
        self.assertEqual(food.fdc_id, fdc_id,
                         "FoodAttribute.fdc_id doesn't match")
        self.assertEqual(food.name, food_name,
                         "FoodAttribute.name doesn't match")
        self.assertEqual(food.value, food_value,
                         "FoodAttribute.value doesn't match")
        self.assertEqual(food.seq_num, None,
                         "FoodAttribute.seq_num doesn't match")


if __name__ == '__main__':
    unittest.main()
