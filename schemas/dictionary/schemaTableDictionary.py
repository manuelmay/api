from config import ma

__all__=["tabledictionarySchema"]

#tabledictionary Schema
class tabledictionarySchema(ma.Schema):
    class Meta:
        fields = ('idWord','expression','definition')

#Init schema
tabledictionary_schema = tabledictionarySchema()
tabledictionary_schemas = tabledictionarySchema(many=True)