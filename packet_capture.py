from scapy.all import sniff
import joblib
import requests

# Load trained model
model = joblib.load("model.pkl")

def process_packet(packet):
    try:
        # 🔹 Extract features
        duration = 0  # not available from packet
        src_bytes = len(packet)
        dst_bytes = len(packet.payload)

        # 🔹 ML Prediction
        prediction = model.predict([[duration, src_bytes, dst_bytes]])[0]

        if prediction == 0:
            result = "🚨 Attack Detected"
        else:
            result = "✅ Normal"

        # 🔹 Packet summary
        packet_info = packet.summary()

        # Print in terminal
        print(result, "|", packet_info)

        # 🔹 Send to Flask UI
        try:
            requests.post(
                "http://127.0.0.1:5000/update",
                json={
                    "result": result,
                    "packet": packet_info
                },
                timeout=1
            )
        except:
            print("⚠️ Flask server not reachable")

    except Exception as e:
        print("Error:", e)


print("🚀 Real-time packet capture started...")
print("👉 Generate traffic (open browser, refresh pages)")

# Start sniffing
sniff(prn=process_packet, store=False)