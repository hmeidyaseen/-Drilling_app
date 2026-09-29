import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Differential Sticking Predictor",
    page_icon="🌵",
    layout="wide"
)

# 2. Black Theme CSS & LTR Alignment
st.markdown("""
    <style>
    /* Full Black Background */
    .stApp {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        direction: ltr !important;
        text-align: left !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #121212 !important;
    }

    /* Metric cards styling */
    [data-testid="stMetric"] {
        background-color: #121212 !important;
        border: 1px solid #333333 !important;
        border-radius: 10px;
        padding: 15px;
    }

    /* All text white */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Main Interface Header
st.title("🌵 Differential Sticking Predictor & Decision Support System")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🎯 Model Accuracy",
        value="99.33%",
        delta="XGBoost High Precision ML Model"
    )

with col2:
    st.metric(
        label="⏱️ Stuck Resolution Time",
        value="< 6 Hours",
        delta="Traditional NPT: 2 - 7 Days"
    )

with col3:
    st.metric(
        label="💰 Loss Reduction Rate",
        value="60% - 85%",
        delta="BHA Downtime Cost Savings"
    )
