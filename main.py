from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from route import get_routes

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

routes_args = get_routes(Resource, parser)

##
## Actually setup the Api resource routing here
##
for route_args in routes_args:
	print(route_args)
	api.add_resource(route_args["class"], route_args["endpoint"])

if __name__ == '__main__':
    app.run(debug=True)