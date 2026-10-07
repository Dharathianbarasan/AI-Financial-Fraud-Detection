import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Bank Fraud Monitoring System",
    page_icon="🏦",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #07111f;
    color: white;
}

.bank-header {
    background: linear-gradient(90deg, #0b1f33, #12395a);
    padding: 25px 30px;
    border-radius: 15px;
    margin-bottom: 20px;
    border: 1px solid #234b6f;
}

.bank-title {
    font-size: 34px;
    font-weight: 800;
}

.bank-subtitle {
    color: #9fb3c8;
    font-size: 15px;
}

.kpi {
    background: #102a43;
    border: 1px solid #234b6f;
    border-radius: 15px;
    padding: 20px;
    min-height: 130px;
}

.kpi-title {
    color: #9fb3c8;
    font-size: 14px;
}

.kpi-value {
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

.kpi-icon {
    font-size: 28px;
}

.section {
    background: #102a43;
    border: 1px solid #234b6f;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
}

.section-title {
    font-size: 21px;
    font-weight: 700;
    color: #5ee7df;
    margin-bottom: 15px;
}

.alert {
    background: #451a1a;
    border: 1px solid #ef4444;
    border-radius: 12px;
    padding: 18px;
    color: white;
}

.safe {
    background: #064e3b;
    border: 1px solid #10b981;
    border-radius: 12px;
    padding: 18px;
    color: white;
}

.model-card {
    background: #102a43;
    border: 1px solid #234b6f;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}

.status {
    color: #10b981;
    font-weight: bold;
}

.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 10px;
    background: linear-gradient(90deg, #0072ff, #00c6ff);
    color: white;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
}

.footer {
    text-align: center;
    color: #78909c;
    margin-top: 30px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="bank-header">

<div class="bank-title">
🏦 SecureBank AI Fraud Monitoring
</div>

<div class="bank-subtitle">
Real-Time Financial Transaction Monitoring & AI-Based Fraud Detection
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# LIVE STATUS
# =========================================================

current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

st.markdown(
    f"🟢 **System Status: LIVE** &nbsp;&nbsp; | &nbsp;&nbsp; "
    f"Last Updated: **{current_time}**",
)


# =========================================================
# KPI DATA
# =========================================================

total_transactions = 12548
fraud_transactions = 186
safe_transactions = total_transactions - fraud_transactions

fraud_rate = (
    fraud_transactions / total_transactions
) * 100

transaction_volume = 8426500


# =========================================================
# KPI CARDS
# =========================================================

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-icon">💳</div>
        <div class="kpi-title">Total Transactions</div>
        <div class="kpi-value">{total_transactions:,}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-icon">🚨</div>
        <div class="kpi-title">Fraud Alerts</div>
        <div class="kpi-value">{fraud_transactions}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-icon">✅</div>
        <div class="kpi-title">Safe Transactions</div>
        <div class="kpi-value">{safe_transactions:,}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-icon">📊</div>
        <div class="kpi-title">Fraud Rate</div>
        <div class="kpi-value">{fraud_rate:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-icon">💰</div>
        <div class="kpi-title">Transaction Volume</div>
        <div class="kpi-value">₹{transaction_volume/100000:.1f}L</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# TWO COLUMN AREA
# =========================================================

left, right = st.columns([1.4, 1])


# =========================================================
# TRANSACTION ANALYSIS
# =========================================================

with left:

    st.markdown("""
    <div class="section">

    <div class="section-title">
    🔍 Transaction Risk Analysis
    </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        login_id = st.text_input(
            "👤 Customer / Login ID",
            placeholder="Example: USER1024"
        )

        amount = st.number_input(
            "💰 Transaction Amount (₹)",
            min_value=0.0,
            value=5000.0,
            step=500.0
        )

        connection = st.selectbox(
            "🌐 Transaction Channel",
            [
                "Online Banking",
                "Mobile Banking",
                "ATM",
                "POS",
                "UPI"
            ]
        )

    with c2:

        transaction_type = st.selectbox(
            "💳 Transaction Type",
            [
                "Purchase",
                "Transfer",
                "Withdrawal",
                "Payment"
            ]
        )

        location = st.selectbox(
            "📍 Transaction Location",
            [
                "Chennai",
                "Coimbatore",
                "Bangalore",
                "Mumbai",
                "Delhi",
                "Other"
            ]
        )

        device = st.selectbox(
            "📱 Device",
            [
                "Mobile",
                "Laptop",
                "ATM",
                "POS Terminal"
            ]
        )

    analyze = st.button(
        "🔍 ANALYZE TRANSACTION"
    )


# =========================================================
# TRANSACTION PREDICTION
# =========================================================

with right:

    st.markdown("""
    <div class="section">

    <div class="section-title">
    🛡️ AI Risk Assessment
    </div>
    """, unsafe_allow_html=True)

    if analyze:

        # =================================================
        # AMOUNT BASED FRAUD PREDICTION
        # =================================================

        if amount > 20000:

            prediction = "FRAUD"
            risk_score = 90

            st.markdown(f"""
            <div class="alert">

            <h2>🚨 FRAUD ALERT</h2>

            <p>
            Transaction amount is above ₹20,000.
            </p>

            <h1>{risk_score}%</h1>

            <p>
            Fraud Risk Score
            </p>

            </div>
            """, unsafe_allow_html=True)

        else:

            prediction = "NON-FRAUD"
            risk_score = 10

            st.markdown(f"""
            <div class="safe">

            <h2>✅ TRANSACTION SAFE</h2>

            <p>
            Transaction amount is ₹20,000 or below.
            </p>

            <h1>{risk_score}%</h1>

            <p>
            Fraud Risk Score
            </p>

            </div>
            """, unsafe_allow_html=True)


        # =================================================
        # MODEL RESULTS
        # =================================================

        st.markdown("<br>", unsafe_allow_html=True)

        st.write("### 🤖 Model Prediction")

        st.write("**XGBoost:**", prediction)

        st.write("**AFF-Net:**", prediction)

        if prediction == "FRAUD":

            st.error(
                "🚨 Action: Review Required"
            )

        else:

            st.success(
                "✅ Action: Transaction Approved"
            )

    else:

        st.info(
            "Enter transaction details and analyze the transaction."
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# RECENT TRANSACTIONS
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
📋 Recent Transaction Monitoring
</div>
""", unsafe_allow_html=True)


transaction_data = pd.DataFrame({

    "Transaction ID": [
        "TXN10001",
        "TXN10002",
        "TXN10003",
        "TXN10004",
        "TXN10005",
        "TXN10006"
    ],

    "Customer ID": [
        "USER101",
        "USER205",
        "USER304",
        "USER412",
        "USER518",
        "USER621"
    ],

    "Amount": [
        2500,
        85000,
        4300,
        56000,
        1200,
        73000
    ],

    "Channel": [
        "UPI",
        "Online Banking",
        "POS",
        "ATM",
        "Mobile Banking",
        "Online Banking"
    ],

    "Risk Score": [
        12,
        91,
        18,
        82,
        9,
        76
    ],

    "Status": [
        "✅ Safe",
        "🚨 Fraud",
        "✅ Safe",
        "🚨 Fraud",
        "✅ Safe",
        "⚠️ Review"
    ]

})


st.dataframe(
    transaction_data,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# ANALYTICS
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

chart1, chart2 = st.columns(2)


with chart1:

    st.markdown("""
    <div class="section-title">
    📈 Daily Transaction Monitoring
    </div>
    """, unsafe_allow_html=True)

    chart_data = pd.DataFrame({

        "Transactions": [
            820,
            910,
            875,
            1020,
            1100,
            980,
            1250
        ],

        "Fraud": [
            12,
            15,
            11,
            22,
            18,
            14,
            25
        ]

    })

    st.line_chart(chart_data)


with chart2:

    st.markdown("""
    <div class="section-title">
    🚨 Fraud Risk Distribution
    </div>
    """, unsafe_allow_html=True)

    risk_data = pd.DataFrame({

        "Risk Level": [
            "Low",
            "Medium",
            "High"
        ],

        "Transactions": [
            8200,
            4162,
            186
        ]

    })

    st.bar_chart(
        risk_data.set_index("Risk Level")
    )


# =========================================================
# AI MODEL STATUS
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
🤖 AI Model Monitoring
</div>
""", unsafe_allow_html=True)


m1, m2, m3 = st.columns(3)


with m1:

    st.markdown("""
    <div class="model-card">

    <div style="font-size:40px;">🤖</div>

    <h3>XGBoost</h3>

    <p>
    Machine Learning Model
    </p>

    <p class="status">
    ● ONLINE
    </p>

    </div>
    """, unsafe_allow_html=True)


with m2:

    st.markdown("""
    <div class="model-card">

    <div style="font-size:40px;">🧠</div>

    <h3>AFF-Net</h3>

    <p>
    Deep Learning Model
    </p>

    <p class="status">
    ● ONLINE
    </p>

    </div>
    """, unsafe_allow_html=True)


with m3:

    st.markdown("""
    <div class="model-card">

    <div style="font-size:40px;">🔐</div>

    <h3>Fraud Engine</h3>

    <p>
    Transaction Monitoring
    </p>

    <p class="status">
    ● ACTIVE
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

🏦 SecureBank AI Fraud Monitoring System

<br><br>

XGBoost • AFF-Net • Machine Learning • Deep Learning

<br>

AI-Based Financial Transaction Monitoring

</div>
""", unsafe_allow_html=True)