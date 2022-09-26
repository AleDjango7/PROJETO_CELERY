import os
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from hashlib import sha256


myFont = ImageFont.truetype('/home/ale/Documents/Mistral.ttf', 30)

@shared_task
def cria_convite(nome, email):
    template = os.path.join(settings.STATIC_ROOT, 'img/invite.png')
    img = Image.open(template)
    img_gravar = ImageDraw.Draw(img)
    img_gravar.text((376, 623), f'{nome}\n Bem Vindo! ', font=myFont, fill=(0, 0, 0))
    secret_key = '7c^y@kamrt7v4hq3a6oy$7+rrk5z_78mw6wl4xv-qogs!8gpjv'
    token = sha256((email + secret_key).encode()).hexdigest()
    path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
    img.save(path_salvar)
    send_mail('Cadastro confirmado', f'Cadastro confirmado com sucesso \n Link para seu cadastro http://127.0.0.1:8000/media/convites/{token}.png', 'alexandre@webfrio.com.br', recipient_list=[email])
    return None