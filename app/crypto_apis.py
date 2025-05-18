import requests
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class CryptoAPIManager:
    @staticmethod
    def get_coin_data(coin_id: str) -> Dict:
        """Получает цену и рыночную капитализацию."""
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
        response = requests.get(url).json()
        return {
            "price": response["market_data"]["current_price"]["usd"],
            "market_cap": response["market_data"]["market_cap"]["usd"],
            "rank": response["market_data"]["market_cap_rank"]
        }

    @staticmethod
    def get_news(coin: str) -> List[str]:
        """Получает последние новости."""
        url = f"https://cryptopanic.com/api/v1/posts/?auth_token={os.getenv('CRYPTOPANIC_API_KEY')}&currencies={coin.upper()}"
        try:
            response = requests.get(url).json()
            # Проверяем наличие ключа 'results' в ответе
            if 'results' in response:
                return [news['title'] for news in response['results'][:3]]
            return ["No news available"]  # Возвращаем заглушку, если нет новостей
        except Exception as e:
            print(f"Error fetching news: {e}")
            return ["Failed to load news"]  # Заглушка при ошибке