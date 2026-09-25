from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)


# ---------------------------------------------------------
# 1. LOAD DEMO DATA
# ---------------------------------------------------------

def load_data():
    """
    Load the simulated water-quality and symptom datasets.
    """

    water_df = pd.read_csv("water_quality_demo.csv")
    symptom_df = pd.read_csv("symptom_reports_demo.csv")

    return water_df, symptom_df


# ---------------------------------------------------------
# 2. CALCULATE WATER-QUALITY RISK
# ---------------------------------------------------------

def calculate_water_risk(row):
    """
    Calculate a prototype water-quality risk score from 0-100.

    These rules are ONLY for demonstration.
    They are not official health or CGWB thresholds.
    """

    score = 0

    # pH
    if row["pH"] < 6.5 or row["pH"] > 8.5:
        score += 15

    # Fluoride
    if row["Fluoride"] > 1.5:
        score += 15

    # Arsenic
    if row["Arsenic"] > 0.01:
        score += 20

    # Iron
    if row["Iron"] > 0.3:
        score += 15

    # Nitrate
    if row["Nitrate"] > 45:
        score += 20

    return min(score, 100)


# ---------------------------------------------------------
# 3. CALCULATE SYMPTOM RISK
# ---------------------------------------------------------

def calculate_symptom_risk(row):
    """
    Calculate a prototype community symptom risk score.

    These rules are demonstration rules only.
    """

    total_cases = row["Total_Cases"]

    if total_cases >= 100:
        return 100
    elif total_cases >= 80:
        return 80
    elif total_cases >= 60:
        return 65
    elif total_cases >= 40:
        return 50
    elif total_cases >= 25:
        return 35
    else:
        return 20


# ---------------------------------------------------------
# 4. CLASSIFY FINAL RISK
# ---------------------------------------------------------

def classify_risk(score):
    """
    Convert the final risk score into LOW, MEDIUM or HIGH.
    """

    if score <= 30:
        return "LOW"
    elif score <= 60:
        return "MEDIUM"
    else:
        return "HIGH"


# ---------------------------------------------------------
# 5. PROCESS DATA
# ---------------------------------------------------------

def process_data():

    water_df, symptom_df = load_data()

    # Merge both datasets using District
    merged_df = pd.merge(
        water_df,
        symptom_df,
        on="District",
        how="inner"
    )

    # Calculate water-quality risk
    merged_df["Water_Risk"] = merged_df.apply(
        calculate_water_risk,
        axis=1
    )

    # Calculate symptom risk
    merged_df["Symptom_Risk"] = merged_df.apply(
        calculate_symptom_risk,
        axis=1
    )

    # Combine the two risk components
    # Water risk = 60%
    # Symptom risk = 40%
    merged_df["Risk_Score"] = (
        merged_df["Water_Risk"] * 0.60
        + merged_df["Symptom_Risk"] * 0.40
    ).round(0).astype(int)

    # Make sure score stays between 0 and 100
    merged_df["Risk_Score"] = merged_df["Risk_Score"].clip(0, 100)

    # Classify risk
    merged_df["Risk_Level"] = merged_df["Risk_Score"].apply(
        classify_risk
    )

    return merged_df


# ---------------------------------------------------------
# 6. MAIN DASHBOARD ROUTE
# ---------------------------------------------------------

@app.route("/")
def dashboard():

    data = process_data()

    # Summary values
    districts_monitored = len(data)

    high_risk = len(
        data[data["Risk_Level"] == "HIGH"]
    )

    medium_risk = len(
        data[data["Risk_Level"] == "MEDIUM"]
    )

    total_symptoms = int(
        data["Total_Cases"].sum()
    )

    # Convert dataframe into dictionary records
    districts = data.to_dict(orient="records")

    return render_template(
        "index.html",
        districts=districts,
        districts_monitored=districts_monitored,
        high_risk=high_risk,
        medium_risk=medium_risk,
        total_symptoms=total_symptoms
    )


# ---------------------------------------------------------
# 7. API ROUTE
# ---------------------------------------------------------

@app.route("/api/districts")
def district_data():

    data = process_data()

    districts = data.to_dict(orient="records")

    return jsonify(districts)


# ---------------------------------------------------------
# 8. RUN FLASK APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5001)