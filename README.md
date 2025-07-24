
# 🧠 Student Depression Checker

This is a **Streamlit-based web app** that predicts the risk of student depression using a trained **Logistic Regression model**. It considers several academic and lifestyle features such as CGPA, academic pressure, sleep, diet, financial stress, and more.

---

## 🧠 Model & Preprocessing

The logistic regression model was trained on the following features:
- Gender (Label encoded)
- Academic Pressure (0–5)
- Study Satisfaction (0–5)
- Sleep Duration (`'5-6 hours'`, `'7-8 hours'`, etc.)
- Dietary Habits (`'Healthy'`, `'Moderate'`, `'Unhealthy'`)
- Suicidal Thoughts (`Yes` / `No`)
- Work/Study Hours (0–12)
- Financial Stress (1–5)
- Family History of Mental Illness (`Yes` / `No`)
- **CGPA** → log transformed & then standardized

## 🧠 Data Insights

### 📊 Numerical Features

- The numerical data was already clean, with **no duplicates** or major outliers.
- **Financial Stress** had only **3 missing values**, which were imputed to maintain dataset consistency.
- **CGPA** was found to be **highly right-skewed**, so it was **log-transformed** and **standardized** to improve model performance.
- Interestingly, **CGPA showed little linear correlation** with depression, but students with **high CGPA and long study hours** still showed higher depression risk—indicating possible **academic overburden**.
- Features like **Academic Pressure**, **Work/Study Hours**, and **Financial Stress** demonstrated **strong correlation** with depression and played a more decisive role in predictions.

### 🧾 Categorical Features

- **Age**, **City**, and **Degree** columns were **removed** as they didn’t contribute meaningfully to the target prediction.
- **Sleep Duration** had some missing values which were **dropped**.
- The **"Others"** category in columns like *Sleep Duration* and *Dietary Habits* had very few samples, so it was also **dropped** to reduce noise.
- Overall, categorical data was **well-structured** and required minimal cleanup.
---

## 🚀 Run Locally (Without Docker)

### 1. Clone the repository
```bash
git clone https://github.com/AbdulWahab740/student-depression-checker.git
cd student-depression-checker
```

### 2. Install required packages
Make sure you’re using Python 3.10+ and then:
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🐳 Run with Docker

### 1. Build the Docker image
```bash
docker build -t student-depression-app .
```

### 2. Run the container
```bash
docker run -p 8501:8501 student-depression-app
```

### 3. Open the app
Go to your browser and open:  
[http://localhost:8501](http://localhost:8501)


---

## 📁 Project Structure

```
student-depression-checker/
├── app.py                      # Streamlit application
├── scaler.pkl                  # StandardScaler used during training
├── student_depression_model.pkl  # Trained Logistic Regression model
├── requirements.txt            # Minimal dependencies
├── Dockerfile                  # Docker config
└── README.md                   # Project overview
```

Both the model (`student_depression_model.pkl`) and the scaler (`scaler.pkl`) are loaded during app startup.

---

## 📄 License

MIT License. Free to use and modify.

---

## 🙌 Acknowledgments

Developed by [Abdul Wahab](https://github.com/AbdulWahab740)  
Built with 💻 Python & ❤️ Streamlit
