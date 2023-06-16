from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

def home(request):
    return render(request,'home.html')
def predict(request):
    return render(request,'predict.html')
def result(request):
    df = pd.read_excel(r'C:\Users\Gaayana\OneDrive\Desktop\DiabetesPrediction\DiabetesPrediction\DiabetesPrediction\dataset1.xlsx').drop(['Name','Gender'], axis = 1)
    # Convert data types
    df = df.astype({
        'Age': 'int64',
        'Ambient Temperature': 'int64',
        'Ambient Humidity': 'int64',
        'Skin temperature': 'float64',
        'Heart rate': 'int64',
        'SpO2': 'int64',
        'Mean_bp': 'float64',
        'Galvanic skin response': 'int64',
        'Blood glucose level': 'int64'
    })

    # Rename columns
    df.columns = ['age', 'ambient_temp', 'ambient_humidity', 'skin_temp', 'heart_rate', 'spo2', 'mean_bp', 'gsr', 'glucose']

    # Remove outliers using the IQR method
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop('glucose', axis=1),
                                                        df['glucose'],
                                                        test_size=0.2,
                                                        random_state=42)
    
    # create the GradientBoostingRegressor model
    gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

    # train the model on the training data
    gbr.fit(X_train, y_train)

    #fetch values
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    #prediction
    pred = gbr.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    #display result
    return render(request,'predict.html', {"result2":pred})

