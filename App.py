
import streamlit as st

# إعداد الصفحة لازم يكون أول أمر برمجي بعد الاستيراد
st.set_page_config(page_title="Tufting Design Studio", layout="wide")

st.title("Tufting Design Studio 3.0 🧶")
st.write("مرحباً بك يا بشمهندس في نظام تصميم التفتنج الذكي")

# هنا بنضيف باقي الخصائص اللي شغالين عليها
option = st.selectbox(
    'اختر نوع الماكينة:',
    ('4-Axis Tufting Machine', 'Carpet Finishing', 'Industrial Compressor'))

st.write(f'تم اختيار: {option}')

# زر تجريبي للتأكد من عمل التطبيق
if st.button('بدء المعالجة'):
    st.success('جاري تجهيز بيئة العمل...')
