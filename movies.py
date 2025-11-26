# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

st.set_page_config(page_title="Movie Rating — Styled", layout="wide", initial_sidebar_state="expanded")
sns.set_style("darkgrid")
st.title("🎬 Movie Rating Analysis — Styled")

# -------------------------
# Helper: image -> base64
# -------------------------
def file_to_base64(path_or_bytes):
    """
    Accepts either a local path (string) or bytes and returns base64 string.
    """
    if isinstance(path_or_bytes, (bytes, bytearray)):
        data = path_or_bytes
    else:
        try:
            with open(path_or_bytes, "rb") as f:
                data = f.read()
        except Exception:
            return None
    return base64.b64encode(data).decode()

# -------------------------
# Sidebar: background controls
# -------------------------
st.sidebar.header("Background & style")

# Developer-provided default local path (from your session)
DEFAULT_BG_PATH = "/mnt/data/25novseaborn.pdf"

uploaded_bg = st.sidebar.file_uploader("Upload background image (png/jpg) to override default", type=["png", "jpg", "jpeg"])
overlay_opacity = st.sidebar.slider("Overlay opacity (0 = none, 1 = solid)", 0.0, 0.9, 0.45, 0.05)
content_blur = st.sidebar.slider("Background blur (px)", 0, 15, 6, 1)
card_opacity = st.sidebar.slider("Card background opacity", 0.0, 1.0, 0.75, 0.05)

# Build CSS for background
bg_b64 = None
if uploaded_bg is not None:
    # Use uploaded image bytes
    bg_b64 = file_to_base64(uploaded_bg.read())
else:
    # Fallback to the default path from your session (developer instruction)
    bg_b64 = file_to_base64(DEFAULT_BG_PATH)

# If the default file isn't an image, bg_b64 may be None — the CSS still provides gradient fallback.
bg_css = ""
if bg_b64:
    bg_css = f"data:image/png;base64,{bg_b64}"

# -------------------------
# Inject CSS
# -------------------------
custom_css = f"""
<style>
/* Page background */
[data-testid="stAppViewContainer"] > .main {{
  background-image: linear-gradient(rgba(10,10,15,{overlay_opacity}), rgba(20,20,30,{overlay_opacity})), url('{bg_css}');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  filter: blur(0px);
  min-height: 100vh;
}}

/* Create a frosted glass card for main content */
.frosted-card {{
  background: rgba(255,255,255,{card_opacity});
  -webkit-backdrop-filter: blur({content_blur}px);
  backdrop-filter: blur({content_blur}px);
  border-radius: 14px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.35);
  padding: 18px;
  margin: 16px 8px;
}}

/* Title style */
h1 {{
  color: #fff;
  text-shadow: 0 2px 8px rgba(0,0,0,0.7);
}}

/* Make sidebar semi-transparent */
[data-testid="stSidebar"] {{
  background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
  backdrop-filter: blur(6px);
  border-right: 1px solid rgba(255,255,255,0.06);
}}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------
# Load movie CSV
# -------------------------
uploaded_file = st.file_uploader("Upload Movie-Rating.csv", type=["csv"], key="movies_csv")
if uploaded_file is None:
    st.warning("Please upload `Movie-Rating.csv` to see visualizations. (Use the uploader above.)")
    st.info("Tip: you can also upload a background image in the sidebar for a prettier background.")
    st.stop()

movies = pd.read_csv(uploaded_file)
# rename columns as in original notebook
movies.columns = ["Film", "Genre", "Criticrating", "Audicencerating", "Budgetmillion", "Year"]
movies["Film"] = movies["Film"].astype("category")
movies["Genre"] = movies["Genre"].astype("category")

# -------------------------
# Main content inside frosted card
# -------------------------
st.markdown('<div class="frosted-card">', unsafe_allow_html=True)

# Top row: data preview + stats
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("Data preview")
    st.dataframe(movies.head(), height=240)
with col2:
    st.subheader("Summary stats")
    st.write(movies.describe())

# Visual controls
st.markdown("---")
st.subheader("Visualizations")

# Jointplot controls
jt_col1, jt_col2 = st.columns([1, 1])
with jt_col1:
    joint_type = st.selectbox("Jointplot type", ["hex", "scatter", "reg", "kde", "hist", "resid"])
with jt_col2:
    show_hue = st.checkbox("Color by Genre (lmplot/hue)", value=True)

# Plot 1: jointplot
fig = sns.jointplot(data=movies, x="Criticrating", y="Audicencerating", kind=joint_type)
st.pyplot(fig)
plt.close()

# Plot 2: distribution
st.markdown("### Distribution")
dist_choice = st.selectbox("Distribution column", ["Audicencerating", "Criticrating", "Budgetmillion"])
fig2, ax2 = plt.subplots(figsize=(8, 3.5))
sns.histplot(movies[dist_choice], bins=20, kde=True, ax=ax2)
st.pyplot(fig2)
plt.close(fig2)

# Genre budget stacked
st.markdown("### Genre-wise Budget (stacked)")
genres = movies.Genre.unique().tolist()[:6]  # keep top few for clarity
fig3, ax3 = plt.subplots(figsize=(10, 3.5))
plt.hist([movies[movies.Genre == g].Budgetmillion for g in genres], bins=20, stacked=True, label=genres)
plt.legend()
st.pyplot(fig3)
plt.close(fig3)

# Lmplot/hue
st.markdown("### Scatter (lmplot)")
if show_hue:
    fig4 = sns.lmplot(data=movies, x="Criticrating", y="Audicencerating", fit_reg=False, hue="Genre", aspect=1.4)
else:
    fig4 = sns.lmplot(data=movies, x="Criticrating", y="Audicencerating", fit_reg=False, aspect=1.4)
st.pyplot(fig4)
plt.close()

# Box + violin
st.markdown("### Box & Violin (Critic rating by Genre)")
b1, b2 = st.columns(2)
with b1:
    fig5, ax5 = plt.subplots(figsize=(8,3.5))
    sns.boxplot(data=movies, x="Genre", y="Criticrating", ax=ax5)
    plt.xticks(rotation=45)
    st.pyplot(fig5)
    plt.close(fig5)
with b2:
    fig6, ax6 = plt.subplots(figsize=(8,3.5))
    sns.violinplot(data=movies, x="Genre", y="Criticrating", ax=ax6)
    plt.xticks(rotation=45)
    st.pyplot(fig6)
    plt.close(fig6)

st.markdown('</div>', unsafe_allow_html=True)
