from dataclasses import dataclass


@dataclass
class Product:
    row_number: int = 0
    description: str = ""

    status: str = "Pending"

    confidence: str = ""

    engineden_url: str = ""

    image_url: str = ""