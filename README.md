<p align="center">
  <img src="https://img.shields.io/badge/AQI%20HealthPredictor-Environmental%20Risk%20Estimator-1E90FF?style=for-the-badge" />
</p>

<h1 align="center"> AI-Enabled AQI HealthPredictor</h1>

<p align="center">
A clean, data-driven project that predicts health impact levels based on Air Quality Index (AQI).  
Built originally as an academic backend assignment and later enhanced independently with additional modelling and a frontend interface.

</p>

---

##  Overview
This project analyzes AQI data and uses regression modelling to estimate health-risk levels associated with pollution.  
The backend manages data cleaning, training, and prediction, while the frontend offers a simple UI for showing results and interacting with the model.

---

##  Features
- AQI dataset preprocessing  
- Linear & polynomial regression models  
- Lightweight UI for user interaction  
- Modular and extendable codebase  

---

##  Tech Stack
**Backend:** Python, Pandas, NumPy, Scikit-Learn  
**Frontend:** Streamlit
**Tools:** Git, GitHub  

---

##  Project Structure

/

├── aqi.csv # AQI dataset

├── aqiHealth.py # Preprocessing, modelling, prediction logic

├── frontend/ # Frontend UI (added later)

└── README.md

---

## Dataset Information
The project uses an AQI dataset (`aqi.csv`) containing historical air-quality readings.  
Key columns include:

- **Date** – Timestamp of the recorded AQI  
- **AQI Value** – Overall Air Quality Index  
- **PM2.5, PM10, NO₂, SO₂, CO, O₃** – Pollutant concentrations (if present)  
- **Health Category** – General AQI-based category (Good/Moderate/Poor/etc.)

The dataset is used for:
- Training regression models  
- Identifying pollution–health patterns  
- Generating prediction values for the frontend


---

##  How to Run

### 1. Clone the repo  
```bash
git clone https://github.com/pratheeksha2023/AI-Enabled-AQI-HealthPredictor
```

### 2. Install dependencies
```bash
pip install pandas numpy scikit-learn streamlit
```

### 3. Start application
```bash
streamlit run aqiHealth.py
```

---

## 📊 Insights & Outcomes

- Polynomial regression showed better accuracy compared to the linear model.  
- Strong correlation observed between rising AQI levels and increased predicted health-risk values.  
- The codebase allows easy extension for more complex environmental or health datasets.

---

## Future Enhancements

- Integrate real-time AQI data through public APIs.  
- Add more predictive features such as weather conditions and demographic factors.  
- Upgrade the frontend into a dashboard with charts and interactive analytics.  
- Deploy the complete system using Docker or cloud hosting.

---

## Background

This project was originally created as an academic backend assignment centered around only one regression modelling.  
The Other one Regression model (Polynomial regression), More Data visualizations and Frontend interface was later added independently to make the system more practical and user-friendly.

---

