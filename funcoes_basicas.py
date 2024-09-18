import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from django.shortcuts import render,redirect
from PIL import Image
from pontos_app.models import *
import io
import pandas as pd
from django.core.files.uploadedfile import InMemoryUploadedFile

def enviar_email(subject,body,recipients):
        html_message = MIMEText(body, 'html')
        html_message['Subject'] = subject
        html_message['From'] = settings.EMAIL_HOST_USER
        html_message['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD_APP)
            server.sendmail(settings.EMAIL_HOST_USER, recipients, html_message.as_string())   
            
            

def is_filho(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            usuario = request.session.get('usuario')
        except:
            usuario=False
        if usuario:
            user= Pessoa.objects.get(id=usuario)
            if (user):
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        else:
            return redirect('login')  # Redireciona para uma página de login ou qualquer outra página apropriada
    return wrapper
def is_responsavel(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            usuario = request.session.get('usuario')
        except:
            usuario=False
        if usuario:
            user= Pessoa.objects.get(id=usuario)
            if (user.responsavel==True):
                return view_func(request, *args, **kwargs)
            else: 
                return redirect("/?status=99")
        else:
            return redirect("/?status=99")  # Redireciona para uma página de login ou qualquer outra página apropriada
    return wrapper
           
