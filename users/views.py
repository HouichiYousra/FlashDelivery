from rest_auth.registration.views import RegisterView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from .serializers import *
from .models import *
from .policy import *

class UserViewset(viewsets.ModelViewSet):
    permission_classes = (UserPolicy,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filterset_fields = ['user_type', ]


class FournisseurViewset(viewsets.ModelViewSet):
    permission_classes = (FournisseurPolicy,)
    serializer_class = FournisseurSerializer
    queryset = Fournisseur.objects.all()

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if ((not request.user.is_authenticated) and (int(request.data['user_type']) == 2)) or \
                request.user.user_type == 3 or request.user.user_type == 4:
            user = self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(self.get_response_data(user),
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        elif request.user.user_type == 3 or request.user.user_type == 4:
            user = self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(self.get_response_data(user),
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter