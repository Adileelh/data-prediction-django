from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is my home page")
# Create your views here.
def predict(request):
    return render(request, "predict/predict.html")
# Create your views here.
def contact(request):
    
    return render(request, "contact/contact.html")
