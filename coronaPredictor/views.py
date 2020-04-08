from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from random import randrange

# Create your views here.

def home(Request):
    return render(Request, 'index.html')

def home_submit(Request):
    pac = paciente()
    try:
        pac.nome = Request.POST.get("nome")
        pac.cpf = Request.POST.get("cpf")
        pac.sexo = Request.POST.get("sexo")
        try:
            pac.idade = int(Request.POST.get("idade"))
        except:
            messages.error(Request, "Idade Inválida")
            return redirect("/")
        doenca = Request.POST.get("doenca")
        if doenca == "Sim":
            pac.doenca = True
            pac.qlDoenca = Request.POST.get("qlDoenca")
        else:
            pac.doenca = False
            pac.qlDoenca = None
        pac.observacao = Request.POST.get("observacao")
        pac.save()
        response = redirect('/fotoUp/')
        response.set_cookie('cpf', Request.POST.get("cpf"))
        return response
    except:
        messages.error(Request, "Não foi possível cadastrar o paciente!")
        return redirect("/")

def fotoUp(request):
    try:
        cpf = request.COOKIES['cpf']
        paciente.objects.get(cpf = cpf)
        return render(request, "foto.html")
    except:
        messages.error(request,"Cadastre o paciente primeiro!")
        return redirect("/")

def fotoUp_submit(request):
    try:
        cpf = request.COOKIES['cpf']
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            file_extension = myfile.name.split(".")
            filename = fs.save(cpf + "." + file_extension[-1], myfile)
            # messages.success(request,"Arquivo enviado com sucesso! ")
            response = redirect("/resultado/")
            response.set_cookie("foto_url",fs.url(filename))
            return response
        else:
            messages.error(request, "Tente novamente!")
            return redirect("/fotoUp/")
    except:
        messages.error(request, "Arquivo ausente")
        return redirect("/fotoUp/")

def resultado(request):
    try:
        photoUrl = request.COOKIES['foto_url']
        cpf = request.COOKIES['cpf']
        pac = paciente.objects.get(cpf = cpf)
        color_prob = ["rgb(0, 255, 0)","rgb(25, 225, 0)","rgb(50, 200, 0)","rgb(75, 175, 0)","rgb(100, 150, 0)","rgb(125, 125, 0)","rgb(150, 100, 0)","rgb(175, 75, 0)","rgb(200, 25, 0)","rgb(255, 0, 0)"]
        prob =  randrange(101) #teste
        num =  int(prob/10)
        if num == 10:
            num = 9
        color = color_prob[num]
        if pac.doenca:
            doenca = "Sim"
            qlDoenca = pac.nome_doenca
        else:
            doenca = "Não"
            qlDoenca = ""
        if len(pac.observacao) == 0:
            obs = "Nenhuma."
        else:
            obs = pac.observacao
        response = render(request, "resultado.html", {"probabilidade":prob,"color":color, "cpf":cpf, "nome":pac.nome, "sexo":pac.sexo, "idade":pac.idade, "observacao":obs, "doenca":doenca, "qlDoenca":qlDoenca})
        response.set_cookie('cpf', "")
        response.set_cookie('foto_url', "")
        return response
    except:
        messages.error(request,"Cadastre o paciente primeiro!")
        return redirect("/")
