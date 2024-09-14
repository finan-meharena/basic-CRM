from django.http import HttpResponse
from django.shortcuts import render
from .models import Lead


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
    