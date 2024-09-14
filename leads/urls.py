from django.urls import path
from .views import lead_detail, lead_list

app_name = "leads"

urlpatterns = [
    path("", lead_list),
    path("<pk>/", lead_detail)
]
