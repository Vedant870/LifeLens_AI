# main.py

import streamlit as st
import datetime
import random

# Set up page
st.set_page_config(
    page_title="LifeLens_AI Dashboard",
    layout="wide",
    page_icon="🌿"
)

# ───────────────────────────────────────────────────────────────
# Title Section
st.markdown("""
    <style>
        .title-text {
            font-size: 42px;
            font-weight: bold;
            color: #4CAF50;
        }
        .sub-text {
            font-size: 18px;
            color: #aaaaaa;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title-text">🌿 LifeLens_AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">An AI agent-based lifestyle dashboard for Productivity & Sustainability – Microsoft Hackathon Project</p>', unsafe_allow_html=True)

st.markdown("---")

# ───────────────────────────────────────────────────────────────
# Sidebar – User Input
st.sidebar.header("📋 Daily Check-In")

name = st.sidebar.text_input("Your Name", "Vedant")
wake_time = st.sidebar.time_input("⏰ Wake-up Time", datetime.time(7, 0))
work_hours = st.sidebar.slider("💼 Hours Worked Today", 0, 16, 8)
steps = st.sidebar.number_input("🚶 Steps Walked", 0, 25000, step=500)
water = st.sidebar.slider("💧 Glasses of Water", 0, 15, 8)
meals = st.sidebar.slider("🍱 Meals Taken", 0, 5, 3)
mood = st.sidebar.selectbox("🙂 Mood Today", ["😄 Happy", "😐 Okay", "😫 Tired", "😢 Low"])

st.sidebar.markdown("---")
date_today = st.sidebar.date_input("📅 Today's Date", datetime.date.today())

# ───────────────────────────────────────────────────────────────
# Scoring Logic
def get_productivity_feedback(hours):
    if hours >= 9:
        return "💪 Super Productive", 90
    elif hours >= 6:
        return "👍 Good Effort", 70
    elif hours >= 4:
        return "😐 Average", 50
    else:
        return "😴 Low Productivity", 30

def get_sustainability_tip(steps, water, meals):
    tips = [
        "Use public transport twice a week to reduce emissions.",
        "Avoid food waste by planning your meals.",
        "Drink more water – it helps with energy too!",
        "Opt for local organic produce where possible.",
        "Walk or cycle for short distances. Great for you and the planet!"
    ]
    if steps > 8000 and water >= 8 and meals == 3:
        return "🌍 Excellent sustainable habits today! Keep it up!"
    else:
        return random.choice(tips)

# ───────────────────────────────────────────────────────────────
# Main Dashboard Display

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"👤 Daily Overview for {name}")
    st.write(f"**Wake-Up Time:** {wake_time.strftime('%I:%M %p')}")
    st.write(f"**Mood:** {mood}")
    st.write(f"**Date:** {date_today.strftime('%A, %d %B %Y')}")

with col2:
    st.subheader("🧠 AI-Based Productivity Summary")
    productivity_status, score = get_productivity_feedback(work_hours)
    st.write(f"**Worked Hours:** {work_hours} hrs — {productivity_status}")
    st.progress(score / 100)

# ───────────────────────────────────────────────────────────────
st.markdown("---")
st.subheader("📊 Health & Lifestyle Stats")

col3, col4, col5 = st.columns(3)

with col3:
    st.metric(label="🚶 Steps", value=f"{steps:,}")
    st.progress(min(steps / 10000, 1.0))

with col4:
    st.metric(label="💧 Water Intake", value=f"{water} Glasses")
    st.progress(min(water / 10, 1.0))

with col5:
    st.metric(label="🍱 Meals", value=f"{meals}/3")
    st.progress(min(meals / 3, 1.0))

# ───────────────────────────────────────────────────────────────
st.markdown("---")
st.subheader("💡 AI-Generated Sustainability Tip")
st.success(get_sustainability_tip(steps, water, meals))

# ───────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("📌 *Developed with ❤️ for the Microsoft Hackathon 2025*")

