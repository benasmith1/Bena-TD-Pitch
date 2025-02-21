#Import necessary libraries
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.set_page_config(
    page_title = "Home",
    page_icon = "🌉",
    # layout = "wide"
)


# Centered Title using HTML and Markdown
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Mito Labs</h2>
    """,
    unsafe_allow_html = True,
)

col1, col2, col3 = st.columns(3)
with col2:
    st.image("Figures/MitoLabs.jpeg", caption="Mito Labs Logo")


# Subtitle with styling
st.markdown(
    """
    <h4 style = "text-align: center; color: #9E6AC7; font-family: Arial, sans-serif;">
    Discover insights about Mito Labs!
    </h4>
    """,
    unsafe_allow_html = True,
)

# Insert an image
#st.sidebar.image("Figures/houses_sidebar.jpeg", caption="California Houses")


# Sidebar navigation header
with st.sidebar:
    st.header("🔍 Navigate the App")
    st.write("Use the links above to explore:")
    st.markdown("""
    - **Sentiment Analysis**: Explore sentiments about MitoLabs on the web.
    - **AI Agent Trends**: Time series analysis of AI agent google searches.
    """)

st.sidebar.info("Select a task above to proceed.")

# Interactive introduction with expander
with st.expander("**What can you do with this app?**", expanded=True):
    st.write("""
    😃 **Explore how users feel about Mito Labs**: Leveraging sentiment analysis on webpages mentioning Mito spreadsheets, we can view the overall opinions of users about this app. Using the OpenAI API, we can find popular phrases in these webpages to see what users like about the Mito application and what can be improved.
    
    🌆 **Analyze the popularity of AI agents**: Using the Newey-West estimator for time series data and a Poisson generalized linear model, we can describe how search results for AI agents have changed over time. 
             
    """)


# Add a footer
st.markdown(
    """
    <hr>
    <p style = "text-align: center; color: #777; font-size: 14px; font-family: Arial, sans-serif;">
    Made with ❤️ by Bena Smith.
    </p>
    """,
    unsafe_allow_html = True,
)
