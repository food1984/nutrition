from sqlalchemy import (Column, Integer, String, Boolean, Float, Date,
                        ForeignKey)
from sqlalchemy.orm import relationship
from app import db


class BrandedFood(db.Model):
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    brand_owner = Column(String)
    gtin_upc = Column(String, primary_key=True)
    ingredients = Column(String)
    serving_size = Column(Integer)
    serving_size_unit = Column(String)
    household_serving_fulltext = Column(String)
    branded_food_category = Column(String)
    data_source = Column(String)
    modified_date = Column(Date)
    available_date = Column(Date)
    food = relationship("Food",
                        back_populates="branded_food")


class FoodCategory(db.Model):
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    description = Column(String)
    food = relationship("Food",
                        back_populates="food_category")


class Food(db.Model):
    fdc_id = Column(Integer, primary_key=True)
    data_type = Column(String(20))
    description = Column(String(200))
    food_category_id = Column(Integer, ForeignKey('food_category.id'))
    publication_date = Column(String(20))
    branded_food = relationship("BrandedFood", back_populates="food")
    food_attribute = relationship("FoodAttribute", back_populates="food")
    food_component = relationship("FoodComponent", back_populates="food")
    food_nutrient = relationship("FoodNutrient", back_populates="food")
    food_portion = relationship("FoodPortion", back_populates="food")
    food_category = relationship("FoodCategory", back_populates="food")
    food_nutrient_conversion_factor = relationship(
        "FoodNutrientConversionFactor", back_populates="food")
    foundation_food = relationship("FoundationFood", back_populates="food")


class FoodAttribute(db.Model):
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    seq_num = Column(Integer)
    food_attribute_type_id = Column(Integer,
                                    ForeignKey('food_attribute_type.id'))
    name = Column(String)
    value = Column(String)
    food = relationship("Food",
                        back_populates="food_attribute")
    food_attribute_type = relationship("FoodAttributeType",
                                  back_populates="food_attribute")


class FoodAttributeType(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    food_attribute = relationship("FoodAttribute",
                                  back_populates="food_attribute_type")


class FoodCalorieConversionFactor(db.Model):
    food_nutrient_conversion_factor_id = \
        Column(Integer, ForeignKey('food_nutrient_conversion_factor.id'),
               primary_key=True)
    protein_value = Column(Float)
    fat_value = Column(Float)
    carbohydrate_value = Column(Float)
    food_nutrient_conversion_factor = \
        relationship("FoodNutrientConversionFactor",
                     back_populates="food_calorie_conversion_factor")


class FoodComponent(db.Model):
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    name = Column(String)
    pct_weight = Column(Float)
    is_refuse = Column(Boolean)
    gram_weight = Column(Float)
    data_points = Column(Integer)
    min_year_acquired = Column(Integer)
    food = relationship("Food",
                        back_populates="food_component")


class FoodNutrient(db.Model):
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    nutrient_id = Column(Integer, ForeignKey('nutrient.id'))
    amount = Column(Float)
    data_points = Column(Integer)
    derivation_id = Column(Integer)
    min = Column(Float)
    max = Column(Float)
    median = Column(Float)
    footnote = Column(String)
    min_year_acquired = Column(Date)
    food = relationship("Food",
                        back_populates="food_nutrient")
    nutrient = relationship("Nutrient",
                    back_populates="food_nutrient")


class FoodNutrientConversionFactor(db.Model):
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    food_calorie_conversion_factor = relationship(
        "FoodCalorieConversionFactor",
        back_populates="food_nutrient_conversion_factor")
    food = relationship("Food",
                        back_populates="food_nutrient_conversion_factor")


class FoodNutrientDerivation(db.Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(20))
    description = Column(String)
    food_nutrient_source_id = Column(Integer, ForeignKey('food_nutrient_source.id'))
    food_nutrient_source = relationship("FoodNutrientSource",
                        back_populates="food_nutrient_derivation")


class FoodNutrientSource(db.Model):
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    description = Column(String(200))
    food_nutrient_derivation = relationship("FoodNutrientDerivation",
                        back_populates="food_nutrient_source")


class FoodPortion(db.Model):
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    seq_num = Column(Integer)
    amount = Column(Integer)
    measure_unit_id =  Column(Integer, ForeignKey('measure_unit.id'))
    portion_description = Column(String(200))
    modifier = Column(String(50))
    gram_weight = Column(Integer)
    data_points = Column(Integer)
    footnote = Column(String(50))
    min_year_acquired = Column(String(10))
    food = relationship("Food", back_populates="food_portion")
    measure_unit = relationship("MeasureUnit", back_populates="food_portion")


class FoodProteinConversionFactor(db.Model):
    id = Column(Integer, primary_key=True)
    value = Column(Float)


class FoodUpdateLogEntry(db.Model):
    id = Column(Integer, primary_key=True)
    description = Column(String(200))
    last_updated = Column(Date)


class FoundationFood(db.Model):
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    NDB_number = Column(Integer, primary_key=True)
    footnote = Column(String(200))
    food = relationship("Food",
                        back_populates="foundation_food")


class MeasureUnit(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    food_portion = relationship("FoodPortion",
                        back_populates="measure_unit")


class Nutrient(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    nutrient_nbr = Column(Integer)
    rank = Column(Integer)
    food_nutrient = relationship("FoodNutrient", back_populates="nutrient")


class NutrientIncomingName(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    nutrient_id = Column(Integer)


class WWEIAFoodCategory(db.Model):
    code = Column(Integer, primary_key=True)
    description = Column(String(200))
