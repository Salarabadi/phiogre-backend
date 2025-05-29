from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "✅ PhiOGRE backend is running successfully!"})

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
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
