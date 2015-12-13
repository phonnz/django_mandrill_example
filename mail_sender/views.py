from django.http import HttpResponse

from django.core.mail import EmailMessage

def send_mail(request):

    msg = EmailMessage(subject='hola', from_email='Phonnz <phonnz@effio.co', to = ['gonzalezm.alfonso@gmail.com',])
    msg.template_name = 'dynamic_test'
    msg.template_content = {
        'user_namer':'<h2>Hola Alfonso</h2>'
    }

    msg.send()

    return HttpResponse('Mail sended')
