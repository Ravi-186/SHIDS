# 🚀 SHIDS - AI-Based Hybrid Intrusion Detection System

## 📌 Overview

SHIDS (Scalable Hybrid Intrusion Detection System) is an AI-based security system designed to detect network intrusions using both **supervised** and **unsupervised learning techniques**.

The system combines multiple machine learning algorithms to identify malicious activities such as:

* DoS (Denial of Service)
* Port Scanning
* Brute Force Attacks
* Anomalous Network Behavior

---

## 🧠 Key Concept

This project follows a **Hybrid Approach**:

* 🔹 **Signature-Based Detection (Supervised Learning)**
* 🔹 **Anomaly-Based Detection (Unsupervised Learning)**

This improves accuracy and helps detect both known and unknown attacks.

---

## 🛠 Technologies Used

* Python
* Machine Learning (Scikit-learn)
* HTML, CSS, JavaScript
* Git & GitHub

---

## 📂 Project Structure

```
SHIDS/
│── index.html
│── dashboard.html
│── live.html
│── train_model.py
│
├── supervised_learning/
│   └── models/
│       └── model_training.py
│
├── unsupervised_learning/
│   ├── anomaly_detection/
│   │   ├── isolation_forest.py
│   │   └── local_outlier_factory.py
│   │
│   └── clustering/
│       ├── kmeans.py
│       └── dbscan.py
│
└── assets/ (CSS, JS, images)
```

---

## ⚙️ Features

* 📊 Real-time intrusion detection (simulated)
* 🤖 Machine learning-based attack classification
* 🔍 Anomaly detection using clustering techniques
* 📈 Dashboard visualization interface
* 🧩 Modular architecture for scalability

---

## 🤖 Machine Learning Models Used

### 🔹 Supervised Learning

* Classification-based attack detection

### 🔹 Unsupervised Learning

* K-Means Clustering
* DBSCAN Clustering
* Isolation Forest
* Local Outlier Factor

---

## ▶️ How to Run (Local Setup)

1. Clone the repository:

```
git clone https://github.com/Ravi-186/SHIDS.git
cd SHIDS
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run model training:

```
python train_model.py
```

4. Open the frontend:

```
index.html (open in browser)
```

---

## 🌐 Deployment

* Frontend deployed using **GitHub Pages**
* Backend (ML models) runs locally

🔗 Live Demo:
https://ravi-186.github.io/SHIDS/

---

## 📸 Screenshots

(Add screenshots of your dashboard, live detection, and results here)

---

## 🎯 Future Enhancements

* Integration with real-time network traffic (packet capture)
* Deployment using Django/Flask backend
* Cloud-based intrusion monitoring
* Advanced deep learning models

---

## 👨‍💻 Author

**Sri Ravi Tej Bobba**

---

## 📜 License

This project is for academic and educational purposes.
