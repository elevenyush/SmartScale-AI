import sys
import os


sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)


import streamlit as st

st.set_page_config(
    page_title="SmartScale AI",
    page_icon="🚀",
    layout="wide"
)
import pandas as pd
import math
from src.train_model import train_model
from src.predictor import (
    predict_traffic,
    forecast_next_7_days
)
import pandas as pd
import math
from src.train_model import train_model
from src.predictor import (
    predict_traffic,
    forecast_next_7_days
)
from src.report_generator import generate_report
# Load data
data = pd.read_csv("data/traffic_data.csv")

model = train_model()
st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    div[data-testid="stMetric"] {
        background-color: #1E1E1E;
        border: 1px solid #333333;
        padding: 15px;
        border-radius: 12px;
    }

    div[data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# UI
st.title("🚀 SmartScale AI Operations Dashboard")

st.info(
    """
    Model: Multiple Linear Regression
    
    Dataset Size: 365 Days
    
    Features: Month, Day, Weekend, Holiday, Sale
    """
)

st.caption(
    "Machine Learning based website traffic forecasting and server capacity recommendation system."
)


st.subheader("📊 Traffic Analytics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Traffic",
        round(data["visitors"].mean())
    )

with col2:
    st.metric(
        "Maximum Traffic",
        round(data["visitors"].max())
    )

with col3:
    st.metric(
        "Minimum Traffic",
        round(data["visitors"].min())
    )
st.subheader("📈 Business Insights")

weekend_avg = data[data["is_weekend"] == 1]["visitors"].mean()
weekday_avg = data[data["is_weekend"] == 0]["visitors"].mean()

sale_avg = data[data["sale_running"] == 1]["visitors"].mean()
normal_avg = data[data["sale_running"] == 0]["visitors"].mean()

st.write(
    f"Weekend traffic is {round((weekend_avg/weekday_avg)*100 - 100)}% higher than weekday traffic."
)

st.write(
    f"Sales campaigns increase traffic by approximately {round((sale_avg/normal_avg)*100 - 100)}%."
)
st.line_chart(data["visitors"])


months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}



days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}
with st.sidebar:

    st.title("🚀 SmartScale AI")

    st.markdown("""
    ### Operations Dashboard

    Predict traffic, estimate
    infrastructure needs,
    and identify risk levels.
    """)

    st.subheader("⚡ Quick Scenarios")

    scenario = st.radio(
        "Choose Scenario",
        [
            "Custom",
            "Weekend Rush",
            "Holiday Traffic",
            "Sale Event",
            "Black Friday"
        ]
    )

    selected_month = st.selectbox(
        "Month",
        list(months.keys())
    )

    month = months[selected_month]

    selected_day = st.selectbox(
        "Day of Week",
        list(days.keys())
    )

    day = days[selected_day]

    weekend = st.selectbox(
        "Weekend?",
        ["No", "Yes"]
    )

    weekend = 1 if weekend == "Yes" else 0

    holiday = st.selectbox(
        "Holiday?",
        ["No", "Yes"]
    )

    holiday = 1 if holiday == "Yes" else 0

    sale = st.selectbox(
        "Sale?",
        ["No", "Yes"]
    )

    sale = 1 if sale == "Yes" else 0

    if scenario == "Weekend Rush":
        weekend = 1

    elif scenario == "Holiday Traffic":
        holiday = 1

    elif scenario == "Sale Event":
        sale = 1

    elif scenario == "Black Friday":
        weekend = 1
        holiday = 1
        sale = 1

    current_servers = st.number_input(
        "Current Servers Available",
        min_value=1,
        value=1
    )

    predict_button = st.button(
        "🚀 Predict Traffic"
    )

if predict_button:
    prediction = predict_traffic(
        model,
        month,
        day,
        weekend,
        holiday,
        sale
    )

    forecast_df = forecast_next_7_days(
        model,
        month,
        holiday,
        sale
    )

    servers_needed = math.ceil(prediction / 5000)
    extra_servers = servers_needed - current_servers

    monthly_server_cost = 3000

    extra_cost = max(
    0,
    extra_servers * monthly_server_cost
)

    

    col1, col2, col3 = st.columns(3)

    risk_level = ""

    if prediction < 7000:
        risk_level = "LOW"
    elif prediction < 12000:
        risk_level = "MEDIUM"
    elif prediction < 18000:
        risk_level = "HIGH"
    else:
        risk_level = "CRITICAL"

   


    with col1:
        st.metric(
            "📈 Predicted Traffic",
            prediction
        )

    with col2:
        st.metric(
            "🖥️ Servers Needed",
            servers_needed
        )

    with col3:
        st.metric(
            "⚠️ Risk Level",
            risk_level
        )

    st.divider()

    st.subheader("🤖 AI Insight")

    reasons = []

    if weekend == 1:
        reasons.append("Weekend traffic increase")

    if holiday == 1:
        reasons.append("Holiday demand surge")

    if sale == 1:
        reasons.append("Active sales campaign")

    if len(reasons) == 0:
        reasons.append("Normal business traffic")

    st.info(
        f"""
Traffic is expected to reach approximately {prediction:,} visitors.

Primary factors:
• {' • '.join(reasons)}
"""
    )

    st.divider()

    st.subheader("🏗 Infrastructure Status")

    if current_servers >= servers_needed:

        st.success(
            f"""
Current Capacity: {current_servers} Servers

Required Capacity: {servers_needed} Servers

Status: CAPACITY SUFFICIENT
"""
        )

    else:

        st.error(
            f"""
Current Capacity: {current_servers} Servers

Required Capacity: {servers_needed} Servers

Need {extra_servers} more server(s)
"""
        )

    st.divider()

    st.subheader("💡 Recommendations")

    recommendations = []

    if servers_needed > current_servers:
        recommendations.append(
            f"Provision {extra_servers} additional server(s)"
        )

    if sale == 1:
        recommendations.append(
            "Enable auto-scaling during the campaign"
        )

    if prediction > 15000:
        recommendations.append(
            "Monitor response times closely"
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Current infrastructure appears healthy"
        )

    for item in recommendations:
        st.write(f"• {item}")

        

      

        st.divider()

    st.subheader("🔮 7-Day Forecast")

    st.line_chart(
        forecast_df.set_index("Day")
    )

    max_day = forecast_df.loc[
        forecast_df["Predicted Traffic"].idxmax()
    ]
    pdf_path = generate_report(
    prediction,
    servers_needed,
    risk_level,
    current_servers,
    recommendations,
    extra_cost,
    max_day["Day"],
    max_day["Predicted Traffic"]
)

    st.warning(
        f"""
Peak Traffic Day: {max_day['Day']}

Expected Visitors: {max_day['Predicted Traffic']:,}
"""
    )

    st.divider()

    st.subheader("📄 Forecast Report")

    with open(pdf_path, "rb") as file:

        st.download_button(
            label="📥 Download PDF Report",
            data=file,
            file_name="SmartScale_Report.pdf",
            mime="application/pdf"
        )