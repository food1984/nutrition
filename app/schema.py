import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, \
    SQLAlchemyConnectionField
from .database import Food as FoodModel, FoodAttribute as FoodAttributeModel, \
    FoodCategory as FoodCategoryModel, BrandedFood as BrandedFoodModel, \
    FoodAttributeType as FoodAttributeTypeModel


class BrandedFood(SQLAlchemyObjectType):
    class Meta:
        model = BrandedFoodModel
        interfaces = (relay.Node, )


class BrandedFoodConnections(relay.Connection):
    class Meta:
        node = BrandedFood


class FoodAttributeType(SQLAlchemyObjectType):
    class Meta:
        model = FoodAttributeTypeModel
        interfaces = (relay.Node, )


class FoodAttributeTypeConnections(relay.Connection):
    class Meta:
        node = FoodAttributeType


class Food(SQLAlchemyObjectType):
    class Meta:
        model = FoodModel
        interfaces = (relay.Node, )


class FoodConnections(relay.Connection):
    class Meta:
        node = Food


class FoodAttribute(SQLAlchemyObjectType):
    class Meta:
        model = FoodAttributeModel
        interfaces = (relay.Node, )


class FoodAttributeConnections(relay.Connection):
    class Meta:
        node = FoodAttribute


class FoodCategory(SQLAlchemyObjectType):
    class Meta:
        model = FoodCategoryModel
        interfaces = (relay.Node, )


class FoodCategoryConnections(relay.Connection):
    class Meta:
        node = FoodCategory


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_food = SQLAlchemyConnectionField(FoodConnections)
    all_branded_food = SQLAlchemyConnectionField(BrandedFoodConnections)
    all_food_attribute = SQLAlchemyConnectionField(FoodAttributeConnections)
    all_food_attribute_type = SQLAlchemyConnectionField(
        FoodAttributeTypeConnections)
    all_food_category = SQLAlchemyConnectionField(FoodCategoryConnections)


schema = graphene.Schema(query=Query)
