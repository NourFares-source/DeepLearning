🏠 Melbourne House Price Predictor
A high-performance machine learning web application that predicts residential property prices in Melbourne, Australia. This project demonstrates an end-to-end data science pipeline, from advanced data preprocessing and exploratory data analysis (EDA) to model deployment.

🚀 View Live App on Streamlit

📌 Project Overview
The objective of this project was to build a predictive model that estimates house prices based on various features such as location, size, and property characteristics.

Unlike a simple linear model, this project implements an Ensemble Learning approach to capture complex, non-linear relationships in the real estate market, resulting in a significantly more accurate tool for potential buyers and investors.

📊 Key Results & Insights
Model Accuracy: The final Random Forest Regressor achieved an R² score of 77.07% on unseen testing data, a massive improvement over the baseline Linear Regression model (57.47%).

Primary Drivers: Location remains the most critical factor. Properties in the Southern Metropolitan region and proximity to the Central Business District (CBD) were the strongest predictors of price.

🛠️ Tech Stack
Language: Python 3.x

Data Science: Pandas, NumPy, Scikit-Learn

Visualization: Matplotlib, Seaborn

Model Persistence: Joblib

Deployment: Streamlit, Ngrok (for development tunneling)

📂 Repository Structure
Melbourne_Housing_Analysis.ipynb: The complete notebook containing data cleaning, handling missing values, outlier detection, and model training.

app.py: The production-ready Streamlit application script.

melbourne_rf_model.pkl: The trained Random Forest model.

scaler.pkl: The StandardScaler object used to normalize numerical features.

model_columns.pkl: Metadata containing the exact column order required for predictions.

