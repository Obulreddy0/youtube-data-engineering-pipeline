import json

from config.paths import (
    BRONZE_PARTITION,
    SILVER_PARTITION
)


class MetadataLoader:

    @staticmethod
    def save_bronze_metadata(metadata: dict):

        destination = BRONZE_PARTITION / "metadata.json"

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

        destination = SILVER_PARTITION / "metadata.json"

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                metadata,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")