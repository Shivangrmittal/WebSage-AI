import requests
import trafilatura

from bs4 import BeautifulSoup
from langchain_core.documents import Document


def load_webpage(url: str):
    """
    Downloads a webpage and extracts only its main content.
    """

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            " AppleWebKit/537.36"
            " Chrome/137.0 Safari/537.36"
        )
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    html = response.text

    # -----------------------------
    # Try Trafilatura
    # -----------------------------

    extracted_text = trafilatura.extract(html)

    # -----------------------------
    # Fallback to BeautifulSoup
    # -----------------------------

    if not extracted_text:

        soup = BeautifulSoup(html, "lxml")

        for tag in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "noscript",
            "aside"
        ]):
            tag.decompose()

        extracted_text = soup.get_text(
            separator="\n",
            strip=True
        )

    return [
        Document(
            page_content=extracted_text,
            metadata={
                "source": url
            }
        )
    ]