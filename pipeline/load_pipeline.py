from loaders.s3_loader import S3Loader

from config.paths import (
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR
)


class LoadPipeline:

    def run(self):

        print("=" * 60)
        print("STARTING LOAD PIPELINE")
        print("=" * 60)

        loader = S3Loader()

        # -----------------------------------
        # Upload Bronze Layer
        # -----------------------------------

        print("\nUploading Bronze Layer...\n")

        loader.upload_directory(
            BRONZE_DIR,
            "bronze"
        )

        # -----------------------------------
        # Upload Silver Layer
        # -----------------------------------

        print("\nUploading Silver Layer...\n")

        loader.upload_directory(
            SILVER_DIR,
            "silver"
        )

        # -----------------------------------
        # Upload Gold Layer
        # -----------------------------------

        print("\nUploading Gold Layer...\n")

        loader.upload_directory(
            GOLD_DIR,
            "gold"
        )

        print("=" * 60)
        print("LOAD PIPELINE COMPLETED")
        print("=" * 60)