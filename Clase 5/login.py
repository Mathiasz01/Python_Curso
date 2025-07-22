from flask import  Blueprint,Flask, jsonify, request


login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])

def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')
    print(user, password)
    print('User enviado:', user,' Password enviado:', password)

    codRes, menRes, accion, rol = inicializarvariables(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes, 
        'usuario': user,
        'accion': accion,
        'rol': rol
    }

    return jsonify(salida)




def inicializarvariables(user, password):
    codRes = 'Sin_Error'
    menRes = 'OK'       
    accion = 'login exitoso'
    rol = 'Admin'
    userlocal = 'mathias'
    passwordlocal = 'unida123'


    try:
        if user == userlocal and password == passwordlocal:
            print('Login exitoso')
            accion = 'login exitoso'
        else:
            codRes = 'Error' 
            menRes = 'Usuario o contraseña incorrectos'
            accion = 'login fallido'
            rol = 'N/A'
            user = 'N/A'
    except Exception as e:
        print('Error en el login:', e)
        codRes = 'Error'
        menRes = 'Error al procesar la solicitud'
        accion = 'error en el login'
        rol = 'N/A'
        user = 'N/A'
        return codRes, menRes, accion, rol, user



    return codRes, menRes, accion, rol, user