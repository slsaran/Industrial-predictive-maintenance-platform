import streamlit as st
import requests

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="Industrial Predictive Maintenance",
    page_icon="⚙️",
    layout="wide"
)

# ==================================================
# Feature Display Names
# ==================================================

DISPLAY_NAMES = {

    "air_temperature_k": "Air Temperature",

    "process_temperature_k": "Process Temperature",

    "rotational_speed_rpm": "Rotational Speed",

    "torque_nm": "Torque",

    "tool_wear_min": "Tool Wear",

    "temperature_difference": "Temperature Difference",

    "power_proxy": "Power Proxy",

    "mechanical_stress_index": "Mechanical Stress Index",

    "thermal_stress_index": "Thermal Stress Index",

    "Type_H": "Machine Type H",

    "Type_L": "Machine Type L",

    "Type_M": "Machine Type M"
}

# ==================================================
# Driver Explanations
# ==================================================

DRIVER_EXPLANATIONS = {

    "Air Temperature":
    "Ambient operating temperature around the machine.",

    "Process Temperature":
    "Internal process temperature during operation.",

    "Rotational Speed":
    "Lower RPM combined with high load can increase failure risk.",

    "Torque":
    "Higher torque generally increases mechanical stress.",

    "Tool Wear":
    "Represents accumulated wear on machine tooling.",

    "Temperature Difference":
    "Difference between process and ambient temperature. Higher values indicate thermal stress.",

    "Power Proxy":
    "Estimated machine power demand (RPM × Torque).",

    "Mechanical Stress Index":
    "Measures mechanical strain using torque and rotational speed.",

    "Thermal Stress Index":
    "Combines tool wear and temperature difference to estimate long-term thermal degradation.",

    "Machine Type H":
    "High-quality machine category.",

    "Machine Type L":
    "Low-quality machine category.",

    "Machine Type M":
    "Medium-quality machine category."
}

# ==================================================
# Sidebar
# ==================================================

st.sidebar.title("⚙️ Project Information")

st.sidebar.markdown("""
### Industrial Predictive Maintenance Platform

**Model**
- XGBoost Classifier

**Backend**
- FastAPI

**Frontend**
- Streamlit

**Explainability**
- SHAP

**Experiment Tracking**
- MLflow

**Dataset**
- AI4I Predictive Maintenance Dataset
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Machine Features")

st.sidebar.markdown("""
**Air Temperature (K)**
- Typical Range: 295-305 K

**Process Temperature (K)**
- Typical Range: 305-315 K

**Rotational Speed (RPM)**
- Typical Range: 1100-2900 RPM

**Torque (Nm)**
- Typical Range: 3-80 Nm

**Tool Wear (min)**
- Typical Range: 0-250 min
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Engineered Features")

st.sidebar.markdown("""
**Temperature Difference**
- Process Temp − Air Temp

**Power Proxy**
- RPM × Torque

**Mechanical Stress Index**
- Torque / RPM

**Thermal Stress Index**
- Tool Wear × Temperature Difference
""")

# ==================================================
# Header
# ==================================================

st.title("⚙️ Industrial Predictive Maintenance Platform")

st.markdown(
    "Predict machine failure risk using machine operating conditions and engineered health indicators."
)

st.info(
    "This system uses XGBoost, SHAP explainability, feature engineering and risk scoring to estimate machine failure risk."
)

st.divider()

# ==================================================
# Inputs
# ==================================================

st.header("Machine Parameters")

col1, col2 = st.columns(2)

with col1:

    air_temperature_k = st.number_input(
        "Air Temperature (K)",
        value=298.1
    )

    process_temperature_k = st.number_input(
        "Process Temperature (K)",
        value=308.6
    )

    rotational_speed_rpm = st.number_input(
        "Rotational Speed (RPM)",
        value=1500
    )

    torque_nm = st.number_input(
        "Torque (Nm)",
        value=40.0
    )

with col2:

    tool_wear_min = st.number_input(
        "Tool Wear (min)",
        value=100
    )

    machine_type = st.selectbox(
        "Machine Type",
        ["H", "L", "M"]
    )

# ==================================================
# Type Encoding
# ==================================================

type_h = 1 if machine_type == "H" else 0
type_l = 1 if machine_type == "L" else 0
type_m = 1 if machine_type == "M" else 0

st.divider()

# ==================================================
# Prediction
# ==================================================

if st.button("🔍 Predict Failure Risk"):

    payload = {

        "air_temperature_k": air_temperature_k,

        "process_temperature_k": process_temperature_k,

        "rotational_speed_rpm": rotational_speed_rpm,

        "torque_nm": torque_nm,

        "tool_wear_min": tool_wear_min,

        "type_h": type_h,

        "type_l": type_l,

        "type_m": type_m
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        st.success("Prediction Generated Successfully")

        st.divider()

        st.header("Prediction Results")

        metric1, metric2, metric3 = st.columns(3)

        with metric1:

            st.metric(
                "Failure Probability",
                f"{result['failure_probability']:.2%}"
            )

        with metric2:

            st.metric(
                "Risk Score",
                f"{result['risk_score']:.2f}"
            )

        with metric3:

            st.metric(
                "Risk Level",
                result["risk_level"]
            )

        st.write("")

        risk_level = result["risk_level"]

        if risk_level == "LOW":

            st.success("🟢 LOW RISK MACHINE")

        elif risk_level == "MEDIUM":

            st.warning("🟠 MEDIUM RISK MACHINE")

        else:

            st.error("🔴 HIGH RISK MACHINE")

        st.divider()

        st.subheader("Top Risk Drivers")

        for driver in result["top_drivers"]:

            display_name = DISPLAY_NAMES.get(
                driver,
                driver
            )

            st.markdown(
                f"""
### {display_name}

{DRIVER_EXPLANATIONS.get(display_name, "No description available.")}
"""
            )

    except Exception as e:

        st.error(
            f"Error connecting to API: {e}"
        )

# ==================================================
# Methodology
# ==================================================

with st.expander("How is risk calculated?"):

    st.markdown("""
### Prediction Pipeline

Machine Inputs

↓

Feature Engineering

↓

XGBoost Model

↓

SHAP Explainability

↓

Risk Scoring

↓

Prediction Report

### Risk Levels

- LOW : Risk Score < 30
- MEDIUM : Risk Score 30 - 70
- HIGH : Risk Score > 70

### Engineered Features

- Temperature Difference
- Power Proxy
- Mechanical Stress Index
- Thermal Stress Index
""")

# ==================================================
# Footer
# ==================================================

st.divider()

st.caption(
    "Built using XGBoost, SHAP, FastAPI, MLflow and Streamlit"
)