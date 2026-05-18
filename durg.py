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

/* -----------------------------
BACKGROUND
------------------------------*/
.main {
    background: linear-gradient(135deg,#eefdf3,#d7f5e5,#f6fff8);
}

/* -----------------------------
GLOBAL
------------------------------*/
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* -----------------------------
HERO SECTION
------------------------------*/
.hero {
    background: linear-gradient(135deg,#064e3b,#065f46,#16a34a);
    padding: 60px;
    border-radius: 28px;
    color: white;
    text-align: center;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.25);
    animation: glow 4s infinite alternate;
}

.hero h1 {
    font-size: 55px;
    font-weight: 800;
}

.hero h3 {
    color: #d1fae5;
}

@keyframes glow {
    from {
        box-shadow: 0px 0px 20px rgba(34,197,94,0.3);
    }
    to {
        box-shadow: 0px 0px 40px rgba(34,197,94,0.7);
    }
}

/* -----------------------------
CARD
------------------------------*/
.card {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(14px);
    padding: 22px;
    border-radius: 24px;
    transition: 0.4s;
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0px 15px 35px rgba(16,185,129,0.35);
}

/* -----------------------------
METRIC CARDS
------------------------------*/
.metric-card {
    background: linear-gradient(135deg,#ffffff,#ecfdf5);
    padding: 25px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid #d1fae5;
    transition: 0.3s;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.08);
}

.metric-card:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg,#dcfce7,#bbf7d0);
}

/* -----------------------------
BUTTONS
------------------------------*/
.stButton>button {
    width: 100%;
    border-radius: 14px;
    height: 52px;
    border: none;
    font-weight: bold;
    font-size: 16px;
    color: white;
    background: linear-gradient(90deg,#10b981,#22c55e,#84cc16);
    box-shadow: 0px 5px 20px rgba(34,197,94,0.4);
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg,#059669,#16a34a,#65a30d);
    box-shadow: 0px 8px 28px rgba(34,197,94,0.7);
}

/* -----------------------------
SIDEBAR
------------------------------*/
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#052e16,#064e3b);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* -----------------------------
INPUTS
------------------------------*/
input, textarea {
    border-radius: 12px !important;
    border: 1px solid #bbf7d0 !important;
    padding: 10px !important;
}

/* -----------------------------
DATAFRAME
------------------------------*/
[data-testid="stDataFrame"] {
    border-radius: 20px;
    overflow: hidden;
}

/* -----------------------------
HEADINGS
------------------------------*/
h1, h2, h3 {
    color: #065f46;
}

/* -----------------------------
FOOTER
------------------------------*/
.footer {
    text-align: center;
    padding: 25px;
    color: #4b5563;
    font-weight: 500;
}

/* -----------------------------
IMAGES
------------------------------*/
img {
    border-radius: 18px;
    transition: 0.3s;
}

img:hover {
    transform: scale(1.02);
}

/* -----------------------------
SCROLLBAR
------------------------------*/
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(#16a34a,#22c55e);
    border-radius: 10px;
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
        "Image": "https://www.yanmar.com/media/news/2019/12/13054632/img_index_0111.jpg"
    },
    {
        "Model": "Seeder S-120",
        "Type": "Seeder",
        "Price": "₹1,20,000",
        "Image": "https://i.ytimg.com/vi/yDK3Ddpcou4/hq720.jpg"
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

    metrics = [
        ("500+", "Happy Farmers"),
        ("50+", "Machines Sold"),
        ("24x7", "Support"),
        ("10+", "Years Experience")
    ]

    for col, metric in zip([c1, c2, c3, c4], metrics):

        with col:
            st.markdown(f"""
            <div class='metric-card'>
            <h2>{metric[0]}</h2>
            <p>{metric[1]}</p>
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

    services = [
        ("Repairing", "Complete maintenance support."),
        ("Spare Parts", "Original spare parts with warranty."),
        ("Annual Service", "Affordable servicing packages.")
    ]

    for col, service in zip([s1, s2, s3], services):

        with col:
            st.markdown(f"""
            <div class='card'>
            <h3>{service[0]}</h3>
            <p>{service[1]}</p>
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
    st.write("📍 Near Dargadahi Golei, Baripada")

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
            <button style='background:linear-gradient(90deg,#10b981,#22c55e);
            color:white;
            padding:14px 20px;
            border:none;
            border-radius:12px;
            font-size:16px;
            font-weight:bold;
            cursor:pointer;
            box-shadow:0px 5px 20px rgba(34,197,94,0.4);'>
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
    © {current_year} DURGA AUTOMOBILE | Designed by deVSabya.exe 🚀
    </div>
    """,
    unsafe_allow_html=True
)
