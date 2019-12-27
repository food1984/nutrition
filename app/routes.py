from flask_graphql import GraphQLView
from .schema import schema, FoodAttribute, Food
from app import app


@app.route('/')
def hello_world():
    return 'Hello World!'


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)
