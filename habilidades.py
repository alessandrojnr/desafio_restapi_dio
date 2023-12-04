import json
from flask import request
from flask_restful import Resource


lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)
        if dados not in lista_habilidades:
            lista_habilidades.append(dados)
            return f"{dados} adicionado com sucesso"
        else:
            return "Habilidade já existe no banco de dados."
    

class AlterarHabilidades(Resource):
    def get(self,id):
        try:
            return lista_habilidades[id]
        except:
            return f'ID de habilidade na posição {id} não cadastrada. Por favor contate a central da API'
        
    def put(self,id):
        dados  = json.loads(request.data)
        lista_habilidades[id] = dados
        return f'Lista de habilidades alterada com sucesso'



    def delete(self,id):
        lista_habilidades.pop(id)
        return f'O item {lista_habilidades[id]} foi excluido com sucesso'
        

