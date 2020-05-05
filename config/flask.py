from flask import Flask
from kombu import Queue,Exchange
from workerCelery.workerConfig import *
from flask_cors import CORS, cross_origin
from kombu.utils.url import safequote

class Config(object):
    '''Flask configurations'''
    
    #: configuration config credentials from SQS
    '''Se definen las credenciales otorgadas por AWS, además se establece 
       la region donde se encuentran alojados nuestros servicios''' 

    aws_access_key = safequote("AKIAJXK7AVU3A3QGYITQ")
    aws_secret_key = safequote("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")
    BROKER_TRANSPORT_OPTIONS= {'region': 'us-east-2'}

    #: configuration celery
    '''Se define la conexión entre la aplicacion y el BROKER (Amazon SQS), tambien se define
        la conexión a nuestra base de datos donde Celery alojará sus propios resultados y por
        ultimo creamos las colas con las cuales nuestros workers trabajan, los nombres y keys
        de las colas se encuentran en workerCelery/workerConfig.py'''

    CELERY_BROKER_URL="sqs://{aws_access_key}:{aws_secret_key}@".format(aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,)
    CELERY_RESULT_BACKEND='db+mysql://root:@localhost:3306/dictionary'
    CELERY_QUEUES = (
        Queue(queue1,Exchange('default'), routing_key=key1),
        Queue(queue2,Exchange('default'), routing_key=key2),
        Queue(queue3,Exchange('default'), routing_key=key3),
        Queue(queue4,Exchange('default'), routing_key=key4)
    )
     
    #: Sqlalchemy config values
    '''Configuración de SQLAlchemy'''

    SQLALCHEMY_DBAPI = "mysql"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_PARAMS = {"charset": "utf8"}
    SQLALCHEMY_DB_USER = "root"
    SQLALCHEMY_DB_PWD = ""
    SQLALCHEMY_DB_NAME = "dictionary"
    SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s/%s" % (
        SQLALCHEMY_DBAPI,
        SQLALCHEMY_DB_USER,
        SQLALCHEMY_DB_PWD,
        "localhost",
        SQLALCHEMY_DB_NAME
    )

    #: Mail config values
    '''Configuración de envio de correo'''

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'manuelmay47@gmail.com'  
    MAIL_DEFAULT_SENDER = 'manuelmay47@gmail.com' 
    MAIL_PASSWORD = 'gnqwzbsykdrwendz' 

#init app

__all__=['app']
app = Flask('__name__')
CORS(app)
app.config.from_object(Config)