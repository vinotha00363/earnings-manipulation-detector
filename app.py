import streamlit as st

st.set_page_config(page_title="Earnings Manipulation Detector", layout="wide")

# ----------------------------
# Title
# ----------------------------
st.title("Earnings Manipulation Detection Tool")

# ----------------------------
# Load & show existing HTML
# ----------------------------
with open("Earnings_Manipulator_Class_2_Jan_2026.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=500, scrolling=True)

st.markdown("---")

# ----------------------------
# User Input Section
# ----------------------------
st.subheader("Enter Financial Values")

dsri = st.number_input("DSRI (Days Sales in Receivables Index)", value=1.0)
gmi = st.number_input("GMI (Gross Margin Index)", value=1.0)
aqi = st.number_input("AQI (Asset Quality Index)", value=1.0)
sgi = st.number_input("SGI (Sales Growth Index)", value=1.0)
depi = st.number_input("DEPI (Depreciation Index)", value=1.0)
sgai = st.number_input("SGAI (SG&A Index)", value=1.0)
tata = st.number_input("TATA (Total Accruals to Total Assets)", value=0.0)
lvgi = st.number_input("LVGI (Leverage Index)", value=1.0)

# ----------------------------
# Calculate Button
# ----------------------------
if st.button("Check Manipulation Risk"):
    
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

    st.markdown("### Result")

    st.write(f"**Beneish M-Score:** `{m_score:.2f}`")

    if m_score > -2.22:
        st.error("⚠️ Company is likely an **EARNINGS MANIPULATOR**")
    else:
        st.success("✅ Company is likely a **NON-MANIPULATOR**")
