from django.shortcuts import render,redirect

# Create your views here.
def vazio(request):
    return redirect('/login/') 
def login(request):
    # cria a view do login do usuário
    status=str(request.GET.get('status'))
    return render(request, "login.html", {'status':status})