# predict_2026_fixed.py  (ye 100% chalega)
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# 1. Data load
df = pd.read_csv('govt_jobs_2015_2025.csv')

# 2. Exam ko number mein convert (ek hi encoder use kar rahe hain)
le = LabelEncoder()
df['exam_code'] = le.fit_transform(df['exam'])

# 3. Features aur target
X = df[['exam_code', 'year']]
y = df['vacancies']

# 4. Sabse best model (Random Forest)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X.values, y)    # <-- .values add kiya

# 5. 2026 ki predictions
print("="*55)
print("        BHARATNAUKRI AI – 2026 PREDICTIONS")
print("="*55)

exams_to_predict = ['SSC CGL', 'UPSC CSE', 'IBPS PO', 'RRB NTPC', 'SBI PO', 'CTET', 'RRB Group D', 'IBPS Clerk']

for exam in exams_to_predict:
    try:
        code = le.transform([exam])[0]
        pred = model.predict([[code, 2026]])[0]
        print(f"{exam:20} → {int(pred):,} vacancies")
    except:
        print(f"{exam:20} → Data nahi hai")

print("="*55)
print("Project complete bhai! Ab Streamlit app bana denge")