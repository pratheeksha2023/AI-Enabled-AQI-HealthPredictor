import streamlit as st
import pandas as pd
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
st.title('Health Impact Prediction from Air Quality Data')
st.markdown('Interactive prediction app for hospital admissions based on pollutant levels and weather.')
df=pd.read_csv(r'D:/Engineering/6th sem/ml proj/aqi.csv')
df.head()
df.shape
df.info()
df.describe()
df.nunique()
df.isnull().sum()
for col in df:
    plt.figure(figsize=(5,3))
    df[col].plot(kind='hist',title=col,bins=60,edgecolor='red')
for col in df:
 plt.figure(figsize=(5,3))
 sb.boxplot(df[col],color='pink')
corr_matrix = df.corr()
plt.figure(figsize=(12, 8))
sb.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
fig = plt.gcf() 
st.pyplot(fig) 
sb.pairplot(df, diag_kind='kde')
plt.title('Pairplot')
fig = plt.gcf()  
st.pyplot(fig) 
X = df[['SO2']]
y = df['HospitalAdmissions']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Linear Regression Model Mean Squared Error: ", mse)
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='True Hospital Admissions')
plt.plot(X_test, y_pred, color='red', label='Predicted (Linear Regression)')
plt.xlabel('SO2')
plt.ylabel('Hospital Admissions')
plt.title('Linear Regression- Health Impact Prediction')
plt.legend()
fig = plt.gcf()  
st.pyplot(fig) 
poly_features = PolynomialFeatures(degree=3)
X_poly_train_transformed = poly_features.fit_transform(X_train)
X_poly_test_transformed = poly_features.transform(X_test)
poly_reg = LinearRegression()
poly_reg.fit(X_poly_train_transformed, y_train)
y_poly_pred_transform = poly_reg.predict(X_poly_test_transformed)
mse_poly_reg = mean_squared_error(y_test, y_poly_pred_transform)
print("Polynomial Regression Model Mean Squared Error: ", mse_poly_reg)
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='True Hospital Admissions')
plt.scatter(X_test, y_poly_pred_transform, color='red', label='Predicted␣(Polynomial Regression)')
plt.xlabel('SO2')
plt.ylabel('Hospital Admissions')
plt.title('Polynomial Regression- Health Impact Prediction')
plt.legend()
fig = plt.gcf()  
st.pyplot(fig) 
st.sidebar.header('Input Air Quality Parameters')

def user_input_features():
    SO2 = st.sidebar.slider('SO2', 0.0, 200.0, 50.0)
    PM10 = st.sidebar.slider('PM10', 0.0, 400.0, 100.0)
    PM25 = st.sidebar.slider('PM2.5', 0.0, 200.0, 50.0)
    NO2 = st.sidebar.slider('NO2', 0.0, 150.0, 50.0)
    O3 = st.sidebar.slider('O3', 0.0, 100.0, 40.0)
    Temperature = st.sidebar.slider('Temperature', -10.0, 50.0, 25.0)
    Humidity = st.sidebar.slider('Humidity (%)', 0, 100, 50)
    WindSpeed = st.sidebar.slider('Wind Speed', 0.0, 20.0, 5.0)
    data = {
        'SO2': SO2,
        'PM10': PM10,
        'PM25': PM25,
        'NO2': NO2,
        'O3': O3,
        'Temperature': Temperature,
        'Humidity': Humidity,
        'WindSpeed': WindSpeed
    }
    features_df = pd.DataFrame(data, index=[0])
    return features_df
input_df = user_input_features()
