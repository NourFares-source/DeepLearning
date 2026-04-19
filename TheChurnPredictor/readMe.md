🏦 Bank Customer Churn Predictor (AI Retention Tool)
This project uses Machine Learning to predict the likelihood of a customer leaving a bank (Churning). By identifying at-risk customers early, financial institutions can proactively offer incentives to improve retention rates.

🚀 View Live Web App

🌟 Key Technical Features
Hyperparameter Tuning: Utilized GridSearchCV to optimize a Random Forest Classifier, ensuring the best balance between precision and recall.

Leakage Detection & Mitigation: Identified and removed "leaky" features (like the Complain column) that were causing artificial 99% accuracy, resulting in a more robust, real-world model.

Probabilistic Prediction: Instead of a simple "Yes/No," the app provides the probability of churn, allowing for risk-based prioritization.

📊 Performance & Insights
Model: Random Forest Classifier (Optimized via Grid Search)

Accuracy: 86% (Honest Model)

Top Predictors: Age, Number of Products, and IsActiveMember.

🛠️ Tech Stack
Python (Pandas, NumPy)

Scikit-Learn (Random Forest, GridSearchCV, One-Hot Encoding)

Streamlit (User Interface)

Joblib (Model Serialization)

📂 Repository Structure
Churn_Modelling.csv: The primary dataset from Kaggle.

churn_analysis.ipynb: The full data science workflow (EDA, Encoding, Tuning, Leakage Fix).

app.py: The production Streamlit application script.

churn_model.pkl: The trained, optimized Random Forest "brain."

