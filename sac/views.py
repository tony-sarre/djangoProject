from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from sac.models import Alert, AlertList
from sac.serializers import AlertSerializer, AlertListSerializer, AlertListDetailSerializer


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect("home")
        else:
            messages.info(request, "username or password is incorrect")

    context = {}
    return render(request, "login.html", context)


def logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home(request):
    list_alert = Alert.objects.all()
    context = {"liste_alert": list_alert}
    return render(request, "index.html", context)


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['due_date', 'Resolue', 'Encours']
    search_fields = ['title']

    @swagger_auto_schema(operation_description="This method returns a list of Todos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AlertListViewSet(viewsets.ModelViewSet):
    queryset = AlertList.objects.all()
    serializer_class = AlertListSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AlertListDetailSerializer
        return AlertListSerializer
