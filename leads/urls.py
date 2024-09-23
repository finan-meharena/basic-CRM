from django.urls import path
import leads.views as lead_views

app_name = "leads"

urlpatterns = [
    path("", lead_views.LeadListView.as_view(), name='lead-list'),
    path("create/", lead_views.LeadCreateView.as_view(), name='lead-create'),
    path("<pk>/", lead_views.LeadDetailView.as_view(), name='lead-detail'),
    path("<pk>/update/", lead_views.LeadUpdateView.as_view(), name='lead-update'),
    path("<pk>/delete/", lead_views.LeadDeleteView.as_view(), name='lead-delete'),
]
