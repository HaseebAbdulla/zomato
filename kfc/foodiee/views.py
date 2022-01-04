from django.shortcuts import render

# Create your views here.

def Cofee(request):
    return render(request, 'cofee.html')
    
