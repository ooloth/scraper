import pytest
import requests_mock
from bs4 import BeautifulSoup
from scraper.check_stock_status import (
    check_stock_status,
)


def stock_status_logic(soup):
    return "In Stock" in soup.text


@pytest.fixture
def mock_get():
    with requests_mock.Mocker() as m:
        yield m


def test_check_stock_in_stock(mock_get):
    mock_get.get("http://example.com", text="<html><body><p>In Stock</p></body></html>")
    result = check_stock_status("http://example.com", stock_status_logic)
    assert result is True


def test_check_stock_out_of_stock(mock_get):
    mock_get.get(
        "http://example.com", text="<html><body><p>Out of Stock</p></body></html>"
    )
    result = check_stock_status("http://example.com", stock_status_logic)
    assert result is False
