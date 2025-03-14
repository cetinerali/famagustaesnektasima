import streamlit as st
import yaml
from yaml.loader import SafeLoader
from streamlit_authenticator import Authenticate

# 🔹 Load Authentication Data
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config["credentials"],
    config["cookie"],
    config["key"],
    config["expiry_days"]
)

# 🔹 Set Up Streamlit UI
st.set_page_config(
    page_title="Famagusta Bus System",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🔹 Authentication System
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.write(f"Welcome *{name}*!")

    # 🔹 App Title
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Famagusta Bus System</h1>", unsafe_allow_html=True)

    # 🔹 Tabs for Different Features
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Map & Landmarks", "Route Planner", "Live Bus Tracking", "User Rewards", "Statistics"
    ])

    with tab1:
        st.subheader("Interactive Map with Landmarks")
        st.write("🚀 Coming soon: Displaying landmarks on a map!")

    with tab2:
        st.subheader("Route Planner")
        st.write("🛣️ Soon: Find the best bus routes!")

    with tab3:
        st.subheader("Live Bus Tracking")
        st.write("🚌 Simulated bus tracking will be added here.")

    with tab4:
        st.subheader("User Rewards & Notifications")
        st.write("🏆 See your energy & time savings!")

    with tab5:
        st.subheader("Usage Statistics")
        st.write("📊 Visualize transport data trends.")

elif authentication_status is False:
    st.error("Incorrect username or password. Please try again.")
elif authentication_status is None:
    st.warning("Please enter your username and password.")

