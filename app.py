# app.py — FINAL BHARATNAUKRI AI (30+ Exams + Dates + Fees + Vacancies)
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="BharatNaukri AI", page_icon="India")
st.title("India BharatNaukri AI - 2026-2030")
st.markdown("**Vacancies + Notification Month + Form Last Date + Fees — Sab AI bataayega!**")

# Load your CSV
df = pd.read_csv("govt_jobs_2015_2025.csv")

# FULL EXAM LIST with real details (2026-27 ke hisab se)
exam_details = {
    "SSC CGL":          {"notif": "June",       "duration": "30-45 days", "fee": "₹100",      "exam": "Sep-Oct"},
    "SSC CHSL":         {"notif": "April",      "duration": "30 days",    "fee": "₹100",      "exam": "Jul-Aug"},
    "SSC MTS":          {"notif": "July",       "duration": "30 days",    "fee": "₹100",      "exam": "Oct-Nov"},
    "SSC GD":           {"notif": "Aug-Sep",    "duration": "30-40 days", "fee": "₹100",      "exam": "Jan-Feb"},
    "UPSC CSE":         {"notif": "Jan",        "duration": "20 days",    "fee": "₹100",      "exam": "May (Pre)"},
    "IBPS PO":          {"notif": "August",     "duration": "30 days",    "fee": "₹850",      "exam": "Oct (Pre)"},
    "IBPS Clerk":       {"notif": "July",       "duration": "30 days",    "fee": "₹850",      "exam": "Aug-Sep"},
    "SBI PO":           {"notif": "Dec-Jan",    "duration": "25 days",    "fee": "₹750",      "exam": "Jul-Aug"},
    "SBI Clerk":        {"notif": "Nov-Dec",    "duration": "25 days",    "fee": "₹750",      "exam": "Feb-Mar"},
    "RRB NTPC":         {"notif": "Oct",        "duration": "35 days",    "fee": "₹500",      "exam": "Dec-Jan"},
    "RRB Group D":      {"notif": "Nov-Dec",    "duration": "40 days",    "fee": "₹500",      "exam": "Mar-Apr"},
    "Delhi Police Constable": {"notif": "Sep",  "duration": "30 days",    "fee": "₹100",      "exam": "Dec"},
    "UP Police Constable":   {"notif": "Dec-Jan","duration": "40 days",    "fee": "₹400",      "exam": "Mar-Apr"},
    "Haryana Police Constable": {"notif": "Oct-Nov", "duration": "30 days", "fee": "₹100",   "exam": "Jan"},
    "Bihar Police SI":  {"notif": "Oct",        "duration": "30 days",    "fee": "₹700",      "exam": "Feb-Mar"},
    "CTET":             {"notif": "Oct & Apr",  "duration": "30 days",    "fee": "₹1000",     "exam": "Jan & Jul"},
    "DSSSB TGT/PRT":    {"notif": "Feb-Mar",    "duration": "30 days",    "fee": "₹100",      "exam": "May-Jun"},
    "Indian Army GD":   {"notif": "Feb & Aug",  "duration": "30 days",    "fee": "Free",      "exam": "Apr & Oct"},
    "Indian Navy SSR":  {"notif": "May & Nov",  "duration": "20 days",    "fee": "Free",      "exam": "Jul & Jan"},
    "Air Force X/Y":    {"notif": "Jan & Jul",  "duration": "25 days",    "fee": "₹250",      "exam": "Mar & Sep"}
}

# Train model
le = LabelEncoder()
df['exam_code'] = le.fit_transform(df['exam'])
X = df[['exam_code', 'year']]
y = df['vacancies']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X.values, y)

# User select
exam = st.selectbox("Exam Select Karo", sorted(exam_details.keys()))
year = st.slider("Year", 2026, 2030, 2026)

# Prediction
code = le.transform([exam])[0] if exam in le.classes_ else 0
pred = model.predict([[code, year]])[0]
d = exam_details[exam]

# Beautiful output
st.success(f"**{exam} {year}**")
col1, col2 = st.columns(2)
with col1:
    st.metric("Expected Vacancies", f"{int(pred):,}")
    st.metric("Notification Month", d['notif'])
with col2:
    st.metric("Form Bharega", d['duration'])
    st.metric("Application Fee (Gen)", d['fee'])

st.info(f"Exam kab hoga → **{d['exam']}**\n\nSC/ST/PwD/Women usually free ya ₹250-400 tak. Official notification aane ke baad confirm kar lena!")

st.balloons()
st.markdown("---")
st.markdown("**Made with ❤️ & 🇮🇳 by Atul Sehwag**")
st.markdown("Instagram: @atul.sehwag | Share karo sabko!")


