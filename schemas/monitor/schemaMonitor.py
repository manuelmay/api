from config import ma

__all__=["monitorSchema"]

#monitor Schema
class monitorSchema(ma.Schema):
    class Meta:
        
        fields = ('id','task_id','status','result','date_done','traceback','worker','queue','routing_key','typeMethod')

#Init schema
monitor_schema = monitorSchema()
monitor_schemas = monitorSchema(many=True)