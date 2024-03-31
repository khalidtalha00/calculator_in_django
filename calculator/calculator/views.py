from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def calculator(request):

    return render(request, 'calculator.html')

def calculate(request):
    num1 = eval(request.GET.get('number1', 'error'))
    num2 = eval(request.GET.get('number2', 'error'))
    operator= request.GET.get('operator','error')
    result=''

    try:

        if operator=='+':
            result=num1+num2
        elif operator=='-':
            result=num1-num2
        elif operator=='*':
            result=num1*num2
        elif operator=='/':
            result=num1/num2


    except :
        print("Invalid Syntax")

    params={'one':num1,'two':num2,'resultant':result,'operation':operator}
    return render(request,'calculate.html',params)