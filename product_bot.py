import streamlit as st
import requests

# 🔧 Update this to your LangGraph agent API URL
AGENT_API_URL = "http://localhost:8080/run-agent"  # or remote endpoint

st.set_page_config(page_title="🛒 ProductBot", page_icon="🛒")
st.title("🛒 ProductBot")
st.write("Ask for product recommendations and I’ll search Amazon, Flipkart, TataCliq for you!")

query = st.text_input("Enter your product query", placeholder="e.g., laptops under ₹60,000")

if st.button("Ask Agent") and query:
    with st.spinner("Talking to agents..."):
        try:
            response = requests.post(AGENT_API_URL, json={"query": query})
            response.raise_for_status()
            data = response.json()
            result = data.get("response", "Agent returned no output.")
            st.success("Here’s what I found:")
            st.write(result)
        except Exception as e:
            st.error(f"⚠️ Failed to get response from agent.\n\nDetails: {e}")