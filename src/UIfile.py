import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
import timeit
import warnings
warnings.filterwarnings("ignore")
import streamlit as st


# Give a title to the web app
st.title("Machine Learning Credit Card Fraud Detection")

# Load the data
df = pd.read_csv("application_data.csv")
st.success("Fetched data!") 

# Preprocess the data
# Clean the data
df = df.dropna()
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

df['FLAG_OWN_CAR'] = LabelEncoder().fit_transform(df['FLAG_OWN_CAR'])

# Print shape and description of the data
if st.sidebar.checkbox('Show what the dataframe looks like'):
    st.write(df.head(100))
    st.write('Shape of the dataframe: ',df.shape)
    st.write('Data decription: \n',df.describe())
    
# Use only columns that affects the prediction significantly, drop the target and 
X = df.drop(['SK_ID_CURR', 'TARGET'], axis=1)
cols = ['EXT_SOURCE_3','EXT_SOURCE_1','EXT_SOURCE_2','DAYS_REGISTRATION','DAYS_BIRTH','DAYS_EMPLOYED','DAYS_ID_PUBLISH','AMT_ANNUITY','AMT_CREDIT','COMMONAREA_AVG']

X = X[cols]
y = df['TARGET']

# Train the model
X_scaled = StandardScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(max_depth=100, random_state=1)
model.fit(X_train, y_train)

# Print valid and fraud transactions
fraud=df[df.TARGET==1]
valid=df[df.TARGET==0]

outlier_percentage=(df.TARGET.value_counts()[1]/df.TARGET.value_counts()[0])*100
if st.sidebar.checkbox('Show fraud and valid transaction details'):
    st.write('Fraudulent transactions are: %.3f%%'%outlier_percentage)
    st.write('Fraud Cases: ',len(fraud))
    st.write('Valid Cases: ',len(valid))
    
# Extract feature importance
feature_importances = pd.DataFrame(model.feature_importances_,
                                   index = X.columns,
                                   columns=['importance']).sort_values('importance',
                                   ascending=False)


if st.sidebar.checkbox('Show feature importance'):
    st.write('Feature importance: ',feature_importances)

    
if st.sidebar.checkbox('Predict if transcation fraudulent'):
    ext_src_1 = st.number_input("Enter Ext source 1")
    ext_src_2 = st.number_input("Enter Ext source 2")
    ext_src_3 = st.number_input("Enter Ext source 3")
    days_registration = st.number_input("Enter Days Registration")
    days_birth = st.number_input("Enter Days_birth")
    days_employed = st.number_input("Enter Days_employed")
    days_id_publish = st.number_input("Enter Days_id_publish")
    amt_annuity = st.number_input("Enter Amt_annuity")
    amt_credit = st.number_input("Enter Amt_credit")
    commonarea_avg= st.number_input("Enter Commonarea_avg")


# Define the function to make predictions
def predict():
    input_data = [[ext_src_3, ext_src_1, ext_src_2, days_registration, days_birth, days_employed, days_id_publish, amt_annuity, amt_credit, commonarea_avg]]
    output = model.predict(input_data)
    
    if output[0] > 1:
        #with st.echo():
            st.title("Fraudulent Transaction")
            st.write("Warning: This transaction appears to be fraudulent. Please contact your bank immediately.")
    else:
        #with st.echo():
            st.title("Legitimate Transaction")
            st.write("Good News: This transaction appears to be legitimate. Thank you for using our service.")
   

# Connect the predict function to the button click event
if st.button('Predict'):
    st.write('Predicting..')
    predict()



