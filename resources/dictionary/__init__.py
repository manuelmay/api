from config import api
from .resorurceDictionary import get_add_Words,get_delete_update_Word,update 

'''Endpoints'''
api.add_resource(get_add_Words, '/restwords')
api.add_resource(get_delete_update_Word, '/restwords/<idWord>')
api.add_resource(update, '/restwordsUpdate')