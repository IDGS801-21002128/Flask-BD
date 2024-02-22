from wtforms import Form,StringField,EmailField,IntegerField,TelField, validators

class UserForm(Form):
    nombre = StringField('nombre',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10,message="ingresa nombre valido")
        ])

   ## email = EmailField('email',[validators.Email(message="Ingrese un correo valido")])
    apaterno=TelField('apaterno',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10,message="ingresa apellido paterno valido")
        ])
    amaterno=TelField('amaterno ',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10,message="ingresa apellido materno valido")
        ])
    numeroCelular=IntegerField('nCelular',[
        validators.DataRequired(message="ingrese un numero celular valido")
    ])