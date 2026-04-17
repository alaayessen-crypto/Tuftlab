import streamlit as st

st.set_pag e_config(page_title="Stuff Lab", layout="centered")

st.title("مختبر الأشياء - Stuff Lab")
st.write("مرحباً بك في تطبيقك الجديد!")

# إضافة واجهة بسيطة
name = st.text_input("ما هو اسمك؟")
if st.button("تأكيد"):
    st.success(f"أهلاً بك يا {name} في Stuff Lab")
