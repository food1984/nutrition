import unittest
import pytest
from app import db
from app.database import (
    FoodAttribute, FoodCategory, FoodComponent, FoodPortion, MeasureUnit,
    Nutrient, FoodNutrient, FoodNutrientConversionFactor,
    FoodNutrientDerivation, FoodNutrientSource, Food, NutrientIncomingName,
    FoodUpdateLogEntry, FoodCalorieConversionFactor,
    FoodProteinConversionFactor, FoodAttributeType, WWEIAFoodCategory
)


@pytest.fixture(scope='class')
def init_database():
    from os.path import (abspath, dirname, join)
    from glob import glob
    from flask_fixtures.loaders import JSONLoader
    from flask_fixtures import load_fixtures

    db.drop_all()
    db.create_all()

    base_dir = abspath(dirname(__file__))

    for fixture_file in glob(join(base_dir, 'fixtures', '*.json')):
        fixtures = JSONLoader().load(fixture_file)
        load_fixtures(db, fixtures)

    yield db
    db.drop_all()


@pytest.mark.usefixtures("init_database")
class TestDatabase(unittest.TestCase):
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

    def test_food_calorie_conversion_factor_all(self):
        food = db.session.query(FoodCalorieConversionFactor).all()
        self.assertEqual(len(food), 4)

    def test_food_component_all(self):
        food = db.session.query(FoodComponent).all()
        self.assertEqual(len(food), 5)

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
        self.assertEqual(len(food), 5)

    def test_food_nutrient_all(self):
        food = db.session.query(FoodNutrient).all()
        self.assertEqual(len(food), 4)

    def test_food_nutrient_derivation_all(self):
        food = db.session.query(FoodNutrientDerivation).all()
        self.assertEqual(len(food), 7)

    def test_food_nutrient_source_all(self):
        food = db.session.query(FoodNutrientSource).all()
        self.assertEqual(len(food), 4)

    def test_food_portion_all(self):
        food = db.session.query(FoodPortion).all()
        self.assertEqual(len(food), 4)

    def test_measure_unit_all(self):
        food = db.session.query(MeasureUnit).all()
        self.assertEqual(len(food), 5)

    def test_nutrient_all(self):
        food = db.session.query(Nutrient).all()
        self.assertEqual(len(food), 5)

    def test_nutrient_incoming_name_all(self):
        food = db.session.query(NutrientIncomingName).all()
        self.assertEqual(len(food), 6)

    def test_food_nutrient_conversion_factor_all(self):
        food = db.session.query(FoodNutrientConversionFactor).all()
        self.assertEqual(len(food), 7)

    def test_food_protein_conversion_factor_all(self):
        food = db.session.query(FoodProteinConversionFactor).all()
        self.assertEqual(len(food), 6)

    def test_food_attribute_type_all(self):
        food = db.session.query(FoodAttributeType).all()
        self.assertEqual(len(food), 5)

    def test_food_update_log_entry_all(self):
        food = db.session.query(FoodUpdateLogEntry).all()
        self.assertEqual(len(food), 4)

    def test_wweia_food_category_all(self):
        food = db.session.query(WWEIAFoodCategory).all()
        self.assertEqual(len(food), 6)

    def test_food_attribute_id(self):
        test_id = 5578
        fdc_id = 323121
        attribute_type_id = 1000
        food_value = "hot dog, frank, wiener"
        food = db.session.query(FoodAttribute).get(test_id)
        self.assertEqual(food.id, test_id, "FoodAttribute.id doesn't match")
        self.assertEqual(food.fdc_id, fdc_id,
                         "FoodAttribute.fdc_id doesn't match")
        self.assertEqual(food.name, None,
                         "FoodAttribute.name doesn't match")
        self.assertEqual(food.value, food_value,
                         "FoodAttribute.value doesn't match")
        self.assertEqual(food.seq_num, 0,
                         "FoodAttribute.seq_num doesn't match")
        self.assertEqual(food.food_attribute_type_id, attribute_type_id,
                         "FoodAttribute.attribute_type doesn't match")


if __name__ == '__main__':
    unittest.main()
