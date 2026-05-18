
import streamlit as st
import pandas as pd
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Durga Automobile",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

.hero {
    background: linear-gradient(135deg,#1e293b,#0f172a);
    padding: 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    box-shadow: 0px 0px 25px rgba(255,255,255,0.1);
}

.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 18px;
    transition: 0.3s;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 10px 30px rgba(255,165,0,0.3);
}

.metric-card {
    background: linear-gradient(135deg,#f97316,#ea580c);
    color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.big-btn button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    background-color: orange;
    color: white;
    font-weight: bold;
}

.footer {
    text-align: center;
    padding: 20px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA
# --------------------------------------------------
products = [
    {
        "Model": "Plough P-50",
        "Type": "Plough",
        "Price": "₹45,000",
        "Stock": 10,
        "Image": "https://images.unsplash.com/photo-1592982537447-7440770cbfc9"
    },
    {
        "Model": "Seeder S-120",
        "Type": "Seeder",
        "Price": "₹1,20,000",
        "Stock": 5,
        "Image": "https://images.unsplash.com/photo-1500937386664-56d1dfef3854"
    },
    {
        "Model": "Cultivator C-80",
        "Type": "Cultivator",
        "Price": "₹85,000",
        "Stock": 4,
        "Image": "https://images.unsplash.com/photo-1464226184884-fa280b87c399"
    }
]

products_df = pd.DataFrame(products)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.image(
    "https://img.icons8.com/emoji/96/tractor-emoji.png",
    width=90
)

st.sidebar.title("🚜 Durga Automobile")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Products", "Services", "Gallery", "About", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.success("Sales & Service Available")
st.sidebar.info("📍 Balasore & Baripada")

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if page == "Home":

    st.markdown("""
    <div class='hero'>
        <h1>🚜 DURGA AUTOMOBILE</h1>
        <h3>Modern Agricultural Equipment Solutions</h3>
        <p>Sales • Service • Spare Parts • Maintenance</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Metrics
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class='metric-card'>
        <h2>500+</h2>
        <p>Happy Farmers</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='metric-card'>
        <h2>50+</h2>
        <p>Machines Sold</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric-card'>
        <h2>24x7</h2>
        <p>Support</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class='metric-card'>
        <h2>10+</h2>
        <p>Years Experience</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.subheader("🔥 Featured Equipment")

    cols = st.columns(3)

    for idx, product in enumerate(products):
        with cols[idx]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.image(product["Image"], use_container_width=True)
            st.subheader(product["Model"])
            st.write(f"Type: {product['Type']}")
            st.write(f"Price: {product['Price']}")
            st.write(f"Stock Available: {product['Stock']}")

            if st.button(f"🚀 Enquire Now - {product['Model']}"):
                st.success(f"Thank you for showing interest in {product['Model']}")
                st.balloons()

            st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.subheader("⭐ Customer Reviews")

    review1, review2 = st.columns(2)

    with review1:
        st.info("⭐⭐⭐⭐⭐ Excellent machine quality and service support.")

    with review2:
        st.info("⭐⭐⭐⭐⭐ Affordable agricultural equipment with fast servicing.")

# --------------------------------------------------
# PRODUCTS PAGE
# --------------------------------------------------
elif page == "Products":

    st.title("🛒 Products")

    search = st.text_input("🔍 Search Product")

    filtered_df = products_df[
        products_df["Model"].str.contains(search, case=False)
    ]

    st.dataframe(filtered_df, use_container_width=True)

    st.write("")

    st.subheader("📩 Quick Enquiry")

    with st.form("enquiry_form"):

        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        product = st.selectbox(
            "Select Product",
            products_df["Model"].tolist()
        )

        message = st.text_area(
            "Message",
            "I want more information about this product."
        )

        submit = st.form_submit_button("Send Enquiry")

        if submit:
            st.success("✅ Enquiry Submitted Successfully")
            st.toast("Our team will contact you soon")
            st.balloons()

# --------------------------------------------------
# SERVICES PAGE
# --------------------------------------------------
elif page == "Services":

    st.title("🛠 Services")

    s1, s2, s3 = st.columns(3)

    with s1:
        st.markdown("""
        <div class='card'>
        <h3>Repairing</h3>
        <p>Complete maintenance support for agricultural equipment.</p>
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown("""
        <div class='card'>
        <h3>Spare Parts</h3>
        <p>Original spare parts with warranty support.</p>
        </div>
        """, unsafe_allow_html=True)

    with s3:
        st.markdown("""
        <div class='card'>
        <h3>Annual Service</h3>
        <p>Affordable annual servicing packages for farmers.</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("📅 Book Service")

    with st.form("service_form"):

        owner = st.text_input("Owner Name")
        machine = st.text_input("Machine Model")
        service_date = st.date_input("Preferred Date")
        issue = st.text_area("Describe Issue")

        service_submit = st.form_submit_button("Book Service")

        if service_submit:
            st.success("✅ Service Booking Confirmed")
            st.toast("Technician will contact you shortly")

# --------------------------------------------------
# GALLERY PAGE
# --------------------------------------------------
elif page == "Gallery":

    st.title("📸 Equipment Gallery")

    g1, g2, g3 = st.columns(3)

    with g1:
        st.image(products[0]["Image"], caption="Plough Machine")

    with g2:
        st.image(products[1]["Image"], caption="Seeder Machine")

    with g3:
        st.image(products[2]["Image"], caption="Cultivator Machine")

# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------
elif page == "About":

    st.title("🏢 About Us")

    st.markdown("""
    <div class='card'>
    <h3>Durga Automobile</h3>
    <p>
    Durga Automobile is a trusted agricultural machinery dealer and service center.
    We provide high-quality farming equipment, fast maintenance service,
    and customer support for modern farmers.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("📍 Remuna Golei, Balasore, Odisha")
    st.write("📍 Baripada Branch Available")

# --------------------------------------------------
# CONTACT PAGE
# --------------------------------------------------
elif page == "Contact":

    st.title("📞 Contact Us")

    st.markdown("""
    <div class='card'>
    <h3>Get In Touch</h3>
    <p>📍 Remuna Golei, Balasore, Odisha</p>
    <p>📞 +91 9876543210</p>
    <p>📧 info@durgaautomobile.com</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("### 💬 Direct WhatsApp")

    whatsapp_url = "https://wa.me/919876543210"

    st.markdown(
        f"""
        <a href='{whatsapp_url}' target='_blank'>
            <button style='background-color:green;color:white;padding:12px;border:none;border-radius:10px;'>
                Open WhatsApp Chat
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")

current_year = datetime.now().year

st.markdown(
    f"""
    <div class='footer'>
    © {current_year} DURGA AUTOMOBILE | Designed with Streamlit 🚜
    </div>
    """,
    unsafe_allow_html=True
)

