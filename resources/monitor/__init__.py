from config import api
from .resourceMonitor import getMonitor,getTasksFailure,getTasksSuccess,getTasksPending,getTasksWorker1,getTasksWorker2

'''Endpoints'''
api.add_resource(getMonitor, '/monitor/allTasks')
api.add_resource(getTasksFailure, '/monitor/taskFailure')
api.add_resource(getTasksSuccess, '/monitor/taskSuccess')
api.add_resource(getTasksPending, '/monitor/taskPending')
api.add_resource(getTasksWorker1, '/monitor/taskWorker1')
api.add_resource(getTasksWorker2, '/monitor/taskWorker2')