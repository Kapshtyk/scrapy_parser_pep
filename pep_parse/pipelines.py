import csv
from datetime import datetime
from pathlib import Path

from constants import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = {}

    def process_item(self, item, spider):
        self.statuses[item["status"]] = (
            self.statuses.get(item["status"], 0) + 1
        )
        return item

    def close_spider(self, spider):
        results = BASE_DIR / "results"
        results.mkdir(exist_ok=True)
        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = Path.joinpath(
            results,
            f"status_summary_{current_date}.csv",
        )
        data = [
            ("Status", "Count"),
            *self.statuses.items(),
            ("Total", sum(self.statuses.values())),
        ]
        with open(file_name, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
