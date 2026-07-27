import json

from config.paths import get_bronze_partition


class BronzeLoader:

    @staticmethod
    def save_json(data, file_path):

        partition = get_bronze_partition()

        destination = partition / file_path.name

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")