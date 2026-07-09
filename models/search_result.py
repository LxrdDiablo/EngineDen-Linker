from dataclasses import dataclass


@dataclass
class SearchResult:
    """
    Result returned from EngineDenService.
    """

    found: bool = False

    product_name: str = ""

    matched_name: str = ""

    product_url: str = ""

    image_url: str = ""

    confidence: int = 0

    error: str = ""