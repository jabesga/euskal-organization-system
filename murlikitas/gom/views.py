from django.shortcuts import render
import pysftp


def index(request):
    if request.method == 'POST':
        hostname = '82.130.237.95'
        username = 'pi'
        password = 'fuze'

        with pysftp.Connection(hostname, username=username, password=password) as sftp:
            sftp.execute('sudo python servo2.py')
        return render(request, 'gom/index.html', {'status': 'active'})

    else:
        return render(request, 'gom/index.html', {'status': 'inactive'})