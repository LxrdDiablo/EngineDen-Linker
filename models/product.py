from dataclasses import dataclass


@dataclass
class Product:
    description: str

    status: str = "Pending"

    confidence: str = ""

    engineden_url: str = ""

    image_url: str = ""