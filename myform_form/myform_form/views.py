from django.shortcuts import render
from .forms import SignupForm, SignupFormWidget, SignupFormData
# Create your views here.
def signup10_affichage(request) :
    form = SignupForm()
    return render(request, "myform_form/signup10_affichage.html", context={"form": form})
def signup20_widget(request) :
    form = SignupFormWidget()
    return render(request, "classroom/signup20_widget.html", context={"form": form})
def signup30_data(request):
    form = SignupFormData()
    if request.method == "POST":
        print(request.POST)
    return render(request, "myform_form/signup30_data.html", context={"form": form})