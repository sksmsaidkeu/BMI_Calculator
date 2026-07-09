import os
import threading
import webbrowser

from flask import Flask, render_template, request

from bmi_calculator import ADVICE, calculate_bmi, classify_bmi

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        height_raw = request.form.get("height", "").strip()
        weight_raw = request.form.get("weight", "").strip()

        try:
            height_cm = float(height_raw)
            weight_kg = float(weight_raw)
            if height_cm <= 0 or weight_kg <= 0:
                raise ValueError
        except ValueError:
            error = "키와 몸무게는 0보다 큰 숫자로 입력해주세요."
        else:
            bmi = calculate_bmi(height_cm, weight_kg)
            category = classify_bmi(bmi)
            result = {
                "height": height_cm,
                "weight": weight_kg,
                "bmi": round(bmi, 2),
                "category": category,
                "advice": ADVICE[category],
            }

    return render_template("bmi.html", result=result, error=error)


if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        threading.Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True, port=5000)
