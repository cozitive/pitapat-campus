from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import (FileUploadParser, JSONParser,
                                    MultiPartParser)
from rest_framework.response import Response

from .models import University, User
from .serializers import (UniversityListReadSerializer, UserCreateSerializer,
                          UserListReadSerializer)


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, JSONParser, FileUploadParser])
def user_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserListReadSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=201)
        return Response(serializer.errors, status=400)

    return Response({"error": "HTTP method not allowed"}, status=405)


@api_view(['GET'])
@parser_classes([MultiPartParser, JSONParser, FileUploadParser])
def university_view(request):
    if request.method == 'GET':
        universities = University.objects.all()
        serializer = UniversityListReadSerializer(universities, many=True)
        return Response(serializer.data)

    return Response({"error": "HTTP method not allowed"}, status=405)
