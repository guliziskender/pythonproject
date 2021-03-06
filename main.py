import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
tree = [{'myFavouriteTree': 'blue spruce'}

]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hello</h1>
<p>I love not men the less but nature more </p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/tree', methods=['GET'])
def api_all():
    return jsonify(tree)

if __name__ == "__main__":
    app.run(host='0.0.0.0')