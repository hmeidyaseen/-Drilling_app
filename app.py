import streamlit as st

# 1. إعدادات الصفحة - تم إغلاق القوس بشكل صحيح
st.set_page_config(
    page_title="Drilling App",
    page_icon="🛢️",
    layout="wide"
)

# 2. تخصيص المظهر باللون الأزرق
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f4f8;
    }
    [data-testid="stSidebar"] {
        background-color: #1e3a8a;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    h1, h2, h3 {
        color: #1d4ed8;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 3. اختيار اللغة
st.sidebar.title("Settings / إعدادات")
language = st.sidebar.radio("Choose Language / اختر اللغة:", ("العربية", "English"))

# 4. واجهة التطبيق
if language == "العربية":
    st.title("🛢️ تطبيق حسابات الحفر")
    st.write("أهلاً بك! يمكنك استخدام الأدوات والحسابات الهندسية الخاصة بالحفر هنا.")
    
    st.header("بيانات الحفر الأساسية")
    depth = st.number_input("العمق الكلي (متر/قدم):", min_value=0.0, value=1000.0)
    mud_weight = st.number_input("كثافة الطين (PPG / SG):", min_value=0.0, value=9.5)
    
    if st.button("حساب"):
        st.success(f"تم تسجيل البيانات: العمق {depth} والكثافة {mud_weight}")

else:
    st.title("🛢️ Drilling Operations App")
    st.write("Welcome! You can use drilling engineering tools and calculations here.")
    
    st.header("Basic Drilling Parameters")
    depth = st.number_input("Total Depth (m/ft):", min_value=0.0, value=1000.0)
    mud_weight = st.number_input("Mud Weight (PPG / SG):", min_value=0.0, value=9.5)
    
    if st.button("Calculate"):
        st.success(f"Data saved: Depth {depth} and Mud Weight {mud_weight}")
import streamlit as st

# 1. إعدادات الصفحة - تم إغلاق القوس بشكل صحيح
st.set_page_config(
    page_title="Drilling App",
    page_icon="🛢️",
    layout="wide"
)

# 2. تخصيص المظهر باللون الأزرق
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f4f8;
    }
    [data-testid="stSidebar"] {
        background-color: #1e3a8a;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    h1, h2, h3 {
        color: #1d4ed8;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 3. اختيار اللغة
st.sidebar.title("Settings / إعدادات")
language = st.sidebar.radio("Choose Language / اختر اللغة:", ("العربية", "English"))

# 4. واجهة التطبيق
if language == "العربية":
    st.title("🛢️ تطبيق حسابات الحفر")
    st.write("أهلاً بك! يمكنك استخدام الأدوات والحسابات الهندسية الخاصة بالحفر هنا.")
    
    st.header("بيانات الحفر الأساسية")
    depth = st.number_input("العمق الكلي (متر/قدم):", min_value=0.0, value=1000.0)
    mud_weight = st.number_input("كثافة الطين (PPG / SG):", min_value=0.0, value=9.5)
    
    if st.button("حساب"):
        st.success(f"تم تسجيل البيانات: العمق {depth} والكثافة {mud_weight}")

else:
    st.title("🛢️ Drilling Operations App")
    st.write("Welcome! You can use drilling engineering tools and calculations here.")
    
    st.header("Basic Drilling Parameters")
    depth = st.number_input("Total Depth (m/ft):", min_value=0.0, value=1000.0)
    mud_weight = st.number_input("Mud Weight (PPG / SG):", min_value=0.0, value=9.5)
    
    if st.button("Calculate"):
        st.success(f"Data saved: Depth {depth} and Mud Weight {mud_weight}")
