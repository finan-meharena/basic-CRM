from django.urls import path
from agents.views import AgentListView, AgentCreateView, AgentDetailView

app_name = 'agents'

urlpatterns = [
    path("", AgentListView.as_view(), name="agents-list"),
    path("<int:pk>/",AgentDetailView.as_view(), name="agent-detail"),
    path("agent-create/",AgentCreateView.as_view(), name="agent-create"),
]
