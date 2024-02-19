from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConversationSerializer, MessageSerializer
from .models import Conversation, Message
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated



class AllMessages(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Optionally, you might want to limit the messages returned or paginate them
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assuming you want to automatically set the message's user to the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AllConversations(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only return conversations for the logged-in user
        conversations = Conversation.objects.filter(user=request.user)
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['user'] = request.user.id
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserConversations(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        conversations = Conversation.objects.filter(user=request.user)
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)


class MessagesByConversationId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, conversation_id):
        if not Conversation.objects.filter(id=conversation_id, user=request.user).exists():
            return Response({"error": "Conversation not found or access denied"}, status=status.HTTP_404_NOT_FOUND)

        messages = Message.objects.filter(conversation_id=conversation_id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
