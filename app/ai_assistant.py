from langchain_community.llms import Ollama
from crypto_apis import CryptoAPIManager

class CryptoAssistant:
    def __init__(self):
        self.llm = Ollama(model="phi3:3.8b")

    def generate_response(self, coin: str, question: str) -> str:
        try:
            # Получаем данные
            data = CryptoAPIManager.get_coin_data(coin)
            news = CryptoAPIManager.get_news(coin)

            # Формируем промпт
            prompt = f"""
            Ты — AI-ассистент по криптовалютам. Ответь на вопрос, используя данные:
            - Монета: {coin}
            - Цена: ${data.get('price', 'N/A')}
            - Капитализация: ${data.get('market_cap', 'N/A')}
            - Новости: {'; '.join(news) if news else 'Нет новостей'}

            Вопрос: {question}
            """
            
            # Генерируем ответ
            return self.llm(prompt)
            
        except Exception as e:
            return f"Произошла ошибка: {str(e)}"