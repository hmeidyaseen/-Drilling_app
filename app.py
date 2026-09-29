import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Differential Sticking Predictor",
    page_icon="🌵",
    layout="wide"
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Differential Sticking Predictor", layout="wide")

# 2. إنشاء الشريط الجانبي لإدخال واسترجاع بيانات الحفر
st.sidebar.header("📋 Drilling Parameters Input")

# حقول إدخال بيانات الحفر
mud_weight = st.sidebar.number_input("Mud Weight (PPG)", min_value=8.0, max_value=20.0, value=10.5, step=0.1)
diff_pressure = st.sidebar.number_input("Differential Pressure (PSI)", min_value=0, max_value=5000, value=1200)
bha_length = st.sidebar.number_input("BHA Length (ft)", min_value=0, max_value=2000, value=450)
hole_diameter = st.sidebar.number_input("Hole Diameter (in)", min_value=4.0, max_value=26.0, value=8.5)
mud_type = st.sidebar.selectbox("Mud Type", ["Water-Based (WBM)", "Oil-Based (OBM)", "Synthetic-Based (SBM)"])

# زر لتنفيذ الحسابات/التنبؤ بناءً على البيانات المدخلة
predict_button = st.sidebar.button("Predict Sticking Risk")

# 3. عرض البطاقات الإحصائية في الواجهة الرئيسية
st.title("🌵 Differential Sticking Predictor & Decision Support System")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🎯 Model Accuracy", "99.33%", "XGBoost High Precision ML Model")
with col2:
    st.metric("⏱️ Stuck Resolution Time", "< 6 Hours", "Traditional NPT: 2 - 7 Days")
with col3:
    st.metric("💰 Loss Reduction Rate", "60% - 85%", "BHA Downtime Cost Savings")

st.divider()

# 4. عرض البيانات المدخلة في الصفحة الرئيسية عند الضغط على الزر
if predict_button:
    st.success("تم استرجاع بيانات الحفر بنجاح!")
    st.write("### البيانات التي تم إدخالها:")
    st.json({
        "Mud Weight": mud_weight,
        "Differential Pressure": diff_pressure,
        "BHA Length": bha_length,
        "Hole Diameter": hole_diameter,
        "Mud Type": mud_type
    })


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
