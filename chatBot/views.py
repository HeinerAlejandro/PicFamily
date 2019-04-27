from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from .bot.ChatBot import ChatBot
from .models import Message

# Create your views here.

class ResponseBotView(APIView):

    def post(self, *args, **kwargs):

        bot = ChatBot(nombre = 'Godmos')
        
        message = self.request.data.get('message', None)
        
        if message:
            response = bot.habla(message)

            if response:
                data = Message(message = response)
                serializer = MessageSerializer(data)

                return Response(serializer.data, status = status.HTTP_200_OK)

        response = "¿No te entiendo, ¿puedes formular mejor tu pregunta?"

        data = Message(message = response)

        serializer = MessageSerializer(data)

        return Response(serializer.data, status = status.HTTP_200_OK)