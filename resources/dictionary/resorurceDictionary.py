from config import db
from datetime import datetime
from flask_restful import Resource
from flask import  request, jsonify
from workerCelery.workerConfig import *
from models.dictionary.tableDictionary import tabledictionary
from schemas.dictionary.schemaTableDictionary import tabledictionary_schema,tabledictionary_schemas

#get all words
class get_add_Words(Resource):
    def get(self):
        #import celery task
        from workerCelery.tasksCelery import Palabras,addTask,updateTask
        
        '''Palabras es un metodo, a través del apply_async mandamos el proceso 
            del metodo a la cola, para mandar una tarea a una cola en especifica
            se necesita colocar el nombre de la cola en el parametro "queue" dentro
            del parentesis del apply_async'''

        result= Palabras.apply_async(kwargs=None,queue=queue1,routing_key=key1)
    
        '''Registro de task '''
        task_id=result.task_id
        status=result.status
        res=''
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        traceback=result.traceback
        worker=worker1
        queue=queue1
        routing_key=key1
        typeMethod='GET'
        
        '''agregando task a tabla monitor:
           "addTask" agrega la informacion del metodo "Palabras" a la tabla monitor, esta tarea se
           ejecuta en segundo plano'''

        addTask.apply_async(args=[task_id, status,res,now,traceback,worker, queue, routing_key,typeMethod],
                            kwargs=None,queue=queue3,routing_key=key3)
       
        while True:
            if result.ready() == False:  
                continue
            else:
                task_idSuccess=result.task_id
                statusSuccess= result.status
                resultSuccess=result.result
                tracebackSuccess=result.traceback

                '''Actualizando estado de task:
                   "updateTask" registra la informacion final del metodo "Palabras", es decir
                    actualiza su estado, el resultado y el tracerback(solo si ocurre un error)'''

                updateTask.apply_async(args=[task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess],
                                        kwargs=None,queue=queue3,routing_key=key3) 
                #execute the consult
                all_words = tabledictionary.query.all()
                result = tabledictionary_schemas.dump(all_words)
                return jsonify(result)
                break
    
    #create a new word
    def post(self):
        from workerCelery.tasksCelery import validationWord,addTask,updateTask,sendEmail

        expression=request.json['expression']
        definition=request.json['definition']

        result= validationWord.apply_async(args=[expression],kwargs=None,queue=queue1,routing_key=key1)
        '''Registro de task '''
        task_id=result.task_id
        status=result.status
        res=''
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        traceback=result.traceback
        worker=worker1
        queue=queue1
        routing_key=key1
        typeMethod='POST'
        
        '''Agrega la informacion inicial del metodo "validationWord" a la tabla monitor'''

        addTask.apply_async(args=[task_id, status,res,now,traceback,worker, queue, routing_key,typeMethod],
                            kwargs=None,queue=queue3,routing_key=key3)

        while True:
            if result.ready() == False:
                continue
            else: 
                task_idSuccess=result.task_id

                '''Se evalua si los datos recibidos por post estan vacios o si ya existen
                    en la base de datos, si estos llegan a ser ciertos, se carga una nueva
                    informacion de la tarea "validationWord" donde "updateTask" se encarga
                    de actualizar la informacion de la tarea y posteriormente se envia un email'''

                if  result.get() == "La palabra ya existe":
                    statusSuccess= 'FAILURE'
                    resultSuccess='Palabra no agregada'
                    tracebackSuccess='La palabra ya existe'

                    updateTask.apply_async(args=[task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess],
                                            kwargs=None,queue=queue3,routing_key=key3) 

                    sendEmail.apply_async(args=[task_id,typeMethod,now], kwargs=None,queue=queue4,routing_key=key4)
                else:
                    if (expression =='' or definition == '') or (expression=='' and definition==''):
                        statusSuccess= 'FAILURE'
                        resultSuccess='Palabra no agregada'
                        tracebackSuccess='Campos vacios'

                        updateTask.apply_async(args=[task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess],
                                                kwargs=None,queue=queue3,routing_key=key3)  

                        sendEmail.apply_async(args=[task_id,typeMethod,now], kwargs=None,queue=queue4,routing_key=key4)

                    else:
                        '''Si los datos recibidos son correctos y no s encuentran
                           registrados en la base de datos, entonces se agrega y se 
                           registra la informacion actual de la tarea y posteriormente 
                           se ejecuta el envio de email'''

                        new_word = tabledictionary(expression,definition)
                        db.session.add(new_word)
                        db.session.commit()

                        statusSuccess= result.status
                        resultSuccess=result.result
                        tracebackSuccess=result.traceback
                       
                        updateTask.apply_async(args=[task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess],
                                                kwargs=None,queue=queue3,routing_key=key3) 

                        sendEmail.apply_async(args=[task_id,typeMethod,now], kwargs=None,queue=queue4,routing_key=key4)

                        return tabledictionary_schema.jsonify(new_word)
                break
        
 

