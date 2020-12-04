from flask import Flask, jsonify
from flask_restplus import Resource, reqparse, Api
from flask_cors import CORS
from Model.spell_check import Spell_check

spell = Spell_check()

def factory():
    app = Flask(__name__, static_url_path='/static')
    app.url_map.strict_slashes = False
    CORS(app)
    return app


app = factory()
api = Api(app, version='1.0', title='Law Tech API',
          description='Law Tech API'
          )

contentParse = reqparse.RequestParser()
contentParse.add_argument('content', help="This field cannot be blank", required=True, action='append')
class spellClass(Resource):
    def post(self):
        data = contentParse.parse_args()
        print(data['content'])
        spell_errors = spell.spell_check(data['content'])
        ret = [{
        	'startPos': err['wordPos'],
        	'endPos': -1,
        	'alternativeWord': err['alternativeWord'] if len(err['alternativeWord']) > 0 else None
        } for err in spell_errors]
        print(spell_errors)
        return jsonify(ret)

api.add_resource(spellClass, '/api/spell/spellcheck')

if __name__ == "__main__":
    print('reloaded')
    app.run(host='0.0.0.0', port=5005, debug=True, use_reloader=False)

