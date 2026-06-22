import streamlit as st
import requests


st.set_page_config(

    page_title="Industrial Predictive Maintenance",

    layout="wide"

)

st.title(
    "Industrial Predictive Maintenance Platform"
)

st.markdown(
    "Predict machine failure risk using the trained XGBoost model."
)

# ==========================================
# Inputs
# ==========================================

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

# ==========================================
# Type Encoding
# ==========================================

type_h = 1 if machine_type == "H" else 0

type_l = 1 if machine_type == "L" else 0

type_m = 1 if machine_type == "M" else 0

# ==========================================
# Predict Button
# ==========================================

if st.button(
    "Predict Failure Risk"
):

    payload = {

        "air_temperature_k":
        air_temperature_k,

        "process_temperature_k":
        process_temperature_k,

        "rotational_speed_rpm":
        rotational_speed_rpm,

        "torque_nm":
        torque_nm,

        "tool_wear_min":
        tool_wear_min,

        "type_h":
        type_h,

        "type_l":
        type_l,

        "type_m":
        type_m

    }

    response = requests.post(

        "http://127.0.0.1:8000/predict",

        json=payload

    )

    result = response.json()

    st.success(
        "Prediction Generated"
    )

    st.subheader(
        "Prediction Results"
    )

    st.write(

        f"Failure Probability: "
        f"{result['failure_probability']:.4f}"

    )

    st.write(

        f"Risk Score: "
        f"{result['risk_score']}"

    )

    st.write(

        f"Risk Level: "
        f"{result['risk_level']}"

    )

    st.subheader(
        "Top Drivers"
    )

    for driver in result["top_drivers"]:

        st.write(
            f"• {driver}"
        )