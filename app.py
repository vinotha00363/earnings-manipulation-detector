import streamlit as st

st.set_page_config(
    page_title="Earnings Manipulation Detector",
    layout="centered"
)

st.title("📊 Earnings Manipulation Detection Tool")
st.write(
    "Enter the financial ratios below. "
    "The model will classify the company as **Manipulator** or **Non-Manipulator** "
    "using the **Beneish M-Score**."
)

st.markdown("---")

# -------------------------
# User Inputs
# -------------------------
dsri = st.number_input(
    "DSRI – Days Sales in Receivables Index",
    value=1.0, step=0.01
)

gmi = st.number_input(
    "GMI – Gross Margin Index",
    value=1.0, step=0.01
)

aqi = st.number_input(
    "AQI – Asset Quality Index",
    value=1.0, step=0.01
)

sgi = st.number_input(
    "SGI – Sales Growth Index",
    value=1.0, step=0.01
)

depi = st.number_input(
    "DEPI – Depreciation Index",
    value=1.0, step=0.01
)

sgai = st.number_input(
    "SGAI – SG&A Expense Index",
    value=1.0, step=0.01
)

tata = st.number_input(
    "TATA – Total Accruals to Total Assets",
    value=0.0, step=0.01
)

lvgi = st.number_input(
    "LVGI – Leverage Index",
    value=1.0, step=0.01
)

st.markdown("---")

# -------------------------
# Calculate Button
# -------------------------
if st.button("🔍 Check Manipulation Risk"):

    # Beneish M-Score Formula
    m_score = (
        -4.84
        + 0.92 * dsri
        + 0.528 * gmi
        + 0.404 * aqi
        + 0.892 * sgi
        + 0.115 * depi
        - 0.172 * sgai
        + 4.679 * tata
        - 0.327 * lvgi
    )

    st.subheader("Result")
    st.write(f"**Beneish M-Score:** `{m_score:.2f}`")

    if m_score > -2.22:
        st.error("⚠️ The company is likely an **EARNINGS MANIPULATOR**")
    else:
        st.success("✅ The company is likely a **NON-MANIPULATOR**")
