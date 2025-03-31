from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pathlib import Path
from ftplib import FTP
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)

def get_nas_files(nas_path_str):
    nas_path = Path(nas_path_str)
    if not nas_path.exists():
        return None
    results = []
    for entry in nas_path.rglob('*'):
        if entry.is_dir():
            results.append({
                "type": "directory",
                "name": entry.name,
                "path": str(entry)
            })
        else:
            results.append({
                "type": "file",
                "name": entry.name,
                "path": str(entry.parent)
            })
    return results


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/nas-files', methods=['GET'])
def api_nas_files():
    nas_path_str = request.args.get('nas_path', r"/media/nas/200/1_Projects/2_Ongoing/2025/Angus_2025_Astro_Piston_HPT2/0_CDF")
    # nas_path_str = request.args.get('nas_path', r"/home/jfy/Documents")
    files = get_nas_files(nas_path_str)
    if files is None:
        return jsonify({"error": f"Path {nas_path_str} does not exist."}), 404
    return jsonify(files)

if __name__ == "__main__":
    app.run(debug=True)
