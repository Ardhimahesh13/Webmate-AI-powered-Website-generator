
# 🤖 Webmate - AI-Powered Website Generator

Webmate is an intelligent web development assistant that transforms natural language descriptions into complete, functional websites. Built with Streamlit and powered by Google's Gemini AI, it automates frontend development by generating clean HTML, CSS, and JavaScript code instantly.

## ✨ Features

- **AI-Powered Code Generation**: Leverages Google Gemini 2.5 Flash to understand requirements and generate professional code
- **Complete Website Package**: Produces HTML, CSS, and JavaScript files in one workflow
- **Clean & Commented Code**: Well-structured, readable code with helpful comments
- **Instant Download**: Automatically packages files into a zip archive
- **User-Friendly Interface**: Simple chat-based interaction requiring no technical expertise
- **Rapid Prototyping**: Perfect for quickly testing ideas and creating mockups

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini AI
- pip package manager

### Installation

1. Clone the repository
### 2. Install required dependencies
pip install streamlit python-dotenv langchain-google-genai

### 3. Set up your environment variables
Create a `.env` file in the project root:
gemini=your_google_api_key_here

### Running the Application
streamlit run app.py


The application will open in your default browser at `http://localhost:8501`

## 📖 Usage

1. **Enter Your Prompt**: Describe the website you want to create in the text area
   - Example: "Create a modern landing page for a coffee shop with a hero section, menu, and contact form"

2. **Generate Website**: Click the "Generate Website" button

3. **Download Files**: Once generated, download the zip file containing:
   - `page.html` - Main HTML structure
   - `style.css` - Styling and layout
   - `script.js` - Interactive functionality

4. **Deploy**: Extract the files and host them on any web server

## 🛠️ Tech Stack

- **Streamlit**: Web application framework
- **LangChain**: AI orchestration and prompt management
- **Google Gemini AI**: Large language model for code generation
- **Python**: Core programming language

## 🔧 Configuration

Adjust the AI model parameters in `app.py`:
## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Requestmodel = ChatGoogleGenerativeAI(
model="gemini-2.5-flash-lite",
temperature=0.7 # Controls creativity (0.0 - 1.0)
)

## 👤 Author

Your Name
- GitHub: [@Ardhimahesh13](https://github.com/Ardhimahesh13)

  ## 🙏 Acknowledgments

- Google Gemini AI for powerful language models
- Streamlit for the intuitive web framework
- LangChain for AI integration tools

  ---

⭐ If you find this project helpful, please consider giving it a star on GitHub!
