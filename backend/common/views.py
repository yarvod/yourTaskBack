from rest_framework.response import Response
from rest_framework.views import APIView

from common.serializers import CheckEmailSerializer
from users.models import User


class CheckEmailView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = CheckEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.validated_data.get('email')).first()
        return Response(data={'exists': bool(user)}, status=200)
