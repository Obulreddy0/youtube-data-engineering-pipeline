import json

from utils.date_partition import get_partition_path

from config.paths import (
    BRONZE_METADATA_DIR,
    SILVER_METADATA_DIR
)


class MetadataLoader:

    @staticmethod
    def save_bronze_metadata(metadata: dict):

        partition = get_partition_path(BRONZE_METADATA_DIR)

        destination = partition / "metadata.json"

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

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

        partition = get_partition_path(SILVER_METADATA_DIR)

        destination = partition / "metadata.json"

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                metadata,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")