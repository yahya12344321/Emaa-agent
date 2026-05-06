import streamlit as st
import os

# إعدادات الواجهة
st.set_page_config(page_title="Emaa Agent - Production", layout="wide")

# رابط الملف الرئيسي
# ملاحظة: Streamlit يخدم الملفات من مجلد static تلقائياً إذا تم إعداده كـ Symlink
# ولكن للسرعة الآن سنقوم بحقن الكود مع تصحيح المسار
static_index = os.path.join("static", "index.html")

if os.path.exists(static_index):
    with open(static_index, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # تصحيح المسارات برمجياً لتعمل داخل Streamlit
    # هذا يضمن أن يقرأ المتصفح ملفات CSS و JS الخاصة بيحيى
    corrected_html = html_content.replace('href="', 'href="static/').replace('src="', 'src="static/')
    # إعادة تصحيح الاستثناءات (مثل الروابط الخارجية)
    corrected_html = corrected_html.replace('static/http', 'http')
    
    st.components.v1.html(corrected_html, height=1200, scrolling=True)
else:
    st.error("تنبيه المهندس: ملف index.html غير موجود في مسار static")
