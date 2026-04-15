import streamlit as st
from langchain_groq import ChatGroq

# 🔑 GROQ API KEY (paste your key here)
GROQ_API_KEY = "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"

# PAGE CONFIG
st.set_page_config(page_title="BugEZ", page_icon="💻", layout="centered")

# 🎨 UI STYLE
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #1f2c3d, #2b5876);
}

/* Title */
h1 {
    color: #ffffff;
    text-align: center;
    font-weight: bold;
    text-shadow: 0 0 5px #00c3ff;
}

/* Subtitle */
h3 {
    color: #e0e0e0;
    text-align: center;
}

/* Labels */
label {
    color: #ffffff !important;
    font-weight: 500;
}

/* Dropdown */
.stSelectbox div {
    background-color: white;
    border-radius: 8px;
}

/* Code input box */
.stTextArea textarea {
    background-color: #ffffff;
    color: #000000;
    border-radius: 12px;
    border: 2px solid #00c3ff;
    padding: 10px;
    font-size: 14px;
}

/* Button */
.stButton button {
    background: linear-gradient(90deg, #00c3ff, #00ffcc);
    color: black;
    border-radius: 10px;
    font-weight: bold;
    width: 100%;
    height: 3em;
}

/* Button hover */
.stButton button:hover {
    background: linear-gradient(90deg, #00ffcc, #00c3ff);
    transform: scale(1.03);
}

/* Result text */
.stMarkdown {
    color: #ffffff;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("💻 AI Code Analyzer PRO")
st.markdown("### 🚀 Analyze, Debug & Optimize your code instantly")

# LANGUAGE SELECT
language = st.selectbox(
    "💡 Select Programming Language",
    ["Python", "Java", "C++", "JavaScript", "Other"]
)

# INPUT
code = st.text_area("📌 Paste your code here:", height=250)

# ANALYZE BUTTON
if st.button("✨ Analyze Code"):
    if code.strip() == "":
        st.warning("⚠️ Please enter some code!")
    else:
        with st.spinner("🤖 AI is analyzing your code..."):

            # 🔥 FINAL WORKING MODEL
            llm = ChatGroq(
                groq_api_key=GROQ_API_KEY,
                model_name="llama-3.1-8b-instant"
            )

            prompt = f"""
            Analyze the following {language} code:

            {code}

            Provide:
            1. Explanation (simple terms)
            2. Step-by-step logic
            3. Time complexity
            4. Errors (if any)
            5. Optimized improvements
            """

            response = llm.invoke(prompt)
            result = response.content

            st.success("✅ Analysis Complete!")

            st.markdown("### 📊 Result")
            st.write(result)

            # SHOW RESULT AS CODE (copy friendly)
            st.code(result, language="text")

            # DOWNLOAD BUTTON
            st.download_button(
                label="⬇ Download Result",
                data=result,
                file_name="analysis.txt",
                mime="text/plain"
            )

            st.balloons()