
import streamlit as st
import pandas as pd

# قراءة الملف
df = pd.read_excel("المرحلة الثالثة.xlsx", sheet_name="Sheet1")

# حذف الأعمدة الفارغة
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# إعداد الواجهة
st.set_page_config(page_title="درجات الطلبة", layout="centered")
st.title("🔍 عرض درجات الطالب")
st.markdown("يرجى اختيار اسمك من القائمة لعرض درجاتك بالتفصيل")

# قائمة الأسماء
names = df["الاسم"].dropna().unique()
selected_name = st.selectbox("اختر اسمك:", names)

# عرض التفاصيل
if selected_name:
    student_data = df[df["الاسم"] == selected_name]
    st.subheader(f"📄 تفاصيل الدرجات لـ: {selected_name}")
    st.table(student_data.transpose())
