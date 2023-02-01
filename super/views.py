from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .auth import AuthHandlerIns , is_super_admin


from .models import User, Branch_cl, Batch_cl, Course_cl, Subject_cl, Topic_cl, Subtopic_cl, batch, branch, course, subject, topic, subtopic
from faculty.models import User as Faculty_user
import jwt, datetime
# Create your views here.

class Super_admin(APIView):
    def post(self, request):
        print('hi')
        User.create_user(self,username=request.data['username'],password=request.data['password'])
        return Response({"message":"done"})
    
    def get(self, request):
        print('hello')
        u=User.get_user(self)
        return Response({"message":"done","u":u})


@api_view(['POST'])
def login(request):
    u=User.get_user(request,username=request.data['username'])
    if u:
        k=AuthHandlerIns.verify_password(plain_password=request.data['password'],hashed_password= u['password'])
        if k:
            payload={
                'id':'',
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow(),
                'super':True,
                'faculty':False,
            }
            token = AuthHandlerIns.get_token(payload)
            return Response({"token":token})

    
    return Response({"message":"Nope"})



class Branch(APIView):
    def post(self,request):
        if is_super_admin(request):
            b=Branch_cl.create_branch(request,name=request.data['name'],place=request.data['place'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})

    def get(self, request):
        b=Branch_cl.get_branch(request)
        return Response({"mess":b})

    def put(self, request):
        if is_super_admin(request):
            c=Branch_cl.add_course(request,id=request.data['branch_id'],course_id=request.data['course_id'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})



class Fac_c(APIView):
    def post(self, request):
        if is_super_admin(request):
            Faculty_user.create_user(username=request.data['username'],password=request.data['password'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})

class Asign_branch_man(APIView):
    def post(self, request, id):
        print(id)
        k=Branch_cl.get_branch(request,id=id)
        print(k)
        if is_super_admin(request):
            Faculty_user.update_perms(request,username=request.data['username'],branch_manager=True,branch_name=k['name'],branch_place=k['place'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})


class Batch(APIView):
    def post(self, request):
        if is_super_admin(request):
            Batch_cl.create_batch(request, name=request.data['name'],branch=request.data['id'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})
    def get(self, request):
        if is_super_admin(request):
            
            return Response({"mess":list(batch.find({}))})
        else:
            return Response({"mess":"no"})
        


class Course(APIView):
    def get(self, request):
        if is_super_admin(request):
            
            return Response({"mess":list(course.find({}))})
        else:
            return Response({"mess":"no"})


    def post(self, request):
        if is_super_admin(request):
            Course_cl.create_course(request,name=request.data['name'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})

    def put(self, request):
        if is_super_admin(request):
            Course_cl.add_subject(request,id=request.data['course_id'],subject_id=request.data['subject_id'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})


class Subject(APIView):
    def get(self, request):
        if is_super_admin(request):
            
            return Response({"mess":list(subject.find({}))})
        else:
            return Response({"mess":"no"})
    def post(self, request):
        if is_super_admin(request):
            Subject_cl.create_subject(request,name=request.data['name'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})

    def put(self, request):
        if is_super_admin(request):
            Subject_cl.add_topic(request,id=request.data['subject_id'],topic_id=request.data['topic_id'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})





class Topic(APIView):
    def get(self, request):
        if is_super_admin(request):
            
            return Response({"mess":list(topic.find({}))})
        else:
            return Response({"mess":"no"})
    def post(self, request):
        if is_super_admin(request):
            Topic_cl.create_topic(request,name=request.data['name'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})
    
    def put(self, request):
        if is_super_admin(request):
            Topic_cl.add_subtopic(request,id=request.data['topic_id'],sub_id=request.data['subtopic_id'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"})



class Subtopic(APIView):
    def get(self, request):
        if is_super_admin(request):
            
            return Response({"mess":list(subtopic.find({}))})
        else:
            return Response({"mess":"no"})
    def post(self, request):
        if is_super_admin(request):
            Subtopic_cl.create_topic(request,name=request.data['name'])
            return Response({"mess":"yes"})
        else:
            return Response({"mess":"no"}) 

@api_view(['PUT'])
def faculty_verify(request,id):
    if is_super_admin(request):
        Faculty_user.verify(request, id)
        return Response({"mess":"yes"})
    else:
        return Response({"mess":"no"}) 

@api_view(['DELETE'])
def faculty_reject(request,id):
    if is_super_admin(request):
        Faculty_user.delete(request, id)
        return Response({"mess":"yes"})
    else:
        return Response({"mess":"no"}) 


@api_view(['GET'])
def faculty(request):
    if is_super_admin(request):
        k=Faculty_user.get_user(request)
        return Response({"mess":k})
    else:
        return Response({"mess":"no"}) 

@api_view(['POST'])
def add_fac(request):
    if is_super_admin(request):
        k=Faculty_user.create_user(request,username=request.data['username'],password=request.data['password'])
        return Response({"mess":"Yes"})
    else:
        return Response({"mess":"no"}) 




            


        
    




        




