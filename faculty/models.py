from django.db import models
import pymongo
# from .serializers import User_serializer
from bson import json_util
from datetime import datetime
from .auth import AuthHandlerIns

# Create your models here.
# from utils import get_db_handle
from pymongo import MongoClient

# Create your models here.

connection_string='mongodb+srv://admin:admin@cluster0.bn80fcq.mongodb.net/test'
db_name='mac-test'
client = pymongo.MongoClient(connection_string)
db = client[db_name]
faculty = db['faculty']



class User:

    def create_user(self,username,password):
        now = datetime.now()
        p = AuthHandlerIns.get_password_hash(password=password)
        print(p)
        k=faculty.insert_one({'_id':str(now),'username':username,'password':p,'Verified':'False'})
        print(k)
        print('lllllllll')

    def get_user(self,username=None):
        if not username:
            k=[json_util.loads(json_util.dumps(i)) for i in faculty.find() ]
        else:
            k= faculty.find_one({'username':username,'Verified':'True'})

        return k

    def update_perms(self,username,branch_name,branch_place,branch_manager=False,):
        if branch_manager:
            faculty.find_one_and_update({"username":username},{"$push":{"branch_manager":branch_manager,"name":branch_name,"place":branch_place}},upsert=True)

            
    def verify(self, id):
        faculty.find_one_and_update({'_id':id},{"$set":{'Verified':'True'}})

    def delete(self, id):
        faculty.find_one_and_delete({'_id':id})