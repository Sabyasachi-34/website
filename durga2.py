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
    background-color: #f6f8f5;
}

/* HERO SECTION */
.hero {
    background: linear-gradient(135deg,#eef7e8,#dff0d4);
    padding: 45px;
    border-radius: 25px;
    color: #14532d;
    text-align: center;
    border: 1px solid #cfe8bf;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

/* PRODUCT CARD */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    transition: 0.3s;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 10px 25px rgba(34,197,94,0.18);
}

/* METRIC BOX */
.metric-card {
    background: white;
    color: #14532d;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid #d1fae5;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
}

/* BUTTON */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 48px;
    background: linear-gradient(90deg,#16a34a,#22c55e);
    color: white;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(90deg,#15803d,#16a34a);
    transform: scale(1.02);
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e5e7eb;
}

/* TITLES */
h1, h2, h3 {
    color: #14532d;
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 20px;
    color: gray;
}

/* SEARCH BAR */
input {
    border-radius: 10px !important;
}

/* SUCCESS BOX */
.stSuccess {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA
# --------------------------------------------------

products = [
    {
        "Model": "AW70GV",
        "Type": "Plough",
        "Price": "₹27,00,000",
        "subsidy": "40%",
        "Image": "https://www.yanmar.com/media/news/2019/12/13054632/img_index_0111.jpg"
    },
    {
        "Model": "Seeder S-120",
        "Type": "Seeder",
        "Price": "₹1,20,000",
        "Image": "https://i.ytimg.com/vi/yDK3Ddpcou4/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAqN96wh18FoO62lQbcqKapJRXLKQ"
    },
    {
        "Model": "Cultivator C-80",
        "Type": "Cultivator",
        "Price": "₹85,000",
        "Image": "https://www.yanmar.com/media/news/2019/12/13061653/img_index_028.jpg"
    }
]

products_df = pd.DataFrame(products)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.image(
    "https://img.icons8.com/color/96/tractor.png",
    width=120
)

st.sidebar.title("🚜 Durga Automobile")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Products", "Services", "Gallery", "About", "Contact"]
)

st.sidebar.markdown("---")

st.sidebar.success("🔧 Sales & Service Available")
st.sidebar.info("📍 Balasore & Baripada")

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "Home":

    st.markdown("""
    <div class='hero'>
        <h1>🚜 DURGA AUTOMOBILE</h1>
        <h3>Modern Agricultural Equipment Solutions</h3>
        <p>
        🛒 Sales &nbsp;&nbsp;&nbsp;
        🔧 Service &nbsp;&nbsp;&nbsp;
        ⚙️ Spare Parts &nbsp;&nbsp;&nbsp;
        🛡️ Maintenance
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # METRICS

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

            st.write(f"**Type:** {product['Type']}")
            st.write(f"**Price:** {product['Price']}")

            if st.button(f"🚀 Enquire Now - {product['Model']}"):
                st.success(f"Thank you for showing interest in {product['Model']}")
                st.balloons()

            st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.subheader("⭐ Customer Reviews")

    r1, r2 = st.columns(2)

    with r1:
        st.info("⭐⭐⭐⭐⭐ Excellent quality machinery and fast service support.")

    with r2:
        st.info("⭐⭐⭐⭐⭐ Trusted agricultural equipment dealer in Odisha.")

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
    st.write("📍 Near Dargadahi golei, Baripada")

# --------------------------------------------------
# CONTACT PAGE
# --------------------------------------------------

elif page == "Contact":

    st.title("📞 Contact Us")

    st.markdown("""
    <div class='card'>
    <h3>Get In Touch</h3>
    <p>📍 Remuna Golei, Balasore, Odisha</p>
    <p>📞 +91 7008490069</p>
    <p>📧 durgaautomobile6@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("### 💬 Direct WhatsApp")

    whatsapp_url = "https://wa.me/9438756540"

    st.markdown(
        f"""
        <a href='{whatsapp_url}' target='_blank'>
            <button style='background-color:#16a34a;
            color:white;
            padding:12px;
            border:none;
            border-radius:10px;
            font-size:16px;
            font-weight:bold;'>
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
    © {current_year} DURGA AUTOMOBILE | Designed by deVSabya 🚜
    </div>
    """,
    unsafe_allow_html=True
)
