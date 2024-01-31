# views.py

from django.shortcuts import render
import joblib
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.management.commands.createsuperuser import Command as CreateSuperuserCommand
from django.contrib.auth.forms import UserCreationForm
from .models import InsuranceResult

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import SignUpForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
            else:
                form.save()
                return redirect('login')  
        else:
            messages.error(request, "Invalid form submission. Please correct the errors.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')

# views.py
# views.py
from django.shortcuts import render
import joblib
import pandas as pd

def result(request):
    if request.method == 'POST':
        # Retrieve values from the form
        age = int(request.POST.get('age'))
        sex = request.POST.get('sex')
        bmi = float(request.POST.get('bmi'))
        smoker = request.POST.get('smoker')
        region = request.POST.get('region')
        children = int(request.POST.get('children'))
        

        # Mapping of options to numerical labels
        sex_mapping = {'Male': 0, 'Female': 1}
        smoker_mapping = {'No': 0, 'Yes': 1}
        region_mapping = {'Southwest': 0, 'Southeast': 1, 'Northwest': 2, 'Northeast': 3}

        # Encode values using the mappings
        sex_encoded = sex_mapping.get(sex, 0)
        smoker_encoded = smoker_mapping.get(smoker, 0)
        region_encoded = region_mapping.get(region, 0)

        # Prepare data for prediction
        data = {'age': [age], 'sex': [sex_encoded], 'bmi': [bmi], 'smoker': [smoker_encoded],
                'region': [region_encoded], 'children': [children]}
        input_data = pd.DataFrame(data)

        # Load the trained machine learning model
        cls = joblib.load("linear_regression_model.sav")

        # Make predictions using the loaded model
        predicted_insurance_charge = cls.predict(input_data)

        # Save the result in the database
        result_instance = InsuranceResult(
            age=age,
            sex=sex,
            bmi=bmi,
            smoker=smoker,
            region=region,
            children=children,
            predicted_insurance_charge=predicted_insurance_charge
        )
        result_instance.save()

        # Pass the values and predicted insurance charge to the template
        return render(request, "result.html", {'age': age, 'sex': sex,
                                               'bmi': bmi, 'smoker': smoker,
                                               'region': region, 'children': children,
                                               'predicted_insurance_charge': predicted_insurance_charge[0]})
    
    else:
        # Handle other HTTP methods if needed
        return render(request, "result.html", {'error': 'Invalid HTTP method'})

# views.py

