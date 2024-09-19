from django.urls import path
from .views import lead_detail, lead_list, lead_create, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path("", lead_list, name='lead-list'),
    path("create/", lead_create, name='lead-create'),
    path("<pk>/", lead_detail, name='lead-detail'),
    path("<pk>/update/", lead_update, name='lead-update'),
    path("<pk>/delete/", lead_delete, name='lead-delete'),
]
