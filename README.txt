SMART COMMUNITY HEALTH MONITORING AND EARLY WARNING SYSTEM
FOR WATER-BORNE DISEASES IN RURAL NORTHEAST INDIA

Project Type:
College PBL Prototype

Technology:
Python
Flask
Pandas
HTML
CSS
JavaScript
CSV

PROJECT OBJECTIVE
Integrate environmental and community health signals to support
early detection of potential water-borne disease outbreaks.

SYSTEM FLOW

Water Quality Data
        +
Community Symptom Data
        ↓
Data Processing
        ↓
Risk Scoring Engine
        ↓
Low / Medium / High Risk
        ↓
Dashboard Alert
        ↓
Community Health Warning

WATER QUALITY PARAMETERS

- pH
- Fluoride
- Arsenic
- Iron
- Nitrate

COMMUNITY SYMPTOM DATA

- District
- Date
- Diarrhea cases
- Vomiting cases
- Fever cases
- Total cases

RISK CLASSIFICATION

0–30   = LOW
31–60  = MEDIUM
61–100 = HIGH

These thresholds are prototype demonstration rules only.

IMPORTANT PROTOTYPE DISCLAIMER

All displayed water-quality and symptom values are simulated
demonstration data.

The data is NOT real CGWB measurement data and does not
represent real patient records.

The risk thresholds are prototype rules and are not official
clinical or public-health thresholds.

NOTIFICATION SYSTEM

The prototype generates location-based warning messages and
provides a Send Alert action.

The Send Alert button is a DEMO action only.

No actual SMS or WhatsApp message is sent.

A future SMS/WhatsApp gateway can connect to this action to
deliver alerts to registered residents or health workers.

HOW TO RUN

1. Open Command Prompt in the project folder.

2. Create a virtual environment:

   python -m venv venv

3. Activate it on Windows:

   venv\Scripts\activate

4. Install dependencies:

   pip install -r requirements.txt

5. Run the Flask application:

   python app.py

6. Open the browser:

   http://127.0.0.1:5000/

PROJECT FILES

app.py
Flask backend, CSV processing and risk calculation.

water_quality_demo.csv
Simulated water-quality demonstration data.

symptom_reports_demo.csv
Simulated community symptom demonstration data.

requirements.txt
Python dependencies required by the project.

templates/index.html
Frontend dashboard.

README.txt
Project documentation and setup instructions.