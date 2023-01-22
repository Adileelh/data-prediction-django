from django.shortcuts import render, HttpResponse
import joblib

model = joblib.load('static/random_forest_regressor')

# Create your views here.


def index(request):
    return render(request, "index/index.html")
# Create your views here.


def predict(request):

    if request.method == 'POST':
        age = int(request.POST.get('age'))
        sex = request.POST.get('sex')
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = request.POST.get('smoker')
        region = request.POST.get('region')

        # print(age, sex, bmi, children, smoker, region)

        pred = round(model.predict(
            [[age, sex, bmi, children, smoker, region]])[0])

        context = {
            'prediction': pred
        }

        return render(request, "predict/predict.html", context)
    else:
        return render(request, "predict/predict.html")


# Create your views here.


def contact(request):

    return render(request, "contact/contact.html")
