from django.shortcuts import render
from accounts.models import Client, Pharmacist, CustomUser
from .models import Chatroom
from .serializers import ChatroomSerializer
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class RequestChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        client = Client.objects.get(user=request.user)
        client_coin = Client.objects.get(client=client)

        if client_coin.coin > 0:
            # Deduct 1 token from the client's wallet
            client_coin.coin -= 1
            client_coin.save()

            # Create a new Chatroom instance
            chatroom = Chatroom.objects.create(client=client)

            # Generate the WebSocket URL using the chatroom ID
            websocket_url = reverse('chat:chatroom', args=[chatroom.id])

            serializer = ChatroomSerializer(chatroom)
            return Response({
                'chatroom': serializer.data,
                'websocket_url': request.build_absolute_uri(websocket_url)
            })
        else:
            return Response({"error": "Insufficient tokens in the wallet."}, status=400)
        

class ViewChatRequests(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pharmacist = Pharmacist.objects.get(user=request.user, is_live=True)
        chat_requests = Chatroom.objects.filter(is_active=True, pharmacist=None)

        serializer = ChatroomSerializer(chat_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        pharmacist = Pharmacist.objects.get(user=request.user, is_live=True)
        chatroom_id = request.data.get('chatroom_id')

        chatroom = Chatroom.objects.get(id=chatroom_id)

        # Add pharmacist to room with no pharmacy
        if chatroom.is_active and chatroom.pharmacist is None:
            chatroom.pharmacist = pharmacist
            chatroom.save()

        elif chatroom.is_active and chatroom.pharmacist == pharmacist:
            # End the chat and close the chatroom
            chatroom.close_chat()

            # Reward the pharmacist with 500 naira in the wallet
            pharmacist.balance += 500
            pharmacist.save()

            # Return success response indicating the pharmacist has joined the chatroom
            return Response({"success": "You have joined the chatroom."})
        else:
            # Return error response indicating the chatroom is no longer available
            return Response({"error": "Chatroom is no longer available."}, status=400)

