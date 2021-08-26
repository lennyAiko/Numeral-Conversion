from flask import Flask
from flask_restful import Resource, Api
import main as m

app = Flask(__name__)
api = Api(app)


class Convert(Resource):
    def get(self, pk):
        value = m.decision(pk)
        return value


api.add_resource(Convert, '/<path:pk>')
if __name__ == '__main__':
    app.run(debug=True)
