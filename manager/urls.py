from django.urls import path
from manager import views as ManagerViews

app_name = "manager"

urlpatterns = [
    path("", ManagerViews.HomeView.as_view(), name="home")
]