#get a word
class get_delete_update_Word(Resource):
    def get(self,idWord):
        from workerCelery.tasksCelery import Palabra,addTask,updateTask
        result= Palabra.apply_async(queue=queue2,routing_key=key2)

        '''Registro de task '''
        task_id=result.task_id
        status=result.status
        res=''
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        traceback=result.traceback
        worker=worker2
        queue=queue2
        routing_key=key2
        typeMethod='GET'
        
        addTask.apply_async(args=[task_id, status,res,now,traceback,worker, queue, routing_key,typeMethod],
                            kwargs=None,queue=queue3,routing_key=key3)
      
        while True:
            if result.ready() == False:                
                continue
            else:  
                task_idSuccess=result.task_id
                statusSuccess= result.status
                resultSuccess=result.result
                tracebackSuccess=result.traceback

                '''Actualizando estado de task'''
                updateTask.apply_async(args=[task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess],
                                        kwargs=None,queue=queue3,routing_key=key3)  

                word= tabledictionary.query.get(idWord)
                
                return tabledictionary_schema.jsonify(word)       
                break
    
        
    
    #delete a word
    def delete(self,idWord):
        from workerCelery.tasksCelery import DeleteWord,addTask,updateTask,sendEmail
        
        result= DeleteWord.apply_async(queue=queue2,routing_key=key2)
        '''Registro de task '''
        task_id=result.task_id
        status=result.status
        res=''
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        traceback=result.traceback
        worker=worker2
        queue=queue2
        routing_key=key2
        typeMethod='DELETE'
        
        addTask.apply_async(args=[task_id, status,res,now,traceback,worker, queue, routing_key,typeMethod],
                            kwargs=None,queue=queue3,routing_key=key3)
        
        while True:
            if result.ready() == False:                
                continue
            else:
                task_idSuccess=result.task_id
                statusSuccess= result.status
                resultSuccess=result.result
                tracebackSuccess=result.traceback

                '''Actualizando estado de task'''
                updateTask.apply_async(args=[task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess],
                                        kwargs=None,queue=queue3,routing_key=key3) 

                word = tabledictionary.query.get(idWord)
                db.session.delete(word)
                db.session.commit()
                sendEmail.apply_async(args=[task_id,typeMethod,now], kwargs=None,queue=queue4,routing_key=key4)
                return  tabledictionary_schema.jsonify(word)     
                break


class update(Resource):
    #update a word
    def put(self):  
        from workerCelery.tasksCelery import UpdateWord,addTask,updateTask,sendEmail
        result = UpdateWord.apply_async(queue=queue2,routing_key=key2)

        '''Registro de task '''
        task_id=result.task_id
        status=result.status
        res=''
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        traceback=result.traceback
        worker=worker2
        queue=queue2
        routing_key=key2
        typeMethod='PUT'
        
        addTask.apply_async(args=[task_id, status,res,now,traceback,worker, queue, routing_key,typeMethod],
                            kwargs=None,queue=queue3,routing_key=key3)

        while True:
            if result.ready() == False:              
                continue
            else:
                expression=request.json['expression']
                definition=request.json['definition']
                idWord=request.json['idWord']

                task_idSuccess=result.task_id
                if (expression =='' or definition == '') or (expression=='' and definition==''):
                    statusSuccess= 'FAILURE'
                    resultSuccess='Expresion no actualizada'
                    tracebackSuccess='Campos vacios'

                    updateTask.apply_async(args=[task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess],
                                            kwargs=None,queue=queue3,routing_key=key3) 

                else:
                    word = tabledictionary.query.get(idWord)
                    word.expression = expression
                    word.definition = definition
            
                    db.session.commit()

                    statusSuccess= result.status
                    resultSuccess=result.result
                    tracebackSuccess=result.traceback
                    
                    updateTask.apply_async(args=[task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess],
                                            kwargs=None,queue=queue3,routing_key=key3)

                    sendEmail.apply_async(args=[task_id,typeMethod,now], kwargs=None,queue=queue4,routing_key=key4)
                    
                    return tabledictionary_schema.jsonify(word)  
                
                break

'''metodo para validar si existe una palabra en la base de datos'''
def validarPalabra(expression):
    word = tabledictionary.query.filter_by(expression = expression)
    n=word.count()
    if n>0:
        return "La palabra ya existe"
    else:
        return "Expresion agregada"