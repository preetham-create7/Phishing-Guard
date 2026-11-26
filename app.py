from flask import Flask, render_template, request, jsonify
from detector import detect_phishing

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    url = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "Enter a URL"}), 400

    result = detect_phishing(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)