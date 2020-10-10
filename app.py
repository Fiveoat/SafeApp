from flask import Flask, redirect, url_for
from flask_graphql import GraphQLView
from database_handler import db_session
from schema import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True,
                                                           context={'session': db_session}))


@app.route('/')
def index():
    return redirect(url_for('graphql'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
