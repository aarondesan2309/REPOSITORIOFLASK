from flask import Blueprint
taskRoute = Blueprint('tasks', __name__, url_prefix='/tasks')
#Creacion de rutas en el modulo rutas
#CRUD C. CRATE R . READ . U. UPDATE D. DELETE

@taskRoute.route('/')
def index():
    return 'Index'#ir a la base de datos dar el contenido de la tabla select *from 

@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show MIRANDA ES LA MAS PERRA DEL SALON DE 5 ICI B ' +str(id) #va a la base de datos y muetra el registro de la tabla especifico es un query select from task where id =3

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    return 'delete ' +str(id)

@taskRoute.route('/create', methods=('GET','POST'))
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    return 'update '+str(id)