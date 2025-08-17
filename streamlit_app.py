# streamlit_app.py

import streamlit as st
import pickle
import numpy as np

# إعداد صفحة Streamlit
st.set_page_config(
    page_title="توقع إجمالي الطلب",
    page_icon="🔮",
    layout="centered"
)

# تحميل الموديل
with open(r"E:\Projects\python\Customer_Data_Analysis\model.pkl", 'rb') as f:
    model = pickle.load(f)

# تنسيق CSS مخصص لتجميل المظهر
st.markdown("""
    <style>
        .main {
            background-color: #F0F2F6;
        }
        .stApp {
            font-family: 'Segoe UI', sans-serif;
            color: #2E2E2E;
        }
        .title {
            text-align: center;
            font-size: 36px;
            color: #4A90E2;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #4A90E2;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #4078c0;
        }
    </style>
""", unsafe_allow_html=True)

# عنوان الصفحة
st.markdown('<div class="title">🧠 توقع إجمالي الطلب</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ادخل بيانات المنتج، وسيقوم النظام بتوقع إجمالي السعر المتوقع بدقة باستخدام نموذج تعلم آلي.</div>', unsafe_allow_html=True)

# إدخال بيانات المستخدم بتقسيم أفقي
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("📦 وزن المنتج (kg)", min_value=0.0, max_value=100.0, value=1.0)
with col2:
    base_price = st.number_input("💲 سعر المنتج الأساسي", min_value=0.0, max_value=10000.0, value=100.0)

item_count = st.slider("🧮 عدد العناصر في الطلب", min_value=1, max_value=1000, value=1)

# توقع السعر
if st.button("✨ توقع السعر"):
    input_data = np.array([[weight, base_price, item_count]])
    prediction = model.predict(input_data)
    st.success(f"✅ إجمالي السعر المتوقع: {prediction[0]:,.2f} جنيه")

# Footer بسيط
st.markdown("""<hr style="margin-top: 40px;"/>
    <div style='text-align: center; color: #aaa; font-size: 14px;'>
    تم التنفيذ بواسطة <b>MHMD</b> · باستخدام <b>Streamlit</b> و <b>Scikit-learn</b>
    </div>
""", unsafe_allow_html=True)
