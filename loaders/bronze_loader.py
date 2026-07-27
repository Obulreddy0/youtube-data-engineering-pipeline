import json
from pathlib import Path


class BronzeLoader:

    @staticmethod
    def save_json(data, file_path):

        file_path = Path(file_path)

        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {file_path}")