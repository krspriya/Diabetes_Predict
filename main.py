# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Diabetic import Diabetic
import joblib
import pandas as pd
# 2. Create the app object
app = FastAPI()
model_filename = 'diabetes.pkl'
model = joblib.load(model_filename)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to Mavericks Care': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
@app.post('/predict')
def predict_diabetes(data:Diabetic):
    data = pd.DataFrame([{
        'HighBP': data.HighBP,
        'HighChol': data.HighChol,
        'BMI': data.BMI,
        'DiffWalk': data.DiffWalk,
        'Sex': data.Sex,
        'Age': data.Age
    }])

    prediction = model.predict(data)
    if(prediction[0]==0):
        prediction="No Diabetes"
    elif (prediction[0]==1):
        prediction="Diabetes"
    else:
        prediction="Pre Diabetes"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload