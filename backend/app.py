from flask import Flask, request, jsonify
from processor import map_skus
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        df = map_skus(filepath)
        mapped_count = df['Mapped SKU'].ne("Not Mapped").sum()
        return jsonify({"status": "success", "rows": len(df), "mapped": int(mapped_count)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
