from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def deposit(request):
    output='''<HTML>
    <BODY bgcolor=cyan>
    <H2>This is Deposit View </H2>
    </BODY>
    </HTML>'''
    response=HttpResponse(output)
    return response 

def withdraw(request):
    output='''<HTML>
    <BODY bgcolor=yellow>
    <H2>This is Withdraw View </H2>
    </BODY>
    </HTML>'''
    response=HttpResponse(output)
    return response

def home(request):
    output='''<HTML>
    <BODY bgcolor=pink>
    <a href=http://127.0.0.1:8000/deposit>Deposit</a><br>
    <a href=http://127.0.0.1:8000/withdraw>Withdraw</a><br>
    </BODY>
    </HTML>'''
    response=HttpResponse(output)
    return response