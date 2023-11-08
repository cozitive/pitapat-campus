from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from pitapat.models import Introduction, User
from pitapat.serializers import IntroductionSerializer


class UserIntroductionViewSet(viewsets.ModelViewSet):
    http_method_names = ['put']
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer

    @swagger_auto_schema(request_body=IntroductionSerializer)
    def update(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(), id=kwargs['user_id'])
        introduction = get_object_or_404(Introduction.objects.all(), user=user)
        content = request.data.get('content')
        if content is None:
            return Response(status=404)
        introduction.delete()
        introduction = Introduction.objects.create(user=user, content=content)
        serializer = IntroductionSerializer(introduction)
        return Response(serializer.data)
