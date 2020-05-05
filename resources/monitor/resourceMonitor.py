from config import db
from flask import  request, jsonify
from flask_restful import Resource
from models.monitor.monitor import tablemonitor
from schemas.monitor.schemaMonitor import monitor_schema,monitor_schemas

'''Consultas por filtro'''

#get all words
class getMonitor(Resource):
    def get(self):
        all_words = tablemonitor.query.all()
        result = monitor_schemas.dump(all_words)
        return jsonify(result)

class getTasksFailure(Resource):
    def get(self):
        tasksFailure = tablemonitor.query.filter_by(status = 'FAILURE')
        result = monitor_schemas.dump(tasksFailure)
        return jsonify(result)

class getTasksSuccess(Resource):
    def get(self):
        tasksSuccess = tablemonitor.query.filter_by(status = 'SUCCESS')
        result = monitor_schemas.dump(tasksSuccess)
        return jsonify(result)

class getTasksPending(Resource):
    def get(self):
        tasksPending= tablemonitor.query.filter_by(status = 'PENDING')
        result = monitor_schemas.dump(tasksPending)
        return jsonify(result)

class getTasksWorker1(Resource):
    def get(self):
        typeWorker = tablemonitor.query.filter_by(worker = 'Get/postWords')
        result = monitor_schemas.dump(typeWorker)
        return jsonify(result)

class getTasksWorker2(Resource):
    def get(self):
        typeWorker = tablemonitor.query.filter_by(worker = 'Edit/updateWord')
        result = monitor_schemas.dump(typeWorker)
        return jsonify(result)

'''Este metodo agrega la informacion que toma una tarea (id, estado, fecha e informacion de la cola)'''
def addTASK(task_id,status,res,date_done,traceback,worker,queue,routing_key,typeMethod):
    task_id= task_id
    status=status
    result=res
    date_done=date_done
    traceback=traceback
    worker=worker
    queue=queue
    routing_key=routing_key
    typeMethod=typeMethod

    new_task = tablemonitor(task_id,status,result,date_done,traceback,worker,queue,routing_key,typeMethod)
    db.session.add(new_task)
    db.session.commit()

    return "task agregado"

'''Este metodo actualiza la informacion de una tarea al terminar de ejecutarse, los parametros
   que se actualizan son el estado, el resultado y el trecerback(si llega a existir un error)'''
def updateTarea(task_idSuccess,statusSuccess,resultSuccess,tracebackSuccess):
    #time.sleep(3)
    task = tablemonitor.query.filter_by(task_id = task_idSuccess).update(dict(status=statusSuccess, result=resultSuccess,traceback=tracebackSuccess))
    db.session.commit()
    return 'tarea actualizada'
    
  