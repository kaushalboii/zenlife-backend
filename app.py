from flask import Flask, request, jsonify
import uuid, os

app = Flask(__name__)
SOUND_FOLDER = "sounds"
os.makedirs(SOUND_FOLDER, exist_ok=True)

@app.route('/generate', methods=['POST'])
def generate_sound():
    user_input = request.json.get('input')
    filename = f"{uuid.uuid4()}.txt"
    with open(os.path.join(SOUND_FOLDER, filename), 'w') as f:
        f.write(f"Sound for: {user_input}")
    return jsonify({'status': 'success', 'file': filename})

@app.route('/')
def home():
    return "ZenLife AI Sound Generator is online."
