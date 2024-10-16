from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from agents.mixins import OrganizerAndLoginRequiredMixing

# CRUD -> Create, Retrieve, Update , Delete + List

# Class Based Views

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

class LandingPageView(generic.TemplateView):
    template_name = "landing_page.html"

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
    
class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"
    
class LeadCreateView(OrganizerAndLoginRequiredMixing, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        # TODO send email 
        send_mail (
            subject = "A lead has been created",
            message = "Go to the site to see the new lead",
            from_email = "test@test.com",
            recipient_list = [ "test2@test.com"]
        )
        
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(OrganizerAndLoginRequiredMixing, generic.UpdateView):
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    template_name = "leads/lead_update.html"
    
    def get_success_url(self):
        return reverse("leads:lead-detail", kwargs={"pk": self.object.pk})

class LeadDeleteView(OrganizerAndLoginRequiredMixing, generic.DeleteView):
    model = Lead
    template_name = "leads/lead_delete.html"
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    


# # function baseed views
# def landing_page(request):
#     return render(request, "landing_page.html")

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }
#     return render(request, 'leads/lead_list.html', context)

# # def lead_detail(request,pk):
# #     lead = Lead.objects.get(id=pk)
# #     context = {
# #         "lead" : lead
# #     }
# #     return render(request, 'leads/lead_detail.html', context = context)

# def lead_create(request):
#     form = LeadModelForm()
#     print(request.POST)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form" : form,
#     }
#     return render(request, "leads/lead_create.html", context)

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead) # populates the form with lead values
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect(f"/leads/{pk}/")
#     context = {
#         "lead" : lead,
#         "form" : form
#     }
#     return render(request, "leads/lead_update.html", context)
# def lead_delete(request,pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")
    

    
# def lead_create(request):
#     form = LeadForm()
#     print(request.POST)
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent,
#             )
#             return redirect("/leads")
#     context = {
#         "form" : form,
#     }
#     return render(request, "leads/lead_create.html", context)