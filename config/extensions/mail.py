from flask_mail import Mail, Message
from config import app


def email(task_id,typeMethod,now):

    Task_id=task_id
    TypeMethod=typeMethod
    Now=now
    
    msg = Message("Alerta de actividad API", recipients=[app.config['MAIL_USERNAME']])
    msg.body = "Hola, realizaste una peticion de tipo {} a las {} , con la identificacion {}".format(TypeMethod,Now, Task_id,app.config['MAIL_USERNAME'])
    mail.send(msg)
    return "email sended"

mail = Mail(app)