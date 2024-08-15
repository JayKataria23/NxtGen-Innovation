import streamlit as st

# Set page config
st.set_page_config(page_title="NxtGen Innovation", page_icon="""<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg">
  <defs>
  </defs>
  <rect width="40" height="40" fill="white"/>
  <text x="5" y="35" font-family="Arial, sans-serif" font-size="40" font-weight="bold">
        <tspan fill="#4CAF50">N</tspan>
      </text>
</svg>
""", layout="wide")

# Custom CSS to set theme colors
st.markdown("""
    <style>
    .st-emotion-cache-p5msec:hover {
        color: #4CAF50
            }
    .stApp {
        background-color: #fff;
    }
    .main > div {
        padding-top: 2rem;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #4CAF50;
        border-color: #4CAF50;
    }
    .stExpander {
        border-color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo
st.image("./NxtGen.png", width=500)

# Main title
st.title("Welcome to NxtGen Innovation")

# Introduction
st.markdown("""
NxtGen Innovation is a leading technology solutions provider specializing in Data Center management, 
Cloud services, IoT (Internet of Things), Security solutions, Networking, and the integration of New 
Technology Innovations. We are committed to driving digital transformation and delivering cutting-edge 
solutions that empower businesses to stay ahead in an ever-evolving technological landscape.
""")

# Core Services
st.header("Our Core Services")
services = {
    "Data Center Solutions": ["Design & Implementation", "Managed Services", "Disaster Recovery"],
    "Cloud Services": ["Cloud Strategy & Migration", "Multi-Cloud Management", "Cloud Security"],
    "IoT (Internet of Things)": ["IoT Solutions Development", "Smart Infrastructure", "Data Analytics"],
    "Security Solutions": ["Cybersecurity Services", "Network Security", "Compliance & Risk Management"],
    "Networking Solutions": ["Network Design & Implementation", "Wireless Networking", "Network Optimization"],
    "New Technology Innovations": ["Artificial Intelligence & Machine Learning", "Blockchain", "Edge Computing"],
    "Gen AI": ["Chat Bots", "Data Entry", "Consumer Sentiment Analysis"]
}

for service, details in services.items():
    with st.expander(service):
        for detail in details:
            st.write(f"- {detail}")

# Industry Expertise
st.header("Industry Expertise")
industries = ["Finance", "Healthcare", "Manufacturing", "Retail", "Energy"]
st.write("We serve a diverse range of industries, including:")
for industry in industries:
    st.write(f"- {industry}")

# Our Approach
st.header("Our Approach")
approach_steps = [
    "Consultation: We begin by understanding your business objectives, challenges, and IT environment.",
    "Design & Planning: Our experts design tailored solutions that align with your goals and future growth.",
    "Implementation: Seamless execution with minimal disruption, ensuring your business operations continue smoothly.",
    "Support & Optimization: Ongoing support and optimization to ensure peak performance and adaptability to new challenges."
]
for step in approach_steps:
    st.write(f"- {step}")

# Why Choose Us
st.header("Why Choose Us?")
reasons = [
    "Expertise: Decades of experience in IT infrastructure, cloud, IoT, and security.",
    "Tailored Solutions: Custom solutions designed to meet your specific needs.",
    "Customer-Centric: A commitment to understanding and addressing the unique challenges of our clients.",
    "Innovation-Driven: Always at the forefront of technology, providing innovative solutions that drive business success."
]
for reason in reasons:
    st.write(f"- {reason}")

# Contact Information
st.header("Contact Us")
st.write("For more information about how NxtGen Innovation can help your business achieve its technology goals, please contact us:")
st.write("[Your Name]")
st.write("[Your Position]")
st.write("[Your Email Address]")
st.write("[Your Phone Number]")
st.write("[Company Website URL]")

# Contact form
st.subheader("Get in Touch")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button("Send Message")

# Footer
st.markdown("---")
st.write("NxtGen Innovation is committed to empowering businesses with innovative technology solutions. Let's work together to build a smarter, more secure, and connected future.")