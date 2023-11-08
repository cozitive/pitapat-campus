from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from pitapat.models import Block, User, Chatroom, UserChatroom, Pitapat
from pitapat.serializers import BlockSerializer


class BlockViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', 'delete']
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def create(self, request, *args, **kwargs):
        from_id = request.data.get('from')
        to_id = request.data.get('to')
        if not from_id or not to_id:
            return Response(status=400)

        from_user = get_object_or_404(User.objects.all(), id=from_id)
        to_user = get_object_or_404(User.objects.all(), id=to_id)

        if Block.objects.filter(is_from=from_user, to=to_user): # duplicated request
            return Response(status=409)

        from_user_chatrooms = UserChatroom.objects.filter(user=from_user).values('chatroom')
        to_user_chatrooms = UserChatroom.objects.filter(user=to_user).values('chatroom')
        chatroom_ids = [id['chatroom'] for id in from_user_chatrooms if id in to_user_chatrooms]
        for id in chatroom_ids:
            chatroom = Chatroom.objects.get(id=id)
            if chatroom.user_count == 2:  # 1:1 chatroom
                chatroom.delete()

        try:
            reverse_pitapat = Pitapat.objects.get(is_from=from_user, to=to_user)
            reverse_pitapat.delete()
        except Pitapat.DoesNotExist:
            pass

        try:
            pitapat = Pitapat.objects.get(is_from=to_user, to=from_user)
            pitapat.delete()
        except Pitapat.DoesNotExist:
            pass

        Block.objects.create(is_from=from_user, to=to_user)

        return Response(status=201)

    @swagger_auto_schema(request_body=BlockSerializer)
    def destroy(self, request, *args, **kwargs):
        from_id = request.data.get('from')
        to_id = request.data.get('to')
        if not from_id or not to_id:
            return Response(status=400)

        from_user = get_object_or_404(User.objects.all(), id=from_id)
        to_user = get_object_or_404(User.objects.all(), id=to_id)

        try:
            block = Block.objects.get(is_from=from_user, to=to_user)
        except Block.DoesNotExist:
            return Response(status=404)
        block.delete()

        return Response(status=204)
