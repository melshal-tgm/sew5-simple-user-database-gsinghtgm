from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json
import os
app = Flask(__name__)
api = Api(app)
db=os.path.dirname(os.path.realpath(__file__))+'\\users.json'
with open(db) as json_file:
    USERS = json.load(json_file)


def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="User {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('user')


class User(Resource):
    def get(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        with open(db, 'w') as outfile:
            json.dump(USERS, outfile)
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        user = {'user': args['user']}
        USERS[user_id] = user
        with open(db, 'w') as outfile:
            json.dump(USERS, outfile)
        return user, 201


class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        user_id = int(max(USERS.keys()).lstrip('user')) + 1
        user_id = 'user%i' % user_id
        USERS[user_id] = {'user': args['user']}
        return USERS[user_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True)