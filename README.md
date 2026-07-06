# 🔍 Multi-Agent Research System

An AI-powered **Multi-Agent Research System** built using **LangChain**, **Google Gemini API**, **Tavily Search API**, **BeautifulSoup**, and **Streamlit**. The application automates the entire research workflow by utilizing multiple AI agents that collaborate to search the web, extract relevant information, generate structured research reports, and evaluate the quality of the generated content.

---

## 🚀 Features

- 🔎 Intelligent web search using Tavily Search API
- 📄 Web scraping with BeautifulSoup for detailed content extraction
- 🤖 Multi-Agent architecture powered by LangChain
- ✍️ AI-generated structured research reports using Google Gemini
- 📝 Automated report review and quality assessment
- 🌐 Interactive Streamlit-based user interface
- ⚡ Fast, modular, and scalable research workflow

---

## 🛠️ Tech Stack

- Python
- LangChain
- Google Gemini API
- Tavily Search API
- BeautifulSoup
- Requests
- Streamlit
- Python-dotenv
- Rich

---

## 🏗️ Project Architecture

```
User Input
     │
     ▼
Search Agent
(Tavily Search)
     │
     ▼
Reader Agent
(Web Scraping using BeautifulSoup)
     │
     ▼
Writer Agent
(Google Gemini)
     │
     ▼
Critic Agent
(Google Gemini)
     │
     ▼
Final Research Report
```

---

## 📂 Project Structure

```
multi-agent-research-system/
│── app.py
│── pipeline.py
│── agents.py
│── tools.py
│── requirements.txt
│── .env
│── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-research-system.git
cd multi-agent-research-system
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

---

## ▶️ Run the Application

### Terminal Version

```bash
python pipeline.py
```

### Streamlit Version

```bash
streamlit run app.py
```

---

## 💡 Sample Research Topics

- Artificial Intelligence in Healthcare
- Climate Change and Renewable Energy
- Cybersecurity Trends
- Future of Quantum Computing
- Electric Vehicles vs Hydrogen Vehicles
- India's Space Missions
- Blockchain in Supply Chain Management

---

## 🔮 Future Enhancements

- PDF Report Export
- DOCX Report Generation
- Citation & Reference Management
- Multi-language Support
- Research History
- Authentication System
- Interactive Charts & Visualizations
- RAG-based Knowledge Retrieval

---

## 👨‍💻 Author

**Heer Lad**

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
