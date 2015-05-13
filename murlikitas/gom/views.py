from django.shortcuts import render, HttpResponse
import json
import pysftp
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        try:
            hostname = '0.0.0.0'  # 82.130.238.211'
            username = 'pi'
            password = 'fuze'

            with pysftp.Connection(hostname, username=username, password=password) as sftp:
                sftp.execute('sudo python servo2.py')
            response_data = {'success': True}
        except pysftp.SSHException:
            response_data = {'success': False}

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        return render(request, 'gom/index.html')


def send_mail_to_admin(request):
    if request.method == 'POST':
        auth_user = request.POST['auth_user']
        auth_password = request.POST['auth_password']
        send_mail("ERROR GOM",
                  "EL GOM NO FUNCIONA",
                  "DESCONOCIDO",
                  "jonan.bsg@gmail.com",
                  fail_silently=False,
                  auth_user=auth_user,
                  auth_password=auth_password,
                  )
        return HttpResponse("<h1>ADMINISTRADOR CONTACTADO</h1>")