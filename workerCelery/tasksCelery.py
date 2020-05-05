from config import app 
from .run_celery import make_celery
from resources.monitor.resourceMonitor import addTASK,updateTarea
from resources.dictionary.resorurceDictionary import validarPalabra
import time

'''Instanciando Celery con la aplicacion de flask'''
celery= make_celery(app)

'''Declarando tareas asincronas, los siguientes metodos estan vacios
    ya que son de ejemplo'''
    
@celery.task(name='Palabras')
def Palabras():
    return 'Lista de palabras'

@celery.task(name='deleteWord')
def DeleteWord():
    return 'Palabra eliminada'

@celery.task(name='updateWord')
def UpdateWord():
    
    return 'Palabra actualizada'

@celery.task(name='Palabra')
def Palabra():
    time.sleep(3)
    return 'Palabra seleccionada'


'''Task con funciones:
    estas tareas tienen funcionamiento el cual se ejecutan de 
    manera asincrona'''

@celery.task(name='newWord')
def validationWord(expression):
    return validarPalabra(expression)

@celery.task(name='addInfoTask')
def addTask(task_id,status,res,date_done,traceback,worker,queue,routing_key,typeMethod):
    return addTASK(task_id,status,res,date_done,traceback,worker,queue,routing_key,typeMethod)

@celery.task(name='updatetask')
def updateTask(task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess):
    return updateTarea(task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess)   

@celery.task(name='Email')
def sendEmail(task_id,typeMethod,now):
    from config.extensions.mail import email
    return email(task_id,typeMethod,now)
