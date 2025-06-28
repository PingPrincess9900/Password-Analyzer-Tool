import streamlit as st
import re

# Password strength analyzer logic
def analyze_password(password):
    strength = ""
    suggestions = []

    if len(password) < 6:
        strength = "Weak"
        suggestions.append("Too short (minimum 6 characters).")
    elif len(password) < 10:
        strength = "Moderate"
        suggestions.append("Make it longer for better security.")
    else:
        strength = "Strong"

    if not re.search(r"[A-Z]", password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Include at least one lowercase letter.")
    if not re.search(r"\d", password):
        suggestions.append("Include at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Include special characters.")

    return strength, suggestions

# Streamlit UI
st.set_page_config(page_title="Password Analyzer", page_icon="🔐")
st.title("🔐 Password Strength Analyzer")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, tips = analyze_password(password)
    st.subheader(f"Strength: {strength}")
    if tips:
        st.write("Suggestions to improve:")
        for tip in tips:
            st.write("✅", tip)
    else:
        st.success("Your password is strong.")
