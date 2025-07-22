from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Create a directory to store sound files
SOUND_DIR = "sounds"
os.makedirs(SOUND_DIR, exist_ok=True)

@app.route("/")
def home():
    return "Zenlife Backend is Running ✅"

@app.route("/generate", methods=["POST"])
def generate_sound():
    data = request.get_json()

    if not data or "username" not in data or "text" not in data:
        return jsonify({"error": "Missing 'username' or 'text' field"}), 400

    username = data["username"]
    text = data["text"]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    filename = f"{username}_{timestamp}.txt"
    filepath = os.path.join(SOUND_DIR, filename)

    with open(filepath, "w") as f:
        f.write(text)

    return jsonify({"message": "Sound file saved successfully", "file": filename}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
