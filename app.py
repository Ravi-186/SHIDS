from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')   # 🔥 IMPORTANT FIX

app = Flask(__name__)

model = joblib.load("model.pkl")

# 🔥 Store latest live result
latest_result = "No live data yet"

# 🔥 Store live predictions (for dashboard)
live_data = []

# 🔥 Store packet logs (last 20)
packet_logs = []

@app.route('/')
def home():
    return render_template('home.html')


# ================= MANUAL PREDICTION =================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        duration = float(request.form['duration'])
        src = float(request.form['src_bytes'])
        dst = float(request.form['dst_bytes'])

        prediction = model.predict([[duration, src, dst]])[0]

        if prediction == 0:
            result = "🚨 Attack Detected (Suspicious Traffic)"
        else:
            result = "✅ Normal Traffic (Safe)"

        return render_template('index.html', prediction=result)

    except:
        return render_template('index.html', prediction="❌ Invalid Input")


# ================= DYNAMIC DASHBOARD =================
@app.route('/dashboard')
def dashboard():
    global live_data

    if len(live_data) == 0:
        attack_count = 0
        normal_count = 0
    else:
        counts = pd.Series(live_data).value_counts()
        attack_count = counts.get("attack", 0)
        normal_count = counts.get("normal", 0)

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.figure()
    plt.bar(["Attack", "Normal"],
            [attack_count, normal_count],
            color=["red", "green"])
    plt.title("Live Traffic Analysis")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.savefig("static/chart.png")
    plt.close()

    total = attack_count + normal_count

    return render_template('dashboard.html',
                           total=total,
                           attacks=attack_count,
                           normal=normal_count)


# ================= REAL-TIME UPDATE API =================
@app.route('/update', methods=['POST'])
def update():
    global latest_result, live_data, packet_logs

    data = request.json
    result = data['result']
    packet_info = data.get('packet', 'Unknown')

    # 🔥 Always update latest result
    latest_result = result

    # Store for dashboard
    if "Attack" in result:
        live_data.append("attack")
    else:
        live_data.append("normal")

    # Store logs
    packet_logs.append({
        "result": result,
        "packet": packet_info
    })

    # Keep last 20 only
    packet_logs = packet_logs[-20:]

    return jsonify({"status": "updated"})


# ================= GET PACKET LOGS =================
@app.route('/logs')
def logs():
    return jsonify(packet_logs)


# ================= LIVE PAGE =================
@app.route('/live')
def live():
    return render_template('live.html', result=latest_result)


if __name__ == "__main__":
    app.run(debug=True)