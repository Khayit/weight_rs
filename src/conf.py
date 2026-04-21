from os import getenv
from pathlib import Path

from dotenv import load_dotenv

from utils.logger import LogWriter
from meter.meter import WeightReader


class Config:
    def __init__(self):
        self.app_dir = Path(__file__).parent.parent
        self.configs_dir = self.app_dir / "storage"

        load_dotenv(self.configs_dir / ".env")
        self.logger = LogWriter(self.configs_dir / "app.log")

        # env
        self.login = getenv("LOGIN")
        self.password = getenv("PASSWORD")

        self.port = getenv("PORT")
        self.read_timeout = float(getenv("READ_TIMEOUT", "3"))
        self.minimal_weight = int(getenv("MINIMAL_WEIGHT", "0"))

        self.meter = WeightReader(self.port)


conf = Config()
