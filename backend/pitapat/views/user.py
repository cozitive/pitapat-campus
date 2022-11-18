from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from pitapat.models import Introduction, Photo, User, UserTag
from pitapat.serializers import UserListSerializer, UserListQuerySerializer, UserCreateSerializer, UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        if self.action == 'create':
            return UserCreateSerializer

    @swagger_auto_schema(query_serializer=UserListQuerySerializer)
    def list(self, request, *args, **kwargs):
        gender = request.GET.get('gender')
        # age_min = request.GET.get('age_min')
        # age_max = request.GET.get('age_max')
        colleges_included = [int(c) for c in request.GET.getlist('colleges_included')]
        colleges_excluded = [int(c) for c in request.GET.getlist('colleges_excluded')]
        majors_included = [int(m) for m in request.GET.getlist('majors_included')]
        majors_excluded = [int(m) for m in request.GET.getlist('majors_excluded')]
        # tags_included = [int(t) for t in request.GET.getlist('tags_included')]
        # tags_excluded = [int(t) for t in request.GET.getlist('tags_excluded')]

        filters = Q()
        if gender:
            filters &= Q(gender=gender)
        if colleges_included:
            filters &= Q(college__in=colleges_included)
        if majors_included:
            filters &= Q(major__in=majors_included)
        # if tags_included:
        #     filters &= Q(tags__in=tags_included)
        if colleges_excluded:
            filters &= ~Q(college__in=colleges_excluded)
        if majors_excluded:
            filters &= ~Q(major__in=majors_excluded)
        # if tags_excluded:
        #     filters &= ~Q(tags__in=tags_excluded)
        users = User.objects.filter(filters).distinct()

        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'delete']
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'key'

    def destroy(self, request, *args, **kwargs):
        key = kwargs['key']
        Introduction.objects.get(user=key).delete()
        for user_tag in UserTag.objects.filter(user=key):
            user_tag.delete()
        for photo in Photo.objects.filter(user=key):
            photo.delete()
        User.objects.get(key=key).delete()
        return Response(status=204)
