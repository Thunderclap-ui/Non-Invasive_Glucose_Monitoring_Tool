# Non Invasive Glucose Monitoring Tool
<p>
    <img align="left" alt="Health_Care" title="Health Care" width="750" height="370" src="https://www.bioworld.com/ext/resources/Stock-images/Therapeutic-topics/Diabetes/diabetes-management.png?1593552366">
</p>

The project aims to combine non-invasive <b> biometric measurements </b> streamed through IoT sensors with machine learning algorithms to accurately predict <b> blood glucose levels (BGLs)</b>.<br><br>
Features used:<br>
  **`Pulse Oxygen (SpO2)`**<br>
  **`Ambient Humidity`**<br>
  **`Ambient Temperature`**<br>
  **`Skin Temperature`**<br>
  **`Heart Rate`**<br>
  **`Blood Pressure`**<br>
  **`Electrodermal Activity`**<br>

## Overview:
The project objectives that are being resolved are:
<br>• To take values from the interface provided by the user and predict the value of body glucose through the given values.
<br>• To create an alert that reminds the user about the body's high or low glucose level according to the predicted value.
<br>• To develop a system that can help the healthcare industry and diabetic patients monitor their blood glucose levels.

## Tools and Framework:
IoT: **`Arduino IDE 2.0`** **`C++ 22`**
<br>Machine Learning: **`Python 3.11`** 
<br>Web Interface: **`Django 4.2.2`** **`HTML 5`** **`CSS 3`** **`Javascript ES6`** 
<br>Database: **`SQLite`** 

## Features:
### System Architecture
The system architecture has 3 phases where it involves Data Processing, Data Transformation and Prediction.
<br>• Load and pre-process the dataset.
<br>• Split the processed data into train and test dataset.
<br>• Transform the data by scaling using mean and standard deviation.
<br>• Train and validate the model using the train dataset to fetch a best fit model.
<br>• Pass the sensor fetched real time data to predict the glucose value.

### Testing Evaluation
1. Data Collection: 
**`Valid Data Collection`** **`Data Synchronization`** **`Sensor Displacement`** **`Sensor Calibration`**
2. Data Pre-Processing:
**`Missing Data`** **`Outlier Detection`** **`Data Validation`**
3. IoT Module:
**`GSR Measurement`** **`Signal Stability`** **`Sensor Placement`**
4. Interface Model:
**`Blood Glucose Prediction`** **`Clinical Range Alert`** **`User Interface Responsiveness`**

### Algorithm Models
<p align="left">
      <a href="https://scikit-learn.org/stable/modules/tree.html">
         <img alt="Algo 1" title="Decision Tree Model" src="https://custom-icon-badges.demolab.com/badge/-Decision_Tree-gold?style=for-the-badge&logo=decision_tree&logoColor=black"/></a>
      <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html">
         <img alt="Algo 2" title="Random Forest Regressor" src="https://custom-icon-badges.demolab.com/badge/-Random_Forest_Regressor-plum?style=for-the-badge&logo=random_forest&logoColor=black"/></a> 
      <a href="https://github.com/ForrestKnight?tab=followers">
         <img alt="Algo 3" title="Long Short Term Model" src="https://custom-icon-badges.demolab.com/badge/-Long_Short_Term-palegreen?style=for-the-badge&logoColor=black&logo=long_short"/></a>
      <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html">
         <img alt="Algo 4" title="Gradient Boosting Regressor" src="https://custom-icon-badges.demolab.com/badge/-Gradient_Boosting_Regressor-teal?style=for-the-badge&logo=gradient_booster&logoColor=black"/></a>
   </p>

## Getting Started:
To get started with the project, you will need to download and install DB browser for database related work, install the required modules & libs specified in the **`Library_Required`** readme file.
Make sure you have the following tool to run and view the project working: **`Visual Code`** and the frameworks listed in the **`Tools and Framework`** block. Once you get the local host url, input the coresponding input values of a person to get the model training for the predicted glucose value.

## Snapshots:
<p align="left">
  <img src="https://github.com/Thunderclap-ui/Non-Invasive_Glucose_Monitoring_Tool/assets/68047912/c0e3c9aa-8566-4fb3-a517-2cf246e3f512"/>
</p>
