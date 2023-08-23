import os
import json
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# cargar variable de entorno
load_dotenv()

app = Flask(__name__) 
## configuracion
app.config['DEBUG'] = True 
app.config['ENV'] = 'development'
## code here

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    saludo = {
        "mensaje": "Hola mi primera API con Flask"
    }
    return jsonify(saludo)


@app.route('/<name>/<int:age>', methods=['GET'])
def saludo(name, age):
    mensaje = {
        "msg": f"Hola, soy {name}, y mi edad es {age}"
    }
    return jsonify(mensaje)

@app.route('/api/search/<category>', methods=['GET'])
def search(category):
    # ?name=luis&lastname=rodriguez
    params = request.args
    
    print(params)
    
    return jsonify({ "msg": "Buscando", "category": category, "params": params })

@app.route('/api/search/<category>', methods=['POST'])
def search_post_put(category):
    # ?name=luis&lastname=rodriguez
    params = request.args
    
    print(params)
    print(request.data)
    
    # Recibir el string y convertirlo en json
    # datos_en_json = json.loads(request.data)
    
    # Recibir directamente los datos en json
    datos_en_json = request.get_json()
    
    print(datos_en_json["datos"])
    
    datos = request.json.get("datos")
    
    print(datos)
    
    return jsonify({ 
                    "msg": "Buscando", 
                    "category": category, 
                    "params": params,
                    "method": request.method,
                    "datos": datos_en_json
    })
    
    
@app.route('/api/search/<category>', methods=['PUT'])
def search_post_put_tipo_form(category):
    # ?name=luis&lastname=rodriguez
    params = request.args
    
    print(params)
    
    # accediendo a la informacion como formulario
    body = request.form
    
    print(body["name"])
    print(body["lastname"])
    
    
    return jsonify({ 
                    "msg": "Buscando", 
                    "category": category, 
                    "params": params,
                    "method": request.method,
                    "form": body 
    })



### fin code
if __name__ == '__main__':
    app.run()