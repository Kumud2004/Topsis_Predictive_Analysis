# Topsis_Predictive_Analysis
# TOPSIS Web Application

This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method using a web-based application developed using Flask.

The application allows users to upload a CSV file, enter weights and impacts, and receive the ranked result through email.

---

## Objective

The objective of this project is to provide an easy-to-use web interface for performing multi-criteria decision making using the TOPSIS method.

---

## Technologies Used

- Python  
- Flask  
- Pandas  
- NumPy  
- Flask-Mail  
- HTML  
- CSS  

---

## Project Structure

```
TOPSIS-102316088/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── data.csv
├── result_web.csv
└── screenshots/
    └── web_form.png
```

---

## Methodology

The TOPSIS algorithm is implemented using the following steps:

1. Normalize the input data.
2. Multiply normalized values with weights.
3. Identify ideal best and ideal worst solutions.
4. Calculate distance from ideal solutions.
5. Compute TOPSIS score.
6. Rank the alternatives based on scores.

The alternative with the highest score is considered the best.

---

## Result Table

After processing, the system generates a result file containing the TOPSIS score and rank for each alternative.

Example:

| Fund | P1   | P2   | P3  | P4  | Topsis Score | Rank |
|------|------|------|-----|-----|--------------|------|
| M4   | 0.60 | 0.36 | 3.5 | 69.2| 0.65         | 2    |
| M1   | 0.67 | 0.45 | 6.5 | 42.6| 0.58         | 3    |
| M2   | 0.60 | 0.36 | 3.6 | 53.3| 0.41         | 4    |

---

## Result Graph Interpretation

A bar graph can be plotted using TOPSIS scores.

- X-axis: Alternatives  
- Y-axis: TOPSIS Scores  

Higher bars represent better-performing alternatives. The graph helps in easy comparison of results.

---

## Web Application Output

The final output of the web application is displayed in the form of a result file and email notification.

A screenshot of the final website output is available in the `screenshots` folder with the name:


![Web Application Output](screenshot/web_form.png)


---

## How to Run the Application

### Step 1: Install Dependencies

```bash
pip install pandas numpy flask flask-mail
```

### Step 2: Run the Server

```bash
python app.py
```

### Step 3: Open in Browser

Open the following URL:

```
http://127.0.0.1:5000
```

### Step 4: Submit Form

- Upload CSV file
- Enter weights
- Enter impacts
- Enter email
- Click Submit

The result file will be sent to the given email.

---

## Input Validation

The system validates:

- Email format
- Numeric values in file
- Equal number of weights and impacts
- Correct impact symbols (+ or -)

---

## Advantages

- Simple interface
- Fast execution
- Automated ranking
- Accurate results
- Easy to use
