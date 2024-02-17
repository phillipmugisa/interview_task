from django.urls import path
from manager import views as ManagerViews

from django.conf import settings
from django.conf.urls.static import static

app_name = "manager"

urlpatterns = [
    path("", ManagerViews.HomeView.as_view(), name="home")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)