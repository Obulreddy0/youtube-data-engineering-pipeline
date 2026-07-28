from pipeline.extract_pipeline import ExtractPipeline
from pipeline.transform_pipeline import TransformPipeline
from pipeline.gold_pipeline import GoldPipeline
from pipeline.load_pipeline import LoadPipeline

from config.paths import (
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
    LOG_DIR
)

from utils.metadata import PipelineMetadata
from utils.logger import get_logger

from loaders.metadata_loader import MetadataLoader


def main():

    # ==========================================================
    # Pipeline Metadata
    # ==========================================================

    metadata = PipelineMetadata()

    logger = get_logger(__name__)

    MetadataLoader.save_bronze_metadata(
        metadata.to_dict()
    )

    MetadataLoader.save_silver_metadata(
        metadata.to_dict()
    )

    # ==========================================================
    # Logging Header
    # ==========================================================

    logger.info("=" * 60)
    logger.info("YOUTUBE DATA ENGINEERING PIPELINE")
    logger.info("=" * 60)

    logger.info(f"Pipeline Run ID : {metadata.pipeline_run_id}")
    logger.info(f"Environment     : {metadata.environment}")
    logger.info(f"Source System   : {metadata.source_system}")
    logger.info(f"Execution Time  : {metadata.execution_timestamp}")

    # ==========================================================
    # Console Header
    # ==========================================================

    print("=" * 60)
    print("YOUTUBE DATA ENGINEERING PIPELINE")
    print("=" * 60)

    print(f"Pipeline Run ID : {metadata.pipeline_run_id}")
    print(f"Environment     : {metadata.environment}")
    print(f"Source System   : {metadata.source_system}")
    print(f"Execution Time  : {metadata.execution_timestamp}")

    print()

    print(f"Bronze Directory : {BRONZE_DIR}")
    print(f"Silver Directory : {SILVER_DIR}")
    print(f"Gold Directory   : {GOLD_DIR}")
    print(f"Log Directory    : {LOG_DIR}")

    print("=" * 60)

    # ==========================================================
    # Execute Pipeline
    # ==========================================================

    try:

        # ------------------------------------------------------
        # Extract
        # ------------------------------------------------------

        logger.info("Starting Extract Pipeline")

        print("\n[1/4] Starting Extract Pipeline...\n")

        ExtractPipeline().run()

        logger.info("Extract Pipeline Completed")

        print("\n[1/4] Extract Pipeline Completed\n")

        # ------------------------------------------------------
        # Transform
        # ------------------------------------------------------

        logger.info("Starting Transform Pipeline")

        print("\n[2/4] Starting Transform Pipeline...\n")

        TransformPipeline().run()

        logger.info("Transform Pipeline Completed")

        print("\n[2/4] Transform Pipeline Completed\n")

        # ------------------------------------------------------
        # Gold
        # ------------------------------------------------------

        logger.info("Starting Gold Pipeline")

        print("\n[3/4] Starting Gold Pipeline...\n")

        GoldPipeline().run()

        logger.info("Gold Pipeline Completed")

        print("\n[3/4] Gold Pipeline Completed\n")

        # ------------------------------------------------------
        # Load
        # ------------------------------------------------------

        logger.info("Starting Load Pipeline")

        print("\n[4/4] Starting Load Pipeline...\n")

        LoadPipeline().run()

        logger.info("Load Pipeline Completed")

        print("\n[4/4] Load Pipeline Completed\n")

        logger.info("Pipeline Completed Successfully")

        print("=" * 60)
        print("PIPELINE EXECUTION COMPLETED SUCCESSFULLY")
        print("=" * 60)

    except Exception as e:

        logger.exception("PIPELINE FAILED")

        print("\n" + "=" * 60)
        print("PIPELINE EXECUTION FAILED")
        print("=" * 60)
        print(e)

        raise


if __name__ == "__main__":
    main()