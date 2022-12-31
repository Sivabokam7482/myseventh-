from django.shortcuts import render

# Create your views here.
def siva(request):
    d={'name':'siva','age':'22'}
    return render(request,'hai.html',d)
    
