from flask import Flask, request, jsonify
from flask_cors import CORS
import os  # ← اضافه شده برای استفاده از PORT محیطی

app = Flask(__name__)
CORS(app)

@app.route("/api/upload", methods=["POST"])
def upload_file():
    return jsonify({"message": "File uploaded successfully"}), 200

@app.route("/api/files", methods=["GET"])
def list_files():
    return jsonify([
        {"name": "Sample_Report.pdf", "status": "Pending"},
        {"name": "Energy_Analysis.xlsx", "status": "Approved"}
    ])

@app.route("/api/investor/download/<filename>", methods=["GET"])
def download_file(filename):
    return jsonify({"message": f"Download {filename} initiated"}), 200

@app.route("/api/investor/meeting", methods=["POST"])
def schedule_meeting():
    data = request.get_json()
    return jsonify({"message": "Meeting request submitted", "data": data}), 200

if __name__ == "__main__":
    # 👇 این خط، پورت را از محیط دریافت می‌کند و برای Render لازم است
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

