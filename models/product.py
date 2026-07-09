from dataclasses import dataclass, field


@dataclass
class Product:
    """
    Represents one row from the Excel workbook.
    """

    row_number: int
    description: str

    matched_name: str = ""
    engineden_url: str = ""
    image_url: str = ""

    confidence: int = 0

    status: str = "Waiting"

    error: str = ""

    processed: bool = False

    extra: dict = field(default_factory=dict)