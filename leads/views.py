from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadForm


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, 'leads/lead_list.html', context)


def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead" : lead
    }
    return render(request, 'leads/lead_detail.html', context = context)

def lead_create(request):
    form = LeadForm()
    print(request.POST)
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent,
            )
            return redirect("/leads")
    context = {
        "form" : form,
    }
    return render(request, "leads/lead_create.html", context)