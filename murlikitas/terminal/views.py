from django.shortcuts import render, HttpResponse, redirect
import json


def index(request):
    return render(request, 'terminal/index.html')


def command(request):
    response_data = {'output': request.POST['input']}
    return HttpResponse(json.dumps(response_data), content_type="application/json")



from terminal.forms import MailForm
from django.core.mail import send_mail
import gdata.data

#Obtained from Google Project Settings
CLIENT_ID  = "1053514243290-qc6m642dtv6dbqdi8k9fttfaapbcqo4d.apps.googleusercontent.com"
CLIENT_SECRET  = "L5VvFtSOdZcAwVfU_7ckxwRX"

#Variable that specifies the data you want to access
GOOGLE_SCOPE = "https://www.google.com/m8/feeds"

#URL where the flow should go on successful authentication
#GOOGLE_APPLICATION_REDIRECT_URI = "localhost:8000/"

USER_AGENT  = ""

def contacts(request):
    if request.POST:
        form = MailForm(request.POST)
        if form.is_valid():
            auth_user = request.POST['auth_user']
            auth_password = request.POST['auth_password']
            mail_subject = request.POST['mail_subject']
            mail_message = request.POST['mail_message']
            mail_from = request.POST['mail_from']
            mail_to = request.POST['mail_to']
            send_mail(mail_subject,
                      mail_message,
                      mail_from,
                      [mail_to],
                      fail_silently=False,
                      auth_user=auth_user,
                      auth_password=auth_password,
                      )

            return HttpResponse("Correo enviado")
        else:
            return render(request, 'main/index.html', {'form': form})

    else:
        # Save the token for later use.
        token = gdata.gauth.OAuth2Token(client_id=CLIENT_ID,
                                        client_secret=CLIENT_SECRET,
                                        scope=GOOGLE_SCOPE,
                                        user_agent=USER_AGENT)

        # The redirect_url parameter needs to match the one you entered in the API Console and points
        # to your callback handler.
        return redirect(token.generate_authorize_url(redirect_url='https://localhost/'))
        #form = MailForm()

        #return render(request, 'main/index.html', {'form': form})