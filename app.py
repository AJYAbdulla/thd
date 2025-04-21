
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

# محاولة إيجاد عمود يحتوي على كلمة "اسم"
name_column = next((col for col in df.columns if "اسم" in col), None)

if name_column:
    names = df[name_column].dropna().unique()
    selected_name = st.selectbox("اختر اسمك:", names)
    if selected_name:
        student_data = df[df[name_column] == selected_name]
        st.subheader(f"📄 تفاصيل الدرجات لـ: {selected_name}")
        st.table(student_data.transpose())
else:
    st.error("❌ لم يتم العثور على عمود يحتوي على أسماء الطلبة.")
