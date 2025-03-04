import re
import random
import string
import streamlit as st
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- LOAD STYLES ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- PASSWORD STRENGTH CHECKER ---
def check_password_strength(password: str) -> int:
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    return score

def get_strength_feedback(score: int) -> str:
    if score == 4:
        return "🟢 Strong Password!"
    elif score == 3:
        return "🟡 Moderate Password - Consider adding more security features."
    else:
        return "🔴 Weak Password - Improve it using the suggestions above."

# --- PASSWORD GENERATOR ---
def generate_password(length: int, complexity: int) -> str:
    characters = string.ascii_lowercase
    if complexity > 1:
        characters += string.ascii_uppercase
    if complexity > 2:
        characters += string.digits
    if complexity > 3:
        characters += "!@#$%^&*"
    
    return ''.join(random.choice(characters) for _ in range(length))

# --- UI LAYOUT ---
st.title("🔐 Password Strength Meter")
st.write("Check the strength of your password and get improvement suggestions!")

# --- PASSWORD INPUT ---
password = st.text_input("Enter a Password:", type="password")

if password:
    score = check_password_strength(password)
    feedback = get_strength_feedback(score)
    
    # --- VISUAL FEEDBACK ---
    st.markdown(f"### {feedback}")
    st.progress(score / 4)

# --- PASSWORD GENERATOR ---
st.write("---")
st.header("🛠️ Generate a Strong Password")

length = st.slider("Password Length", min_value=8, max_value=32, value=12, step=1)
complexity = st.selectbox(
    "Select Complexity Level",
    options=[1, 2, 3, 4],
    format_func=lambda x: [
        "🔤 Lowercase Only",
        "🔡 Lower & Uppercase",
        "🔢 Letters & Numbers",
        "🔣 Letters, Numbers & Symbols"
    ][x-1]
)

if st.button("Generate Password"):
    generated_password = generate_password(length, complexity)
    st.code(generated_password, language="")



# Footer
st.markdown("<p style='text-align: center; color: grey;'>Developed with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)

# --- SIDEBAR TIPS ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4359/4359875.png", width=100)
st.sidebar.header("💡 Password Security Tips")
st.sidebar.info("""
- Use at least 8 characters.
- Mix uppercase, lowercase, numbers, and symbols.
- Avoid common passwords (e.g., "password123").
- Do not reuse passwords across sites.
- Consider using a password manager.
""")

# Add a 'Contact Us' section
st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")

# Email Link
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")

# LinkedIn Link
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")

# WhatsApp Link
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")
