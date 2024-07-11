from django.shortcuts import render
import pickle

# Load your model
def load_model():
    with open('prediction/naive_bayes_matric_model_78.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Create your views here
def predict(request):
    if request.method == 'POST':
        # Load model
        model = load_model()

        # Get input data from form
        feature1 = float(request.POST['feature1'])
        feature2 = float(request.POST['feature2'])

        # Prepare input data for prediction
        input_data = [[feature1, feature2]]  # Adjust based on your model input

        # Make prediction
        prediction = model.predict(input_data)

        # Pass prediction result to template
        return render(request, 'prediction/result.html', {'prediction': prediction})

    return render(request, 'prediction/predict.html')
