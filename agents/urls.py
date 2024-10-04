from django.urls import path
from agents.views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateViews

app_name = 'agents'

urlpatterns = [
    path("", AgentListView.as_view(), name="agents-list"),
    path("agent-create/",AgentCreateView.as_view(), name="agent-create"),
    path("<int:pk>/",AgentDetailView.as_view(), name="agent-detail"),
    path("<int:pk>/update/",AgentUpdateViews.as_view(), name="agent-update"),
]
