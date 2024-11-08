from flask import Flask
from myapp.config import DevConfig
from myapp.tasks.controller import taskRoute
app = Flask(__name__)#el objeto se construye a traves de la carpeta flask 
app.register_blueprint(taskRoute)#
#app.debug = True
#esta ruta raiz de nuestro proyecto 
app.config.from_object(DevConfig)
@app.route('/')#ruta raiz del proyecto entonces busca e imprime el hello world
def hello_world() -> str:
    return ' Hello world'