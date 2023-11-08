from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from pitapat.models import Pitapat, User, UserChatroom
# from pitapat.paginations import UserListPagination
from pitapat.serializers import UserListSerializer
# from pitapat.utils.page import paginate


class PitapatToUserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Pitapat.objects.all()
    serializer_class = UserListSerializer
    # pagination_class = UserListPagination

    def list(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(), id=kwargs['user_id'])
        pitapats = Pitapat.objects.filter(to=user, is_from__isnull=False)
        user_chatrooms = UserChatroom.objects.filter(user=user)
        chatroom_participants = []
        for user_chatroom in user_chatrooms:
            try:
                chatroom_participant = UserChatroom.objects.get(
                    Q(chatroom=user_chatroom.chatroom) & ~Q(user=user_chatroom.user)).user
                chatroom_participants.append(chatroom_participant)
            except:
                pass
        for chatroom_participant in chatroom_participants:
            pitapats=pitapats.exclude(is_from=chatroom_participant)
        sender_ids = [pitapat.is_from.id for pitapat in pitapats]
        sender_users = User.objects.filter(id__in=sender_ids).order_by('-reg_dt')
        return Response(self.get_serializer(sender_users, many=True).data)

class PitapatFromUserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Pitapat.objects.all()
    serializer_class = UserListSerializer
    # pagination_class = UserListPagination

    def list(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(), id=kwargs['user_id'])
        pitapats = Pitapat.objects.filter(is_from=user, to__isnull=False)
        user_chatrooms = UserChatroom.objects.filter(user=user)
        chatroom_participants = []
        for user_chatroom in user_chatrooms:
            try:
                chatroom_participant = UserChatroom.objects.get(
                    Q(chatroom=user_chatroom.chatroom) & ~Q(user=user_chatroom.user)).user
                chatroom_participants.append(chatroom_participant)
            except:
                pass
        for chatroom_participant in chatroom_participants:
            pitapats=pitapats.exclude(to=chatroom_participant)
        receiver_ids = [pitapat.to.id for pitapat in pitapats]
        receiver_users = User.objects.filter(id__in=receiver_ids).order_by('-reg_dt')
        return Response(self.get_serializer(receiver_users, many=True).data)
