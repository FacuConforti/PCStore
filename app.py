from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configura tu aplicación Flask aquí

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/categorias')
def categorias():
    return render_template('categorias.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

#CONFIGURACIONES PARA LA BASE DE DATOS

# Configura la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/pc_store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crea una instancia de SQLAlchemy
db = SQLAlchemy(app)

# Define el modelo de la tabla 'productos'
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    precio = db.Column(db.Integer)
    id_categoria = db.Column(db.Integer)
    activo = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def mostrar_productos():
    # Consulta todos los productos de la base de datos
    productos = Producto.query.all()
    # Renderiza la plantilla HTML y pasa los productos como contexto
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)

