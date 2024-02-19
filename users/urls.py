from django.urls import path
from .views import AllConversations, AllMessages, UserConversations, MessagesByConversationId

urlpatterns = [
    path('conversations/', AllConversations.as_view(), name='all_conversations'),
    path('messages/', AllMessages.as_view(), name='all_messages'),
    path('user_conversations/', UserConversations.as_view(), name='user_conversations'),
    path('messages_by_conversation/<int:conversation_id>/', MessagesByConversationId.as_view(), name='messages_by_conversation'),
]
