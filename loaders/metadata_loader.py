import json

from config.paths import (
    get_bronze_partition,
    get_silver_partition
)


class MetadataLoader:

    @staticmethod
    def save_bronze_metadata(metadata: dict):

        destination = get_bronze_partition() / "metadata.json"

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                metadata,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")

    @staticmethod
    def save_silver_metadata(metadata: dict):

        destination = get_silver_partition() / "metadata.json"

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                metadata,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")