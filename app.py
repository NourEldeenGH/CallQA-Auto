import streamlit as st
import os

st.set_page_config(page_title="Call QA Automation", layout="centered")

st.title("📞 Call QA Automation")
st.write("Upload a call recording and specify the campaign. The system will transcribe and check it based on QA criteria.")

# Upload audio file
uploaded_file = st.file_uploader("Upload Call Recording", type=["mp3", "wav", "m4a"])
campaign_name = st.text_input("Campaign Name")

# Upload campaign criteria
uploaded_criteria = st.file_uploader("Upload Campaign Criteria (TXT or PDF)", type=["txt", "pdf"])

if uploaded_file and campaign_name and uploaded_criteria:
    st.success("✅ All inputs received.")
    
    st.write("🧠 Processing your file... (Coming soon)")

    # Placeholder result
    st.markdown("### Results")
    st.write("- **Agent Name:** (to be extracted)")
    st.write("- **Owner Name:** (to be extracted)")
    st.write("- **Call Status:** (Qualified / Disqualified)")
    st.write("- **Reason:** (based on criteria matching)")

    st.info("🚧 Full logic for transcription and QA matching will be added here.")
else:
    st.warning("Please upload a call recording, campaign name, and campaign criteria.")

