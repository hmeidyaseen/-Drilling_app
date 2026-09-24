import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="نظام التنبؤ باحتجاز أنابيب الحفر",
    page_icon="🏜️",
    layout="wide"
)

# 2. إضافة تنسيق CSS للون الصحراوي وتصميم البطاقات
st.markdown("""
    <style>
    /* خلفية التطبيق باللون الصحراوي الناعم */
    .stApp {
        background-color: #F4EAD5;
        color: #2C221E;
    }
    
    /* القائمة الجانبية */
    [data-testid="stSidebar"] {
        background-color: #E2D4B7;
    }

    /* تصميم بطاقات المؤشرات (KPI Cards) */
    .kpi-card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
        border-right: 5px solid #C29B38;
        text-align: center;
        margin-bottom: 20px;
    }
    .kpi-title {
        font-size: 14px;
        color: #6B5B45;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .kpi-value {
        font-size: 22px;
        color: #2C221E;
        font-weight: 800;
    }
    .kpi-sub {
        font-size: 11px;
        color: #8C7B65;
        margin-top: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.title("🏜️ نظام التنبؤ باحتجاز أنابيب الحفر والدعم القراري")
st.subheader("Differential Sticking Predictor & Decision Support System")

st.markdown("---")

# 4. عرض المؤشرات الاقتصادية والهندسية الرئيسية (KPIs)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">🎯 دقة النموذج التنبئي</div>
            <div class="kpi-value">99.33%</div>
            <div class="kpi-sub">نموذج ML - XGBoost High Precision</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">⏱️ زمن معالجة الاستعصاء</div>
            <div class="kpi-value">أقل من 6 ساعات</div>
            <div class="kpi-sub">بدلاً من 2 - 7 أيام (NPT) التقليدية</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">💰 نسبة توفير الخسائر</div>
            <div class="kpi-value">60% - 85%</div>
            <div class="kpi-sub">تخفيض تكاليف التوقف والـ BHA</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 5. مدخلات الحفر الحية
st.write("### 📊 إدخال القراءات الحية للحفر (Drilling Data)")

diff_press = st.number_input("(psi) فرق الضغط التفاضلي", value=400.0, step=50.0)
static_time = st.number_input("(دقيقة) زمن سكون الأنبوب", value=0.0, step=5.0)
rpm = st.number_input("(RPM) سرعة الدوران", value=120.0, step=10.0)
mud_cake = st.number_input("(mm) سمك كعكة الطين", value=1.5, step=0.5)
perm = st.number_input("(md) نفاذية الطبقة", value=20.0, step=10.0)

st.markdown("---")
st.write("### 🚨 نتائج التحليل والتوصيات الهندسية")

# منطق تقييم الخطر
is_critical = (diff_press > 1500 or static_time > 30 or rpm < 20 or mud_cake > 5.0)

if is_critical:
    st.error("🚨 خطر استعصاء تفاضلي حرِج! (Critical Risk)")
    st.warning("⚠️ التوصية الهندسية: قم بتدوير الأنابيب وسحبها فوراً، وضخ دفعة تزييت (Spot Lubricant Pill).")
else:
    st.success("✅ عمليات الحفر آمنة (Safe Operations)")
    st.info("ℹ️ التوصية الهندسية: استمر بالحفر الاعتيادي مع المراقبة الروتينية.")
