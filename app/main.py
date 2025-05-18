import streamlit as st
from ai_assistant import CryptoAssistant
from crypto_apis import CryptoAPIManager  # Добавлен импорт
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Crypto AI Assistant", layout="wide")
st.title("💰 AI Crypto Assistant")

# Ввод пользователя
coin = st.text_input("Введите криптовалюту (например, bitcoin):").lower()
question = st.text_input("Задайте вопрос (например, 'Какая цена?'):")

if st.button("Получить ответ"):
    if not coin or not question:
        st.error("Введите название криптовалюты и вопрос!")
    else:
        try:
            assistant = CryptoAssistant()
            answer = assistant.generate_response(coin, question)
            st.success(answer)
            
            # Добавим проверку перед выводом данных
            if hasattr(CryptoAPIManager, 'get_coin_data'):
                coin_data = CryptoAPIManager.get_coin_data(coin)
                st.json(coin_data)
        except Exception as e:
            st.error(f"Произошла ошибка: {str(e)}")