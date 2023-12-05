from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):

        age_limit = int(request.args.get('age_limit', 0))

        data = pd.read_csv('users.csv')


        filtered_data = data[data['age'] >= age_limit]


        filtered_data = filtered_data.to_dict('records')

        return {'data': filtered_data}, 200







api.add_resource(Users, '/users')
api.add_resource(Cities, '/cities')
api.add_resource(Name, '/<string:name>')

if __name__ == '__main__':
    app.run()
