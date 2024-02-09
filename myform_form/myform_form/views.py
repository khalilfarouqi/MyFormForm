from django.shortcuts import render
from .forms import SignupForm, SignupFormWidget
# Create your views here.
def signup10_affichage(request) :
    form = SignupForm()
    return render(request, "myform_form/signup10_affichage.html", context={"form" : form})
def signup20_widget(request) :
    form = SignupFormWidget()
    return render(request, "classroom/signup20_widget.html", context={"form" : form})