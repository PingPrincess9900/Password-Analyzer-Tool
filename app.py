import streamlit as st
import math
import re
import pandas as pd

# Function to calculate entropy
def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32
    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

# Function to analyze password
def analyze_password(password):
    strength = "Strong"
    suggestions = []

    if len(password) < 6:
        strength = "Weak"
        suggestions.append("Password is too short.")
    elif len(password) < 10:
        strength = "Moderate"
        suggestions.append("Make it longer for better security.")

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Add at least one lowercase letter.")
    if not re.search(r"\d", password):
        suggestions.append("Add at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Add at least one special character.")

    return strength, suggestions

# UI
st.set_page_config(page_title="Password Analyzer", page_icon="🔐")
st.title("🔐 Password Strength Analyzer Tool")

# Record all results
records = []

# Single password input
st.subheader("🔍 Analyze a Single Password")
password = st.text_input("Enter a password to analyze:", type="password")

if password:
    strength, tips = analyze_password(password)
    entropy = calculate_entropy(password)

    st.markdown(f"**Strength:** {strength}")
    st.markdown(f"**Entropy:** {entropy} bits")

    if tips:
        st.write("Suggestions:")
        for tip in tips:
            st.write("✅", tip)
    else:
        st.success("Great! Your password looks strong.")

    records.append({"Password": password, "Strength": strength, "Entropy": entropy})

# CSV Upload Section
st.subheader("📁 Upload a CSV File of Passwords")
uploaded_file = st.file_uploader("Upload CSV file (must have a column named 'password')", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if 'password' not in df.columns:
            st.error("CSV must contain a column named 'password'")
        else:
            results = []
            for pw in df['password']:
                strength, tips = analyze_password(str(pw))
                entropy = calculate_entropy(str(pw))
                results.append({
                    "Password": pw,
                    "Strength": strength,
                    "Entropy": entropy
                })

            result_df = pd.DataFrame(results)
            st.success("Analysis complete!")
            st.dataframe(result_df)

            # Download option
            csv = result_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name='password_analysis_results.csv',
                mime='text/csv',
            )
    except Exception as e:
        st.error(f"Error processing file: {e}")
