import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="Stuck Pipe Predictor",
    page_icon="🛢️",
    layout="wide"
)

# 2. تخصيص المظهر باللون الأزرق
st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
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
        width: 100%;
        padding: 10px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 3. اختيار اللغة في الشريط الجانبي
language = st.sidebar.radio("Language / اللغة", ["العربية", "English"], key="lang_radio")

# 4. واجهة التطبيق
if language == "العربية":
    st.title("🛢️ برنامج التنبؤ باستعصاء أنابيب الحفر")
    st.write("أدخل معاملات الحفر لتحليل مخاطر استعصاء الانابيب (Stuck Pipe Risks).")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("بيانات السائل والعمق")
        depth = st.number_input("العمق (ft):", min_value=0.0, value=8000.0, key="txt_depth_ar")
        mud_weight = st.number_input("كثافة الطين (ppg):", min_value=0.0, value=10.5, key="txt_mw_ar")
        viscosity = st.number_input("اللزوجة (sec/qt):", min_value=0.0, value=45.0, key="txt_visc_ar")
        flow_rate = st.number_input("معدل الضخ (GPM):", min_value=0.0, value=500.0, key="txt_flow_ar")

    with col2:
        st.subheader("المعاملات الميكانيكية")
        rop = st.number_input("معدل الاختراق (ft/hr):", min_value=0.0, value=35.0, key="txt_rop_ar")
        wob = st.number_input("الوزن على الدقاقة (klbs):", min_value=0.0, value=20.0, key="txt_wob_ar")
        rpm = st.number_input("سرعة الدوران (RPM):", min_value=0.0, value=120.0, key="txt_rpm_ar")
        torque = st.number_input("العزم (ft-lbs):", min_value=0.0, value=12000.0, key="txt_tq_ar")

    st.markdown("---")
    if st.button("تحليل مخاطر الاستعصاء", key="btn_calc_ar"):
        risk = 0
        reasons = []
        if mud_weight > 12.0 and flow_rate < 400:
            risk += 40
            reasons.append("خطر استعصاء تفاضلي (Differential Sticking) بسبب ارتفاع كثافة الطين وانخفاض الضخ.")
        if rop > 50 and flow_rate < 450:
            risk += 40
            reasons.append("خطر تراكم نواتج الحفر (Cuttings Accumulation) لضعف تنظيف التجويف.")
        if torque > 15000:
            risk += 20
            reasons.append("ارتفاع كبير في العزم (High Torque).")

        if risk == 0:
            st.success("✅ **المخاطر منخفضة:** المعاملات تشير إلى ظروف حفر آمنة.")
        elif risk < 50:
            st.warning(f"⚠️ **المخاطر متوسطة ({risk}%):** انتبه للنقاط التالية:")
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.error(f"🚨 **المخاطر عالية جداً ({risk}%):** يجب مراجعة المعاملات:")
            for r in reasons:
                st.write(f"- {r}")

else:
    st.title("🛢️ Stuck Pipe Prediction System")
    st.write("Enter drilling parameters to assess stuck pipe risk levels.")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Mud & Well Parameters")
        depth = st.number_input("Depth (ft):", min_value=0.0, value=8000.0, key="txt_depth_en")
        mud_weight = st.number_input("Mud Weight (ppg):", min_value=0.0, value=10.5, key="txt_mw_en")
        viscosity = st.number_input("Funnel Viscosity (sec/qt):", min_value=0.0, value=45.0, key="txt_visc_en")
        flow_rate = st.number_input("Flow Rate (GPM):", min_value=0.0, value=500.0, key="txt_flow_en")

    with col2:
        st.subheader("Mechanical Parameters")
        rop = st.number_input("ROP (ft/hr):", min_value=0.0, value=35.0, key="txt_rop_en")
        wob = st.number_input("WOB (klbs):", min_value=0.0, value=20.0, key="txt_wob_en")
        rpm = st.number_input("RPM:", min_value=0.0, value=120.0, key="txt_rpm_en")
        torque = st.number_input("Torque (ft-lbs):", min_value=0.0, value=12000.0, key="txt_tq_en")

    st.markdown("---")
    if st.button("Analyze Stuck Pipe Risk", key="btn_calc_en"):
        risk = 0
        reasons = []
        if mud_weight > 12.0 and flow_rate < 400:
            risk += 40
            reasons.append("High Differential Sticking risk (High MW & Low Flow Rate).")
        if rop > 50 and flow_rate < 450:
            risk += 40
            reasons.append("Cuttings Accumulation risk (High ROP & Insufficient hole cleaning).")
        if torque > 15000:
            risk += 20
            reasons.append("High Torque detected.")

        if risk == 0:
            st.success("✅ **Low Risk:** Drilling parameters are within safe limits.")
        elif risk < 50:
            st.warning(f"⚠️ **Medium Risk ({risk}%):** Pay attention to:")
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.error(f"🚨 **High Stuck Pipe Risk ({risk}%):** Action required:")
            for r in reasons:
                st.write(f"- {r}")
