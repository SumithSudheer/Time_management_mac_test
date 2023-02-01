from django.db import models
import pymongo
from .serializers import User_serializer
from bson import json_util
from datetime import datetime
from .auth import AuthHandlerIns

# Create your models here.
# from utils import get_db_handle
from pymongo import MongoClient


connection_string='mongodb+srv://admin:admin@cluster0.bn80fcq.mongodb.net/test'
db_name='mac-test'
client = pymongo.MongoClient(connection_string)
db = client[db_name]
super = db['super']
branch = db['branch']
batch = db['batch']
course = db['course']
subject = db['subject']
topic = db['topic']
subtopic= db['subtopic']






class User:

    def create_user(self,username,password):
        now = datetime.now()
        p = AuthHandlerIns.get_password_hash(password=password)
        print(p)
        k=super.insert_one({'_id':str(now),'username':username,'password':p})
        print(k)
        print('lllllllll')

    def get_user(self,username=None):
        if not username:
            k=[json_util.loads(json_util.dumps(i)) for i in super.find() ]
            # k=list(super.find())
            print(k)
        else:
            k= super.find_one({'username':username})

        return k

    
class Branch_cl:

    def create_branch(self, name, place):
        now = datetime.now()
        k=branch.insert_one({'_id':str(now),'name':name,'place':place})

    def get_branch(self,id=None):
        if id:
           return branch.find_one({'_id':id}) 
        return list(branch.find())

    def add_course(self, id,course_id):
        b=course.find_one({'_id':course_id})
        branch.find_one_and_update({'_id':id},{"$push":{"course":b}},upsert=True)


class Batch_cl:
    def create_batch(self, name, branch):
        now = datetime.now()

        b=Branch_cl.get_branch(self,id=branch)
        batch.insert_one({"_id":str(now),'name':name,'branch':b})



class Course_cl:
    def create_course(self, name):
        now = datetime.now()
        c= course.insert_one({'_id':str(now),'name':name})
        print(c)

    def add_subject(self, id, subject_id):
        s=subject.find_one({'_id':subject_id})
        course.find_one_and_update({'_id':id},{"$push":{"subject":s}},upsert=True)



class Subject_cl:
    def create_subject(self, name):
        now = datetime.now()
        s = subject.insert_one({'_id':str(now),'name':name})

    def add_topic(self, id, topic_id):
        t=topic.find_one({'_id':topic_id})
        subject.find_one_and_update({'_id':id},{"$push":{'topic':t}},upsert=True)


class Topic_cl:
    def create_topic(self, name):
        now = datetime.now()
        t= topic.insert_one({'_id':str(now),'name':name})

    def add_subtopic(self, id, sub_id):
        s= subtopic.find_one({'_id':sub_id})
        topic.find_one_and_update({'_id':id},{"$push":{"subtopic":s}})




class Subtopic_cl:
    def create_topic(self, name):
        now = datetime.now()
        t= subtopic.insert_one({'_id':str(now),'name':name})










    


   


