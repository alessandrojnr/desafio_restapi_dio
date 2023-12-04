from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import AlterarHabilidades, Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0,
     'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']
    },
    {'id': 1,
     'nome': 'Galeani',
     'habilidades': ['Python', 'Django']
    }
]

class Home(Resource):
    def get(self):
        return "Bem vindo !!!"

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = f'Erro !!! Desenvolvedor de ID {id}, não existe .'
        except Exception:
            response = 'Erro !!! Procure o administrador da API .'
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return "Registro excluído com sucesso ."
    
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    

api.add_resource(Home, '/')
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(AlterarHabilidades, '/habilidades/<int:id>')



if __name__ == "__main__":
    app.run(debug= True)