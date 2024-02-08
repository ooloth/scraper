from bs4 import BeautifulSoup

from scraper.check_stock_status import check_stock_status
from scraper.notifications import send_email_notification


def is_amazon_product_in_stock(soup: BeautifulSoup) -> bool:
    # Replace this with the actual logic to find the stock status
    in_stock = soup.find("div", {"id": "availability"})
    if not in_stock:
        print("Product is not in stock.")
        return False
    return True


if __name__ == "__main__":
    product_url = "https://www.amazon.ca/Nutramigen-Hypoallergenic-Infant-Formula-Powder/dp/B00DOPYTAA"

    in_stock = check_stock_status(product_url, is_amazon_product_in_stock)

    # TODO: replace `"your-email@example.com"`, `"your-gmail@example.com"`, and `"your-gmail-password"` with your actual email addresses and password. Be sure to handle your password securely and consider using environment variables or a secure password manager to avoid hardcoding it into your script.

    if not in_stock:
        print("Product is not in stock.")
        send_email_notification(
            subject="Product Out of Stock",
            body=f"The product at {product_url} is out of stock.",
            to="your-email@example.com",
            gmail_user="your-gmail@example.com",
            gmail_password="your-gmail-password",
        )

    # Logic for notification
