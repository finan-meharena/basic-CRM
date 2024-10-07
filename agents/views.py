from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = 'agents'

    def get_queryset(self) -> QuerySet[Any]:
        organization = self.request.user.userprofile
        
        return Agent.objects.filter(organization=organization)

class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name  = "agents/agent_detail.html"
    context_object_name = 'agent'
    model = Agent
    
    def get_queryset(self) -> QuerySet[Any]:
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agents-list")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    
class AgentUpdateViews(LoginRequiredMixin, generic.UpdateView):
    form_class = AgentModelForm
    queryset = Agent.objects.all()
    template_name = "agents/agent_update.html"
    context_object_name = 'agent'
    
    def get_success_url(self) -> str:
        return reverse("agents:agents-list")

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Agent
    template_name = "agents/agent_delete.html"
    
    def get_success_url(self):
        return reverse("agents:agents-list")
    
    def get_queryset(self) -> QuerySet[Any]:
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    