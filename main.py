from flask import jsonify
from google.cloud import firestore

def insereCarro(request):
    request_json = request.get_json()
    def getAttribute(attr):
        if request.args and attr in request.args:
            return request.args.get(attr)
        elif request_json and attr in request_json:
            return request_json[attr]
        else:
            return null
    placa = getAttribute('placa')
    cor = getAttribute('cor')
    preco = getAttribute('preco')
    modelo = getAttribute('modelo')
    marca = getAttribute('marca')

    db = firestore.Client()
    carro_ref = db.collection('carros').document(placa)
    carro = carro_ref.get()

    if carro.exists:
        return 'O carro informado já está cadastrado!', 409
    else:
        carro_ref.set({
            'placa': placa,
            'cor': cor,
            'preco': preco,
            'modelo': modelo,
            'marca': marca
        })
        return 'O carro com a placa ' + placa + ' foi adicionado!', 200

def buscaCarro(request):
    request_json = request.get_json()
    request_json = request.get_json()
    def getAttribute(attr):
        if request.args and attr in request.args:
            return request.args.get(attr)
        elif request_json and attr in request_json:
            return request_json[attr]
        else:
            return null
    placa = getAttribute('placa')

    db = firestore.Client()
    carro_ref = db.collection('carros').document(placa)
    carro = carro_ref.get()

    if carro.exists:
        return jsonify(carro.to_dict()), 200
    else:
        return 'Carro nao encontrado.', 404