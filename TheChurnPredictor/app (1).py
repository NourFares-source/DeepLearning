import streamlit as st
import pandas as pd
import joblib

# 1. Load the assets
# We use try/except to give a helpful error if the files aren't exported yet
try:
    model = joblib.load('churn_model.pkl')
    model_columns = joblib.load('churn_columns.pkl')
except:
    st.error("Model files not found! Please run the export cell in your notebook first.")

st.set_page_config(page_title="Bank Churn AI", page_icon="🏦")

st.title("🏦 Bank Customer Churn Predictor")
st.markdown("""
Predict which customers are likely to leave the bank based on their profile.
**Data Scientist Tip:** *Age* and *IsActiveMember* are often the strongest drivers!
""")

# 2. Input Layout
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customer Profile")
        credit_score = st.slider("Credit Score", 300, 850, 600)
        age = st.number_input("Age", 18, 100, 35)
        tenure = st.slider("Tenure (Years)", 0, 10, 5)
        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
        geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

    with col2:
        st.subheader("Bank Relationship")
        balance = st.number_input("Account Balance ($)", min_value=0.0, value=50000.0)
        num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
        is_active = st.toggle("Active Member Status", value=True)
        has_card = st.toggle("Has Credit Card", value=True)
        salary = st.number_input("Estimated Salary ($)", min_value=0.0, value=75000.0)

# 3. Prediction Logic
if st.button("Analyze Customer Retention Risk", type="primary", use_container_width=True):
    # Prepare the raw data
    input_dict = {
        'CreditScore': credit_score,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_products,
        'HasCrCard': int(has_card),
        'IsActiveMember': int(is_active),
        'EstimatedSalary': salary,
        # Based on your data info, including satisfaction/points if they were in the final model
        'Satisfaction Score': 3, 
        'Point Earned': 500
    }
    
    input_df = pd.DataFrame([input_dict])
    
    # Handle One-Hot Encoding manually to match our 'df_final'
    input_df[f"Geography_{geography}"] = 1
    input_df[f"Gender_Male"] = 1 if gender == "Male" else 0
    # Note: Drop_first=True was used in training, so France/Female are the 'baseline' (all zeros)

    # Reindex to match the exact training columns order
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    
    # Predict
    prob = model.predict_proba(input_df)[0][1]
    
    # 4. Results Display
    st.divider()
    if prob > 0.5:
        st.error(f"### ⚠️ High Risk: {prob:.1%} probability of leaving")
        st.warning("Recommendation: Offer loyalty incentives or a personal account review.")
    else:
        st.success(f"### ✅ Low Risk: {prob:.1%} probability of leaving")
        st.info("Recommendation: Maintain standard communication.")
