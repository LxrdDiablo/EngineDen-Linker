from datetime import datetime
from pathlib import Path


class LoggerService:
    """
    Simple logger used by the processing service.
    """

    def __init__(self):

        self.log_directory = Path("logs")
        self.log_directory.mkdir(exist_ok=True)

        self.log_file = (
            self.log_directory /
            f"{datetime.now():%Y-%m-%d}.log"
        )

    def write(self, message: str):

        timestamp = datetime.now().strftime("%H:%M:%S")

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"[{timestamp}] {message}\n"
            )