# AI Crypto Assistant

![Project Demo](assets/demo.gif)

## 📌 Overview
AI-powered cryptocurrency assistant that provides real-time:
- Price data (CoinGecko API)
- Market cap & rankings
- Latest news (CryptoPanic API)
- AI-generated insights (Ollama + Phi-3)

## 🚀 Features
- Query handling: "What's Bitcoin's current price?"
- Multi-source data aggregation
- Local LLM processing (Ollama)
- Streamlit web interface

## ⚙️ Installation
1. Install prerequisites:
```bash
git clone https://github.com/yourusername/crypto-ai-assistant.git
cd crypto-ai-assistant
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```
Install dependencies:

```bash
pip install -r requirements.txt
ollama pull phi3:3.8b
```
Configure environment:

```bash
cp .env.example .env
```
# Add your API keys to .env
🖥️ Usage
Run in two separate terminals:

```bash
# Terminal 1
ollama serve
```
# Terminal 2
```bash
streamlit run app/main.py
```
🌐 APIs Used
Service	Use Case	Free Tier
CoinGecko	Price/Market Data	Yes
CryptoPanic	News Aggregation	Limited
Ollama	Local LLM	Free
