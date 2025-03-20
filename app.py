from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# تحميل بيانات BIN عند بدء التشغيل
with open("top_bin.json", "r", encoding="utf-8") as file:
    BIN_DATA = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/bin/<bin_code>")
def get_bin_info(bin_code):
    if len(bin_code) != 6 or not bin_code.isdigit():
        return jsonify({"error": "BIN must be 6 digits"}), 400

    bin_info = BIN_DATA.get(bin_code, {"error": "BIN not found"})
    return jsonify(bin_info)

@app.route("/check", methods=["POST"])
def check_bin():
    bin_code = request.form.get("bin")
    bin_info = BIN_DATA.get(bin_code, None)
    return render_template("index.html", bin_info=bin_info, bin_code=bin_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
