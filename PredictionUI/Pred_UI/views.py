import pickle
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import SalaryPrediction

# Load the model
with open(r"C:\Users\rillh\PredictionUI\Pred_UI\linear_model.pkl", "rb") as file:
    model = pickle.load(file)


def predict_salary(request):
    if request.method == "POST":
        # Get the years of experience from the form input
        years_experience = float(request.POST.get("years_experience", 0))
        
        # Make the prediction using the loaded model
        try:
            predicted_salary = model.predict([[years_experience]])[0]
            
            # Save the prediction result to the database
            prediction = SalaryPrediction.objects.create(
                years_experience=years_experience,
                predicted_salary=predicted_salary
            )
            
            # Redirect to the specific result.html page
            return redirect('view_prediction', prediction_id=prediction.id)
        
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"})

    # Render the input form for GET requests
    return render(request, 'predict.html')


def view_predictions(request):
    # Fetch all stored predictions
    predictions = SalaryPrediction.objects.all().order_by('-created_at')  # Latest first
    return render(request, 'result.html', {'predictions': predictions})


def view_prediction(request, prediction_id):
    # Fetch the specific prediction by ID or return 404 if not found
    prediction = get_object_or_404(SalaryPrediction, id=prediction_id)
    
    # Render the result.html template with the prediction data
    return render(request, 'result.html', {'prediction': prediction})




