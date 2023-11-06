"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from tictactoe.consumers import *

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application


django_asgi_app = get_asgi_application()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_asgi_application()
application=ProtocolTypeRouter({
    #'https': get_asgi_application(),
    "http": django_asgi_app,
    'websocket': URLRouter([
        path('ws/tictactoe/<int:id>/',GameConsumer.as_asgi())
    ])
})

