import streamlit as st
from PIL import Image
import base64
from pathlib import Path
import pandas as pd

# -----------------------
# Configuration
# -----------------------
st.set_page_config(page_title="Durga Automobile", layout="wide")
SHOWROOM_NAME = "Durga Automobile"
BACKGROUND_PATH = r"C:\Users\dsaby\OneDrive\Desktop\har.webp"  # change if you move the file

# -----------------------
# Helper: set background image from a local file (embedded as base64)
# -----------------------
def set_background(local_img_path: str):
    img_path = Path(local_img_path)
    if not img_path.exists():
        st.warning(f"Background image not found at {local_img_path}. Remove or fix the path in the script.")
        return
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/webp;base64,{data}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .card {{
        background: rgba(255,255,255,0.85);
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# -----------------------
# Layout / Navigation
# -----------------------
set_background(BACKGROUND_PATH)

st.markdown("<div class='card'>", unsafe_allow_html=True)
col1, col2 = st.columns([3,1])
with col1:
    st.title(SHOWROOM_NAME)
    st.write("**Sales & Service — Agricultural Equipment**")
with col2:
    st.image("https://img.icons8.com/emoji/48/000000/tractor-emoji.png", width=48)
st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Products", "Services", "About", "Contact"])

# -----------------------
# Sample data (editable)
# -----------------------
products = [
    {"Model": "Plough P-50", "Type": "Plough", "Price": "₹ 45,000", "Stock": 10},
    {"Model": "Seeder S-120", "Type": "Seeder", "Price": "₹ 1,20,000", "Stock": 5},
    {"Model": "Cultivator C-80", "Type": "Cultivator", "Price": "₹ 85,000", "Stock": 4},
]
products_df = pd.DataFrame(products)

# -----------------------
# Pages
# -----------------------
if page == "Home":
    st.header("Welcome to Durga Automobile")
    st.write(
        "We sell and service ploughs, seeders, cultivators, and other agricultural machinery."
        "Use the sidebar to browse products, read about our services, or contact us."
    )

    st.subheader("Featured Equipment")
    cols = st.columns(3)
    for i, c in enumerate(cols):
        with c:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            if i < len(products):
                st.subheader(products[i]["Model"])
                st.write(products[i]["Type"])
                st.write(products[i]["Price"])
            else:
                st.subheader("Equipment")
                st.write("Details unavailable")
            st.button(f"Enquire {i+1}")
            st.markdown("</div>", unsafe_allow_html=True)

elif page == "Products":
    st.header("Products")
    st.write("Browse the equipment we offer. Click a row to enquire.")
    st.dataframe(products_df)

    # Quick enquiry
    st.subheader("Quick Enquiry")
    with st.form("enq_form"):
        name = st.text_input("Your name")
        phone = st.text_input("Phone / WhatsApp")
        model = st.selectbox("Interested model", products_df["Model"].tolist())
        msg = st.text_area("Message", "I am interested in ...")
        submitted = st.form_submit_button("Send Enquiry")
        if submitted:
            st.success("Thanks! Your enquiry has been received. We'll contact you soon.")
            st.write("Summary:", name, phone, model)

elif page == "Services":
    st.header("Sales & Service")
    st.write("We provide: On-site maintenance and repairs \n Spare parts ordering \n Annual servicing packages")


    st.subheader("Book a Service")
    with st.form("service_form"):
        s_name = st.text_input("Owner name")
        s_model = st.text_input("Equipment model")
        s_date = st.date_input("Preferred date")
        s_notes = st.text_area("Notes (faults, symptoms)")
        s_submit = st.form_submit_button("Book Service")
        if s_submit:
            st.success("Service request received. We'll confirm the slot by phone.")

elif page == "About":
    st.header("About Durga Automobile")
    st.write(
        "Durga Automobile is a local dealership and service center specializing in agricultural machinery."
        "We focus on dependable machines, prompt service, and helping farmers get the most from their equipment."
    )
    st.write("Location: Remuna Golei, Balasore, Odisha & Baripada")

elif page == "Contact":
    st.header("Contact Us")
    st.write("Address: Remuna Golei, Balasore, Odisha.")
    st.write("\n Phone: +9123456789 \n ")
    st.write("info:info@durgaautomobile.example ")
 

# -----------------------
# Footer
# -----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<small>Built with ❤️ for farmers — edit the Python file to customize models, prices, images and contact details.</small>", unsafe_allow_html=True)
