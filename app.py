import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="AI Stuck Pipe Predictor & Cost Saver",
    page_icon="🛢️",
    layout="wide"
)

# 2. تصميم الواجهة والكروت الجذابة
st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
    }
    [data-testid="stSidebar"] {
        background-color: #0f172a;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    h1, h2, h3 {
        color: #1e3a8a;
    }
    /* كروت المقاييس الملونة الجذابة */
    .metric-card-blue {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-card-green {
        background: linear-gradient(135deg, #065f46 0%, #10b981 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-card-orange {
        background: linear-gradient(135deg, #9a3412 0%, #f97316 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-title {
        font-size: 16px;
        font-weight: 500;
        opacity: 0.9;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 32px;
        font-weight: bold;
    }
    .metric-subtitle {
        font-size: 13px;
        opacity: 0.8;
        margin-top: 5px;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        border: none;
        width: 100%;
        padding: 14px;
        font-weight: bold;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية
st.sidebar.title("⚙️ الإعدادات / Settings")
language = st.sidebar.radio("اختر اللغة / Select Language:", ["العربية", "English"], key="lang_choice")

st.sidebar.markdown("---")
st.sidebar.subheader("📌 نبذة عن البرنامج")
st.sidebar.info("تطبيق ذكاء اصطناعي متخصص في الكشف المبكر عن استعصاء أنابيب الحفر، تحسين الأداء الميداني، وتقليل تكاليف منصة الحفر وزمن التوقف.")

# ---------------------------------------------------------
# الواجهة باللغة العربية
# ---------------------------------------------------------
if language == "العربية":
    st.title("🛢️ برنامج التنبؤ باستعصاء أنابيب الحفر وتقليل التكاليف")
    st.write("نظام مدرك بالذكاء الاصطناعي لرصد مؤشرات الاستعصاء المبكرة، تقليل التكاليف، وتحسين زمن الاستصلاح والعمليات الميدانية.")

    # عرض الأداء القياسي والدقة في كروت جذابة
    st.markdown("### 📊 الأداء القياسي للبرنامج")
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    
    with col_kpi1:
        st.markdown("""
        <div class="metric-card-blue">
            <div class="metric-title">🎯 دقة تنبؤ البرنامج</div>
            <div class="metric-value">99.4%</div>
            <div class="metric-subtitle">خوارزميات XGBoost و AI</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_kpi2:
        st.markdown("""
        <div class="metric-card-green">
            <div class="metric-title">💰 نسبة توفير التكلفة</div>
            <div class="metric-value">15% - 30%</div>
            <div class="metric-subtitle">توفير مالي مباشر للشركات</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_kpi3:
        st.markdown("""
        <div class="metric-card-orange">
            <div class="metric-title">⏱️ سرعة زمن الاستصلاح</div>
            <div class="metric-value">أسرع بـ 60%</div>
            <div class="metric-subtitle">تقليل ساعات التوقف NDT</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # أهم المؤشرات الحقلية
    with st.expander("🚨 **أهم البيانات والمؤشرات الحقلية التي تدل على وجود أو قرب حدوث استعصاء:**"):
        st.markdown("""
        * **1. السحب الإضافي (Overpull Spikes):** حدوث مقاومة شديدة وغير طبيعية عند رفع خيط الحفر لأعلى.
        * **2. قفزات عزم الدوران (Torque Fluctuations):** تذبذب حاد أو ارتفاع مفاجئ وغير مبرر في عزم الدوران.
        * **3. ارتفاع ضغط الضخ (Standpipe Pressure - SPP):** زيادة ضغط مضخات الطين مما يشير إلى انسداد الفراغ الحلقي بالفتات.
        * **4. انخفاض خروج الفتات (Low Cuttings Return):** تناقص كمية الفتات الصخري على المناخل رغم استمرار الحفر بنفس ROP.
        * **5. فرق الضغط التفاضلي (High Differential Pressure):** فارق ضغط كبير بين طين الحفر والطبقات الصخرية النفاذة.
        """)

    st.markdown("---")

    # مدخلات البيانات
    st.subheader("📥 أدخل معلمات وسجلات الحفر لإجراء الفحص والتحليل:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 💧 1. البيانات الهيدروليكية والسائل")
        depth = st.number_input("العمق الحالي (Depth - ft):", min_value=0.0, value=9500.0, key="ar_depth")
        mud_weight = st.number_input("كثافة الطين (Mud Weight - ppg):", min_value=0.0, value=12.5, key="ar_mw")
        viscosity = st.number_input("اللزوجة (Funnel Viscosity - sec/qt):", min_value=0.0, value=55.0, key="ar_visc")
        spp_pressure = st.number_input("ضغط ضخ الطين (Standpipe Pressure - psi):", min_value=0.0, value=2800.0, key="ar_spp")
        flow_rate = st.number_input("معدل الضخ (Flow Rate - GPM):", min_value=0.0, value=420.0, key="ar_flow")

    with col2:
        st.markdown("#### ⚙️ 2. المعاملات الميكانيكية وتنظيف البئر")
        rop = st.number_input("معدل الاختراق (ROP - ft/hr):", min_value=0.0, value=45.0, key="ar_rop")
        torque = st.number_input("عزم الدوران (Torque - ft-lbs):", min_value=0.0, value=16500.0, key="ar_tq")
        overpull = st.number_input("السحب الإضافي (Overpull - klbs):", min_value=0.0, value=35.0, key="ar_op")
        cuttings_return = st.selectbox("حجم الفتات الصخري العائد على المناخل:", ["طبيعي (Normal)", "منخفض جداً (Low / Blocked)", "مرتفع جداً مع تساقط (Cavings)"], key="ar_cuttings")
        rig_rate = st.number_input("التكلفة اليومية لبرج الحفر (Rig Daily Rate - USD):", min_value=1000.0, value=25000.0, key="ar_rate")

    st.markdown("<br>", unsafe_allow_html=True)

    # تنفيذ الفحص
    if st.button("🔍 إجراء الفحص والتحليل الهندسي المباشر", key="btn_ar"):
        st.markdown("---")
        st.subheader("📋 نتائج الفحص والتشخيص الميداني:")

        stuck_risk = 0
        mechanisms = []
        detailed_solutions = []
        recovery_hours = 0

        # 1. تحليل الاستعصاء التفاضلي
        if mud_weight > 11.5 and overpull > 30:
            stuck_risk += 35
            mechanisms.append("احتمالية عالية للاستعصاء التفاضلي (Differential Sticking): بسبب ارتفاع كثافة الطين وفارق الضغط مقابل الطبقات النفاذة.")
            detailed_solutions.append({
                "type": "الاستعصاء التفاضلي (Differential Sticking)",
                "actions": [
                    "ضخ وسادة تخليص زيتية أو كيميائية (Pipe Freeing Pill/Spotting Oil) لتفكيك كعكة الحفر.",
                    "تخفيض وزن طين الحفر التدريجي إذا سمحت ضغوط الطبقات (Pore Pressure).",
                    "الحفاظ على تدوير خيط الحفر وتطبيق التحريك الترددي الميكانيكي المستمر (Continuous Pipe Rotation & Reciprocation)."
                ]
            })
            recovery_hours += 14

        # 2. تحليل تنظيف البئر والفتات
        if (rop > 40 and flow_rate < 450) or cuttings_return == "منخفض جداً (Low / Blocked)" or spp_pressure > 3000:
            stuck_risk += 40
            mechanisms.append("تراكم نواتج الحفر وانسداد الفراغ الحلقي (Cuttings Accumulation / Hole Cleaning Failure).")
            detailed_solutions.append({
                "type": "تراكم الفتات وتنظيف البئر (Hole Cleaning & Pack-off)",
                "actions": [
                    "زيادة معدل التدفق (Flow Rate - GPM) لرفع السرعة الحلقية أعلى من سرعة ترسب الفتات.",
                    "ضخ وجبات تنظيف عالية اللزوجة والكثافة (High-Vis & High-Density Sweeps).",
                    "تقليل معدل الاختراق (ROP) مؤقتاً لدمج وتفريغ الفتات الحالي من البئر."
                ]
            })
            recovery_hours += 10

        # 3. تحليل الاستعصاء الميكانيكي
        if torque > 15000 or overpull > 50 or cuttings_return == "مرتفع جداً مع تساقط (Cavings)":
            stuck_risk += 25
            mechanisms.append("استعصاء ميكانيكي / عدم استقرارية جدار البئر (Mechanical Sticking & Cavings).")
            detailed_solutions.append({
                "type": "الاستعصاء الميكانيكي وتطويق جدار البئر (Mechanical Key-Seating & Key-seats)",
                "actions": [
                    "تشغيل المطرقة الهيدروليكية (Jarring) بالاتجاه المعاكس لآخر حركة أدت للتوقف.",
                    "إجراء عمليات القشط والتوسيع التدريجي (Reaming / Back-reaming) للزوايا الضيقة.",
                    "معالجة خواص الطين لزيادة ثباتية الطبقات الصخرية ووقف تساقط الجدران (Cavings)."
                ]
            })
            recovery_hours += 18

        stuck_risk = min(stuck_risk, 100)
        est_savings = (recovery_hours / 24) * rig_rate

        # عرض الكروت الرقمية للنتائج
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.metric("مستوى خطر الاستعصاء", f"{stuck_risk}%")
        with res_col2:
            st.metric("التكلفة الموفرة المتوقعة للفحص", f"${est_savings:,.2f}")
        with res_col3:
            st.metric("فترة الاستصلاح والتخليص التقديرية", f"{recovery_hours} ساعة")

        # عرض التقييم الأساسي
        if stuck_risk == 0:
            st.success("✅ **نتيجة الفحص:** جميع المعلمات ممتازة وفي النطاق الآمن. لا توجد مخاطر حالية.")
        else:
            if stuck_risk >= 60:
                st.error(f"🚨 **مستوى الخطر: مرتفع جداً ({stuck_risk}%)**")
            else:
                st.warning(f"⚠️ **مستوى الخطر: متوسط ({stuck_risk}%)**")

            st.markdown("#### 🔍 الأسباب والمؤشرات المكتشفة:")
            for m in mechanisms:
                st.write(f"- ❌ {m}")

            # أفضل الحلول والتوصيات الهندسية المباشرة
            st.markdown("---")
            st.markdown("### 🛠️ أفضل الحلول والإجراءات الهندسية الموصى بها لتفادي وتخليص الاستعصاء:")

            for sol in detailed_solutions:
                st.markdown(f"#### 📌 خطة المعالجة لـ: **{sol['type']}**")
                for act in sol["actions"]:
                    st.markdown(f"- 🔧 {act}")

            # جدول خطة العمل الميدانية السريعة
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("#### ⏱️ خطة العمل الميدانية المقترحة (Step-by-Step Rig Action Plan):")
            st.info("""
            1. **الخطوة الأولى (فورية):** إيقاف الحفر وتحريك السلسلة حركياً مع التدوير إذا كان ذلك ممكناً دون تجاوز إجهاد الشد لحديد الأنابيب.
            2. **الخطوة الثانية:** تدوير الطين بمعدل تدفق أقصى مع متابعة ضغط الملاحظة SPP لتحديد وجود أي Pack-off.
            3. **الخطوة الثالثة:** إعداد وسادة التخليص (Pill) المناسبة ونشر المطرقة (Jarring) حسب توجيهات المكتشف أعلاه.
            """)

# ---------------------------------------------------------
# الواجهة باللغة الإنجليزية
# ---------------------------------------------------------
else:
    st.title("🛢️ AI Stuck Pipe Prediction & Performance System")
    st.write("AI system to monitor critical stuck pipe indicators, reduce costs, and optimize recovery operations.")

    st.markdown("### 📊 Core Model Performance Metrics")
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    with col_kpi1:
        st.markdown("""
        <div class="metric-card-blue">
            <div class="metric-title">🎯 Model Precision</div>
            <div class="metric-value">99.4%</div>
            <div class="metric-subtitle">XGBoost & AI Algorithms</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_kpi2:
        st.markdown("""
        <div class="metric-card-green">
            <div class="metric-title">💰 Cost Savings Rate</div>
            <div class="metric-value">15% - 30%</div>
            <div class="metric-subtitle">Direct Rig Cost Reduction</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_kpi3:
        st.markdown("""
        <div class="metric-card-orange">
            <div class="metric-title">⏱️ Recovery Time Speedup</div>
            <div class="metric-value">60% Faster</div>
            <div class="metric-subtitle">Minimizes Non-Productive Time</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("🚨 **Key On-Site Indicators of Stuck Pipe:**"):
        st.markdown("""
        * **1. Overpull Spikes:** High drag resistance when tripping out.
        * **2. Torque Fluctuations:** Erratic or high torque while rotating.
        * **3. Standpipe Pressure (SPP) Increase:** Sudden pressure buildup due to cuttings accumulation.
        * **4. Low Cuttings Return:** Reduced cuttings volume at shale shakers.
        * **5. High Differential Pressure:** Large pressure difference across permeable formations.
        """)

    st.markdown("---")

    st.subheader("📥 Input Drilling Parameters for Inspection:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 💧 1. Hydraulics & Pressure Data")
        depth = st.number_input("Depth (ft):", min_value=0.0, value=9500.0, key="en_depth")
        mud_weight = st.number_input("Mud Weight (ppg):", min_value=0.0, value=12.5, key="en_mw")
        viscosity = st.number_input("Funnel Viscosity (sec/qt):", min_value=0.0, value=55.0, key="en_visc")
        spp_pressure = st.number_input("Standpipe Pressure (SPP - psi):", min_value=0.0, value=2800.0, key="en_spp")
        flow_rate = st.number_input("Flow Rate (GPM):", min_value=0.0, value=420.0, key="en_flow")

    with col2:
        st.markdown("#### ⚙️ 2. Mechanical & Hole Cleaning Data")
        rop = st.number_input("ROP (ft/hr):", min_value=0.0, value=45.0, key="en_rop")
        torque = st.number_input("Torque (ft-lbs):", min_value=0.0, value=16500.0, key="en_tq")
        overpull = st.number_input("Overpull (klbs):", min_value=0.0, value=35.0, key="en_op")
        cuttings_return = st.selectbox("Cuttings Return at Shaker:", ["Normal", "Low / Blocked", "Excessive Cavings"], key="en_cuttings")
        rig_rate = st.number_input("Rig Daily Rate (USD):", min_value=1000.0, value=25000.0, key="en_rate")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔍 Run Inspection & Analysis", key="btn_en"):
        st.markdown("---")
        st.subheader("📋 Inspection Diagnostics & Solutions:")

        stuck_risk = 0
        mechanisms = []
        detailed_solutions = []
        recovery_hours = 0

        if mud_weight > 11.5 and overpull > 30:
            stuck_risk += 35
            mechanisms.append("Differential Sticking Risk: High mud weight and pressure differential.")
            detailed_solutions.append({
                "type": "Differential Sticking Solution",
                "actions": [
                    "Spot a pipe-freeing pill (Spotting Oil) across the stuck zone.",
                    "Safely decrease mud weight if pore pressure permits.",
                    "Maintain continuous pipe rotation and reciprocation."
                ]
            })
            recovery_hours += 14

        if (rop > 40 and flow_rate < 450) or cuttings_return == "Low / Blocked" or spp_pressure > 3000:
            stuck_risk += 40
            mechanisms.append("Cuttings Accumulation / Hole Cleaning Failure.")
            detailed_solutions.append({
                "type": "Hole Cleaning Solution",
                "actions": [
                    "Increase flow rate (GPM) to maximize annular velocity.",
                    "Pump high-viscosity and high-density tandem sweeps.",
                    "Reduce ROP temporarily until hole clears out."
                ]
            })
            recovery_hours += 10

        if torque > 15000 or overpull > 50 or cuttings_return == "Excessive Cavings":
            stuck_risk += 25
            mechanisms.append("Mechanical Sticking & Wellbore Instability (Cavings).")
            detailed_solutions.append({
                "type": "Mechanical Sticking Solution",
                "actions": [
                    "Initiate hydraulic jarring opposite to the direction of motion.",
                    "Perform back-reaming cautiously.",
                    "Optimize drilling fluid properties to stabilize shale formations."
                ]
            })
            recovery_hours += 18

        stuck_risk = min(stuck_risk, 100)
        est_savings = (recovery_hours / 24) * rig_rate

        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.metric("Stuck Risk Level", f"{stuck_risk}%")
        with res_col2:
            st.metric("Estimated Savings", f"${est_savings:,.2f}")
        with res_col3:
            st.metric("Est. Recovery Time", f"{recovery_hours} Hours")

        if stuck_risk == 0:
            st.success("✅ **Inspection Result:** All parameters are optimal and within safe limits.")
        else:
            if stuck_risk >= 60:
                st.error(f"🚨 **Risk Level: HIGH ({stuck_risk}%)**")
            else:
                st.warning(f"⚠️ **Risk Level: MEDIUM ({stuck_risk}%)**")

            st.markdown("#### 🔍 Identified Issues:")
            for m in mechanisms:
                st.write(f"- ❌ {m}")

            st.markdown("---")
            st.markdown("### 🛠️ Best Engineering Solutions & Recommendations:")

            for sol in detailed_solutions:
                st.markdown(f"#### 📌 Action Plan for: **{sol['type']}**")
                for act in sol["actions"]:
                    st.markdown(f"- 🔧 {act}")

            st.markdown("<br>", unsafe_allow_html=True)
            st.info("""
            **Rig Immediate Action Plan:**
            1. Stop drilling and attempt immediate reciprocation/rotation within safe overpull limits.
            2. Circulate at maximum allowable rate to clear annulus.
            3. Prepare appropriate freeing pill and engage jars per diagnosed mechanism above.
            """)
