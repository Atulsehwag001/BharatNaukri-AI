import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import numpy as np
import streamlit as st

# Google Tag Manager (GSC verify ke liye)
st.markdown('''
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-SDLC4KF3');</script>
<!-- End Google Tag Manager -->
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-SDLC4KF3"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
''', unsafe_allow_html=True)
st.set_page_config(page_title="BharatNaukri AI Pro - 2026-2030", page_icon="India")

st.title("भारतनौकरी AI Pro")
st.markdown("**SSC | UPSC | Railway | Bank | Defence | State PSC – 100% AI Prediction**")

# Historical data (real past trends se banaya gaya model)
data = {
    "Exam": ["SSC CGL", "SSC CHSL", "SSC GD", "UPSC CSE", "IBPS PO", "RRB NTPC", "UPPSC PCS", "SBI PO", "Railway Group D", "Defence Agniveer"],
    "Year": [2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024],
    "Vacancies": [17000, 3700, 40000, 1056, 3000, 35000, 600, 2000, 32000, 45000],
    "Notification_Month": [6, 3, 2, 1, 8, 9, 3, 9, 12, 5],
    "Fee_General": [100, 100, 100, 100, 850, 500, 125, 750, 500, 250],
    "Competition_Level": [9, 7, 10, 10, 8, 9, 8, 7, 10, 9]
}
df = pd.DataFrame(data)

# Training simple AI model
le = LabelEncoder()
df["Exam_Encoded"] = le.fit_transform(df["Exam"])

X = df[["Exam_Encoded", "Year", "Competition_Level"]]
y_vac = df["Vacancies"]
y_month = df["Notification_Month"]
y_fee = df["Fee_General"]

model_vac = RandomForestRegressor(n_estimators=100, random_state=42)
model_month = RandomForestRegressor(n_estimators=100, random_state=42)
model_fee = RandomForestRegressor(n_estimators=100, random_state=42)

model_vac.fit(X, y_vac)
model_month.fit(X, y_month)
model_fee.fit(X, y_fee)

# All exams list
all_exams = ["SSC CGL","SSC CHSL","SSC GD","SSC MTS","UPSC CSE","UPSC CAPF","IBPS PO","IBPS Clerk","SBI PO","RRB NTPC","Railway Group D","UPPSC PCS","BPSC","MPPSC","RPSC RAS","Delhi Police","Army Agniveer","Air Force","Navy SSR","CTET","KVS","NVS","REET","Bihar SI","UP Police SI"]

exam = st.selectbox("Exam चुनो या खुद लिखो", [""] + all_exams)
if not exam:
    exam = st.text_input("Exam का नाम लिखो (जैसे SSC CGL 2027)").upper()

year = st.selectbox("Year", [2026, 2027, 2028, 2029, 2030])
category = st.selectbox("Category", ["General", "OBC", "SC", "ST", "EWS"])

if st.button("AI Prediction दो", type="primary"):
    if not exam.strip():
        st.error("Exam name daal do bhai!")
    else:
        # Agar exam list mein nahi toh closest match assume kar lenge
        if exam not in le.classes_:
            exam_code = 0  # default SSC CGL jaisa treat karo
        else:
            exam_code = le.transform([exam])[0]

        # Prediction
        pred_vac = int(model_vac.predict([[exam_code, year, 9]])[0])
        pred_month = int(model_month.predict([[exam_code, year, 9]])[0])
        pred_fee = int(model_fee.predict([[exam_code, year, 9]])[0])

        # Realistic range
        vac_range = f"{int(pred_vac*0.8):,} - {int(pred_vac*1.4):,}+"

        month_names = ["", "January", "February", "March", "April", "May", "June", 
                       "July", "August", "September", "October", "November", "December"]
        notif_month = month_names[pred_month] if 1 <= pred_month <= 12 else "Mar-Jun"

        st.balloons()
        st.success(f"**{exam} {year} – AI Prediction Ready!**")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Vacancies", vac_range)
        c2.metric("Notification", notif_month)
        c3.metric("Form Last Date", "1-2 महीने बाद")
        c4.metric("Fee (General)", f"₹{pred_fee}")

        st.info(f"Age, syllabus, selection process – sab official notification ke saath update ho jayega!")

# Footer
st.markdown("---")
st.markdown("**Made with ❤️ & ML by Atul Sehwag**")
st.markdown("Instagram: @atul.sehwag | Ab har sarkari job ki prediction ek click mein!")



