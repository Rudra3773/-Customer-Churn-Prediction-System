import streamlit as st
import sys

sys.path.append("../src")

from predict import predict_churn

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction System")

st.write("Enter customer details and predict churn probability.")

# -----------------------
# Input Form
# -----------------------

gender = st.selectbox("Gender", [0, 1])

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", [0, 1])

dependents = st.selectbox("Dependents", [0, 1])

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    value=12
)

phone_service = st.selectbox("Phone Service", [0, 1])

multiple_lines = st.selectbox("Multiple Lines", [0, 1])

internet_service = st.selectbox("Internet Service", [0, 1])

online_security = st.selectbox("Online Security", [0, 1])

online_backup = st.selectbox("Online Backup", [0, 1])

device_protection = st.selectbox("Device Protection", [0, 1])

tech_support = st.selectbox("Tech Support", [0, 1])

streaming_tv = st.selectbox("Streaming TV", [0, 1])

streaming_movies = st.selectbox("Streaming Movies", [0, 1])

contract = st.selectbox(
    "Contract",
    [0, 1, 2]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    [0, 1]
)

payment_method = st.selectbox(
    "Payment Method",
    [0, 1, 2, 3]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    value=75.5
)

total_charges = st.number_input(
    "Total Charges",
    value=900.0
)

# -----------------------
# Prediction
# -----------------------

if st.button("Predict Churn"):

    customer = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    prediction, probability = predict_churn(customer)

    st.subheader("Prediction Result")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    if prediction == 1:
        st.error("⚠️ Customer Likely To Churn")
    else:
        st.success("✅ Customer Likely To Stay")


         # ==========================
         # Risk Meter
         # ==========================

    st.markdown("---")

    if probability < 0.30:
        risk_level = "🟢 Low Risk"

    elif probability < 0.70:
        risk_level = "🟡 Medium Risk"

    else:
        risk_level = "🔴 High Risk"

    st.subheader("Risk Analysis")

    st.metric(
        "Risk Level",
        risk_level
    )



    # ==========================
    # Customer Segmentation
    # ==========================

    if tenure < 12:
        segment = "New Customer"

    elif tenure < 36:
        segment = "Regular Customer"

    else:
        segment = "Loyal Customer"

    st.metric(
        "Customer Segment",
        segment
    )



    # ==========================
    # Probability Gauge
    # ==========================

    import plotly.graph_objects as go

    st.subheader("Churn Probability Gauge")

    gauge_fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability * 100,

            title={
                "text": "Churn Probability (%)"
            },

            gauge={
                "axis": {
                    "range": [0, 100]
                },

                "steps": [

                    {
                        "range": [0, 30]
                    },

                    {
                        "range": [30, 70]
                    },

                    {
                        "range": [70, 100]
                    }

                ]
            }
        )
    )

    st.plotly_chart(
        gauge_fig,
        use_container_width=True
    )



    # ==========================
    # Pie Chart
    # ==========================

    import plotly.express as px

    pie_data = {
        "Status": [
            "Stay",
            "Churn"
        ],

        "Value": [
            1 - probability,
            probability
        ]
    }

    pie_fig = px.pie(
        values=pie_data["Value"],
        names=pie_data["Status"],
        title="Customer Churn Distribution",
        hole=0.45
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )



    # ==========================
    # Recommendation Engine
    # ==========================

    st.subheader("Business Recommendation")

    if probability > 0.70:

        st.error("""
        🔥 High Churn Risk

        Recommended Actions:

        • Offer Discount

        • Customer Retention Call

        • Loyalty Benefits

        • Upgrade Service Plan

        • Priority Support
        """)

    elif probability > 0.40:

        st.warning("""
        ⚠️ Medium Churn Risk

        Recommended Actions:

        • Send Promotional Offers

        • Engage Through Email Campaign

        • Customer Satisfaction Survey
        """)

    else:

        st.success("""
        ✅ Low Churn Risk

        Recommended Actions:

        • Maintain Service Quality

        • Cross Sell Products

        • Reward Loyal Customers
        """)
    
    
    # Colorful Metrics


col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

with col2:
    st.metric(
        "Customer Segment",
        segment
    )


        


# Sidebar


st.sidebar.title("Customer Churn Dashboard")

st.sidebar.info("""
Built using:
- Python
- Scikit-Learn
- Streamlit
- Plotly
""")


# Footer


st.markdown("---")

st.caption(
    "Developed by Rudra Tripathi | AI/ML Engineer & Data Scientist"
)


