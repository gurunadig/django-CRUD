from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy, NoReverseMatch

from .models import Detail
from .forms import DetailForm

def home(request):

    return render(request, 'portal/landing.html')


def createdetail(request):
    details = Detail.objects.all()
    form = DetailForm()
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'details': details, 'form':form}
    return render(request, 'portal/createdetail.html', context)


def updatedetail(request, pk):
    details = Detail.objects.get(id=pk)
    form = DetailForm(instance=details)

    if request.method == 'POST':
        form = DetailForm(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect('/createdetail')

    context = {'form':form}
    return render(request, 'portal/createdetail.html', context)


def deletedetail(request, pk):
	details = Detail.objects.get(id=pk)
	if request.method == "POST":
		details.delete()
		return redirect('/createdetail')

	context = {'item':details}
	return render(request, 'portal/delete.html', context)