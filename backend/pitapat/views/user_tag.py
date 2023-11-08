from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from pitapat.models import Tag, User, UserTag
from pitapat.serializers import UserTagCreateSerializer


class UserTagViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', 'delete']
    queryset = Tag.objects.all()

    def get_serializer_class(self):
        if self.action in ('create', 'delete'):
            return UserTagCreateSerializer
        return None

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
        tags = request.data['tags']
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            UserTag.objects.create(user=user, tag=tag)
        return Response(status=201)

    @swagger_auto_schema(request_body=UserTagCreateSerializer)
    def destroy(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
#         tag_ids = request.data['tags']
#         for tag_id in tag_ids:
#             user_tag = UserTag.objects.get(user=user, tag=tag_id)
#             user_tag.delete()
        user_tags = UserTag.objects.filter(user=user)
        for user_tag in user_tags:
            user_tag.delete()
        return Response(status=204)
