from config import db
'''Modelo de la tabla donde se registran las peticiones'''

class tablemonitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id=db.Column(db.String(155))
    status=db.Column(db.String(45))
    result=db.Column(db.String(45))
    date_done=db.Column(db.DateTime)
    traceback=db.Column(db.String(150))
    worker=db.Column(db.String(45))
    queue=db.Column(db.String(45))
    routing_key=db.Column(db.String(45))
    typeMethod=db.Column(db.String(45))
    

    def __init__(self, task_id,status,result,date_done,traceback,worker,queue,routing_key,typeMethod):
        self.task_id = task_id
        self.status = status
        self.result = result
        self.date_done = date_done
        self.traceback = traceback
        self.worker = worker
        self.queue = queue
        self.routing_key = routing_key
        self.typeMethod = typeMethod
