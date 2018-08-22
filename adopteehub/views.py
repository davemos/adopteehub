from django.shortcuts import render

def home(request):
    return render(request,'adopteehub/home.html')
    
def about(request):
    return render(request,'adopteehub/about.html')
    
def board(request):
    return render(request,'adopteehub/board.html')
    
def services(request):
    return render(request,'adopteehub/services.html')
    
def getinvolved(request):
    return render(request,'adopteehub/getinvolved.html')

def letter(request):
    return render(request, 'adopteehub/letter.html')
