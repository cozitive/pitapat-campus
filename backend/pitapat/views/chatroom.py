from rest_framework import viewsets
from rest_framework.response import Response

from pitapat.models import User, UserChatroom
from pitapat.serializers import UserListSerializer


class ChatroomParticipantViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        id = kwargs['chatroom_id']
        user_chatrooms = UserChatroom.objects.filter(chatroom__id=id)
        users = [user_chatroom.user for user_chatroom in user_chatrooms]
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
