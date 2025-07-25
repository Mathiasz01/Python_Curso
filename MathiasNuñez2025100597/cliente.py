from flask import Flask, Blueprint, jsonify, request

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def llamarServicioCliente():
    user = request.json.get('user')
    password = request.json.get('password')
    print('User enviado:', user, ' Password enviado:', password)

    codRes, menRes, accion, ci, nombre =  iniciarlizarVariables(user, password)
    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'accion': accion,
        'nombre': nombre,
        'ci': ci,
    }
    return jsonify(salida)

def iniciarlizarVariables(user, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    accion = 'Succes'
    ci = '7496297'
    nombre = 'Mathias'
    try:
        if user == 'Mathias' and ci == '7496297':
            print('Login exitoso')
            accion = 'Succes'
        else:
            codRes = 'ERROR'
            menRes = 'Error cliente'
            ci = '7496297'
            accion = 'Cliente no está en el sistema'
            nombre = 'Mathias'
    except Exception as e:
        print('Error en el cliente:', e)
        codRes = 'ERROR'
        menRes = 'Error cliente'
        accion = 'Error en el cliente'
        ci = '7496297'
        nombre = 'Mathias'

    return codRes, menRes, accion, ci, nombre
