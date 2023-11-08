from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from pitapat.models import Block, User
# from pitapat.paginations import UserListPagination
from pitapat.serializers import UserListSerializer
# from pitapat.utils.page import paginate


class BlockFromUserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Block.objects.all()
    serializer_class = UserListSerializer
    # pagination_class = UserListPagination

    def list(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(), id=kwargs['user_id'])
        blocks = Block.objects.filter(is_from=user, to__isnull=False)
        receiver_ids = [block.to.id for block in blocks]
        blocked_users = User.objects.filter(id__in=receiver_ids).order_by('-reg_dt')
        return Response(self.get_serializer(blocked_users, many=True).data)
