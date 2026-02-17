from flask import Flask, request, render_template
from flask_mail import Mail, Message
import pandas as pd
import numpy as np
import re

app = Flask(__name__)

# ---------- EMAIL CONFIG (CHANGE THESE) ----------

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 657
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'kkumud_be23@thapar.edu'
app.config['MAIL_PASSWORD'] = 'GO with flow'

mail = Mail(app)

# -----------------------------------------------


def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def topsis(data, weights, impacts):

    matrix = data.iloc[:, 1:].values

    norm = np.sqrt((matrix ** 2).sum(axis=0))
    matrix = matrix / norm
    matrix = matrix * weights

    best = []
    worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            best.append(matrix[:, i].max())
            worst.append(matrix[:, i].min())
        else:
            best.append(matrix[:, i].min())
            worst.append(matrix[:, i].max())

    best = np.array(best)
    worst = np.array(worst)

    d1 = np.sqrt(((matrix - best) ** 2).sum(axis=1))
    d2 = np.sqrt(((matrix - worst) ** 2).sum(axis=1))

    score = d2 / (d1 + d2)
    rank = score.argsort()[::-1] + 1

    data["Topsis Score"] = score
    data["Rank"] = rank

    return data


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        if not valid_email(email):
            return "Invalid Email Format"

        weights = list(map(float, weights.split(",")))
        impacts = impacts.split(",")

        if len(weights) != len(impacts):
            return "Weights and Impacts must be same length"

        for i in impacts:
            if i not in ['+', '-']:
                return "Impacts must be + or -"

        df = pd.read_csv(file)

        result = topsis(df, weights, impacts)

        output_file = "result_web.csv"
        result.to_csv(output_file, index=False)

        # ---------- SEND EMAIL ----------

        msg = Message(
            "TOPSIS Result",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )

        msg.body = "Your TOPSIS result is attached."

        with open(output_file, "rb") as f:
            msg.attach(output_file, "text/csv", f.read())

        mail.send(msg)

        return "Result sent to your email successfully!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
