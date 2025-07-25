#Coding in utf-8 -*-
#Caracteres especiales

from flask import Flask, jsonify, request
from cliente import cliente 


app = Flask(__name__)

# Se expone el blueprint de cliente
app.register_blueprint(cliente)
@app.route('/', methods=['GET'])

def unida():
    return 'Server Flask is running on port 5003'

if __name__ == '__main__':
    app.run(debug=True, port=5003, host=('0.0.0.0'))

    #0.0.0.0 es una dirección IP que permite que la aplicación Flask sea accesible desde cualquier dirección IP de la red local.

 