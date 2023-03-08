from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from datetime import datetime

# def pathview(request, name, id):
#     return HttpResponse("Name: {} UserID: {}".format(name,id))

# def qryview(request):
#     name = request.GET['name']
#     id = request.GET['id']
#     return HttpResponse("Name: {}, UserID: {}".format(name,id))

def menuitems(request, dish):
    items = {
        'pasta': 'pasta is a type of food made from colombia.',
        'falafel': "falafels are deep fried ",
        'cheesecake': "cheescke is a type of desert made"
    } 
    description = items[dish] 
    return HttpResponse(f"<h2> {dish} </h>" + description)
    
# 
# def home(request):
#     path = request.path 
#     scheme = request.scheme
#     method = request.method
#     address = request.META["REMOTE_ADDR"]
#     user_agent = request.META["HTTP_USER_AGENT"]
#     path_info = request.path_info

#     response = HttpResponse()
#     response.headers['Age'] = 20

#     msg = f"""<br>
#     <br>Path: {path}
#     <br>Scheme: {scheme}
#     <br>Method: {method}
#     <br>Address: {address}
#     <br>User agent: {user_agent}
#     <br>Path Info: {path_info}
#     <br>Response Header: {response.headers}
    
#     <br>u
#     """
#     return HttpResponse(msg, content_type='text/html',charset='utf-8')

# def myView(request):
#     if request.method == "GET":
#         val = request.GET['Key']
#         # perform read or delete orperations on the model

#     if request.method == "POST":
#         val = request.POST['key']
#         # perform insert or update operations on the model

# # VIEW RENDERING TEMPLATE
#         # function base view
# def myview(request):
#     if request.method == "GET":
#         # PERFORM READ OR DELETE OEPRATION ON MODEL
#         pass

#     if request.method == "POST": 
#         # PERFORM INSERT OR UPDATE OPERATIONS ON MODEL 
#         context = { } # dictionary containing data tob be send to the client

#     return render(request,'mytmplate.html', context ) 

# #CLASS BASED VIEWS
# from django.views import View 
# class MyView(View):
#     def get(self, request):
#         # logic to process GET request 
#         return HttpResponse('response to to GET request') 
    
#     def post(self, requst):
#         # logic to process POST request 
#         return HttpResponse("respone to POST requst")
