from sqlalchemy import (Column, Integer, String, Boolean, Float, Date,
                        ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class FoodAttribute(Base):
    __tablename__ = 'food_attribute'
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer)
    seq_num = Column(Integer)
    food_attribute_type_id = Column(Integer)
    name = Column(String)
    value = Column(String)


class BrandedFood(Base):
    __tablename__ = 'branded_food'
    fdc_id = Column(Integer, primary_key=True)
    brand_owner = Column(String)
    gtin_upc = Column(String)
    ingredients = Column(String)
    serving_size = Column(Integer)
    serving_size_unit = Column(String)
    household_serving_fulltext = Column(String)
    branded_food_category = Column(String)
    data_source = Column(String)
    modified_date = Column(Date)
    available_date = Column(Date)


class FoodCategory(Base):
    __tablename__ = 'food_category'
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    description = Column(String)


class FoodCalorieConversionFactor(Base):
    __tablename__ = 'food_calorie_conversion_factor'
    food_nutrient_conversion_factor_id =  Column(Integer, primary_key=True)
    protein_value = Column(Float)
    fat_value = Column(Float)
    carbohydrate_value = Column(Float)


class FoodComponent(Base):
    __tablename__ = 'food_component'
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer)
    name = Column(String)
    pct_weight = Column(Float)
    is_refuse = Column(Boolean)
    gram_weight = Column(Float)
    data_points = Column(Integer)
    min_year_acquired = Column(Integer)


class Food(Base):
    __tablename__ = 'food'
    fdc_id = Column(Integer, primary_key=True)
    data_type = Column(String(200))
    description = Column(String(200))
    food_category_id = Column(String(10))
    publication_date = Column(String(20))
    food_portion = relationship("FoodPortion", back_populates="food")
    nutrient_conversion_factor = relationship("FoodNutrientConversionFactor",
                        back_populates="food_nutrient_conversion_factor")
    nutrient_derivation = relationship("FoodNutrientDerivation",
                                       back_populates="food")


class FoodPortion(Base):
    __tablename__ = 'food_portion'
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    seq_num = Column(Integer)
    amount = Column(Integer)
    measure_unit_id = Column(Integer)
    portion_description = Column(String(200))
    modifier = Column(String(50))
    gram_weight = Column(Integer)
    data_points = Column(Integer)
    footnote = Column(String(50))
    min_year_acquired = Column(String(10))
    food = relationship("Food", back_populates="food_portion")


class MeasureUnit(Base):
    __tablename__ = 'measure_unit'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))


class Nutrient(Base):
    __tablename__ = 'nutrient'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    nutrient_nbr = Column(Integer)
    rank = Column(Integer)


class FoodNutrientConversionFactor(Base):
    __tablename__ = 'food_nutrient_conversion_factor'
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    food = relationship("FoodNutrientConversionFactor",
                        back_populates="food_nutrient_conversion_factor")


class FoodUpdateLogEntry(Base):
    __tablename__ = 'food_update_log_entry'
    id = Column(Integer, primary_key=True)
    description = Column(String(200))
    last_updated = Column(Date)


class FoundationFood(Base):
    __tablename__ = 'foundation_food'
    fdc_id = Column(Integer, primary_key=True)
    NDB_number = Column(Integer)
    footnote = Column(String(200))


class FoodNutrientDerivation(Base):
    __tablename__ = 'food_nutrient_derivation'
    id = Column(Integer, primary_key=True)
    fdc_id = Column(Integer, ForeignKey('food.fdc_id'))
    seq_num = Column(Integer)
    amount = Column(Integer)
    measure_unit_id = Column(Integer)
    portion_description = Column(String(200))
    modifier = Column(String(50))
    gram_weight = Column(Integer)
    data_points = Column(Integer)
    footnote = Column(String(50))
    min_year_acquired = Column(String(10))
    food = relationship("FoodNutrientDerivation",
                        back_populates="food_nutrient_derivation")


class NutrientIncomingName(Base):
    __tablename__ = 'nutrient_incoming_name'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    nutrient_id = Column(Integer)


class FoodNutrientSource(Base):
    __tablename__ = 'food_nutrient_source'
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    description = Column(String(200))
    source_id = Column(Integer)


class FoodProteinConversionFactor(Base):
    __tablename__ = 'food_protein_conversion_factor'
    id = Column(Integer, primary_key=True)
    value = Column(Float)


class WWIEAFoodCategory(Base):
    __tablename__ = 'wweia_food_category'
    code = Column(Integer, primary_key=True)
    description = Column(String(200))
