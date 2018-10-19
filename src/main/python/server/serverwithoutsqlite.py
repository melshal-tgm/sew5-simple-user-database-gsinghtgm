from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

USERS = {
    'user1': {'username': 'gsingh','email':'gsingh@student.tgm.ac.at','picture':'imgur.com/321'},
    'user2': {'username': 'gsingh2','email':'gsingh2@student.tgm.ac.at','picture':'imgur.com/222'},
    'user3': {'username': 'gsingh3','email':'gsingh3@student.tgm.ac.at','picture':'imgur.com/333'},
}


def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="Todo {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('user')



class User(Resource):
    def get(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        abort_if_user_doesnt_exist(todo_id)
        del USERS[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        user = {'user': args['user']}
        USERS[user_id] = user
        return user, 201


class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        user_id = int(max(USERS.keys()).lstrip('user')) + 1
        user_id = 'todo%i' % user_id
        USERS[user_id] = {'user': args['user']}
        return USERS[user_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True)