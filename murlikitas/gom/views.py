from django.shortcuts import render
import pysftp


def index(request):

    hostname = '82.130.237.95'
    username = 'pi'
    password = 'fuze'

    with pysftp.Connection(hostname, username=username, password=password) as sftp:
        sftp.execute('sudo python servo2.py')

    return render(request, 'gom/index.html')