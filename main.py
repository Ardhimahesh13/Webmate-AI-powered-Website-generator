import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# STREAMLIT APP CONFIGURATION

st.set_page_config(page_title="Webmate", page_icon="🤖")
st.title("🤖 Webmate - Your AI Assistant")
prompt = st.text_area("Welcome to Webmate! Tell me how would you like to design your website today?")

# PROCESSING USER INPUT AND GENERATING RESPONSE
if st.button("Generate Website"):
    message=[("system","""You're an expert web developer mainly on frontend development.
               You will be provided with a prompt from the user to create a website.So create a complete website code with HTML, CSS and JavaScript if required.
               Ensure the code is clean and well commented.
              the output should be in the below format:

              ---html--
              [html code]
              ---html--
              
              ---css--
              [css code]
              ---css--
              
              ---js--
              [js code]
              --js-- """)]
    message.append(("user",prompt))
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)  
    response = model.invoke(message)

    # Save the generated code into separate files

    with open("page.html", "w") as f:
        f.write(response.content.split("--html--")[1])
    with open("style.css", "w") as f:
        f.write(response.content.split("--css--")[1])
    with open("script.js", "w") as f:
        f.write(response.content.split("--js--")[1])

# Now importing  zip File
    import zipfile

    with zipfile.ZipFile("website_files.zip", "w") as zf:
        zf.write("page.html")
        zf.write("style.css")
        zf.write("script.js")

    st.download_button("Download Website",data=open("website_files.zip","rb"),file_name="website_files.zip")

    st.write("Website generated successfully! Download the zip file below.")