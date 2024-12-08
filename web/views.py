from django.shortcuts import render
from django.http import JsonResponse 
from json import JSONEncoder
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from web.models import Token , User , Expense , Income
from datetime import datetime


@csrf_exempt
def submit_income(request):
    # user submit request an expense

    this_token= request.POST['token'] 

    this_user= User.objects.filter(token__token = this_token).get()
    if  'date' not in request.POST:
        date= datetime.now()
    Income.objects.create(user= this_user,text=request.POST['text'],
                           amount=request.POST['amount'],date=date)
    
    
    
    print(request.POST )

    return JsonResponse({
        'status': 'OK' } , encoder= JSONEncoder )




@csrf_exempt
def submit_expense(request):
    # user submit request an expense

    this_token= request.POST['token'] 

    this_user= User.objects.filter(token__token = this_token).get()
    if  'date' not in request.POST:
        date= datetime.now()
    Expense.objects.create(user= this_user,text=request.POST['text'],
                           amount=request.POST['amount'],date=date)
    
    
    
    print(request.POST )

    return JsonResponse({
        'status': 'OK' } , encoder= JSONEncoder )