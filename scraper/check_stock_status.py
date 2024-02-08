from typing import Callable
import requests
from bs4 import BeautifulSoup


def check_stock_status(
    url: str, stock_status_logic: Callable[[BeautifulSoup], bool]
) -> bool:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    in_stock = stock_status_logic(soup)

    return in_stock
