from flask import *
from forms import UserForm
from flask_wtf.csrf import CSRFProtect
from config import DevelomentConfig

from models import db
from models import Alumnos

app=Flask(__name__)
app.config.from_object(DevelomentConfig)
csrf=CSRFProtect()

@app.route("/ABC_Completo", methods=[ "GET", "POST"])
def ABCompleto():
    alumno = Alumnos.query.all()
    return render_template("ABC_Completo.html", alumnos=alumno)

@app.route("/eliminar", methods=[ "GET", "POST"])
def eliminar():
    formulario = UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alumno1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        formulario.id.data = request.args.get('id')
        formulario.nombre.data = alumno1.nombre 
        formulario.apaterno.data = alumno1.apaterno
        formulario.email.data = alumno1.email
        
    if request.method == 'POST':
        id = formulario.id.data
        alumno = Alumnos.query.get(id)
        db.session.delete(alumno)
        db.session.commit()
        return redirect(url_for("ABCompleto"))
    
    return render_template("eliminar.html", form=formulario)
 
 
@app.route("/modificar", methods=[ "GET", "POST"])
def modificar():
    formulario = UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alumno1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        formulario.id.data = request.args.get('id')
        formulario.nombre.data = alumno1.nombre 
        formulario.apaterno.data = alumno1.apaterno
        formulario.email.data = alumno1.email
        
    if request.method == 'POST':
        id = formulario.id.data
        alumno = Alumnos.query.get(id)
        alumno.nombre =formulario.nombre.data 
        alumno.apaterno =formulario.apaterno.data 
        alumno.email = formulario.email.data 
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for("ABCompleto"))
    
    return render_template("modificar.html", form=formulario)
 

@app.route("/",methods=['GET','POST'])
def index():
    formulario = UserForm(request.form)
    if request.method == 'POST':
        alumno = Alumnos(nombre = formulario.nombre.data, 
                         apaterno = formulario.apaterno.data,
                         amaterno = formulario.amaterno.data,
                         email = formulario.email.data)
        db.session.add(alumno)
        db.session.commit()
        print("Finalizó")
    return render_template("index.html", form=formulario)

@app.errorhandler(404)
def page_noit_found():
    return render_template("404.html"),404

@app.before_request
def before_request():
    g.nombre="Mario"
    print("Before 1")

@app.after_request
def after_request(response):
        print("after 3")
        return response
@app.route("/alumno",methods=['GET','POST'])
def alumno():
    print("alumno: {}".format(g.nombre))
    alumno_clase = UserForm(request.form)
    nombre,apaterno='',""
    amaterno=''
    email=""
    numeroCelular=''
    if request.method == "POST" and alumno_clase.validate():
       nombre=alumno_clase.nombre.data
       ##email= alumno_clase.email
       apaterno=alumno_clase.apaterno.data
       amaterno=alumno_clase.amaterno.data
       numeroCelular=alumno_clase.numeroCelular
       
       mensaje="BIENVENIDO  {}".format(nombre)
       flash(mensaje )

    return render_template("alumno.html",form=alumno_clase,nombre=nombre,apaterno=apaterno,amaterno=amaterno,numeroCelular=numeroCelular,email=email)



if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()