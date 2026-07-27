from pipeline.extract_pipeline import ExtractPipeline
from pipeline.transform_pipeline import TransformPipeline
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

    # ---------------------------------------
    # Create Pipeline Metadata
    # ---------------------------------------

    metadata = PipelineMetadata()

    logger = get_logger(__name__)

    # Save metadata for this execution
    MetadataLoader.save_bronze_metadata(
        metadata.to_dict()
    )

    MetadataLoader.save_silver_metadata(
        metadata.to_dict()
    )

    # ---------------------------------------
    # Logging
    # ---------------------------------------

    logger.info("=" * 60)
    logger.info("YOUTUBE DATA ENGINEERING PIPELINE")
    logger.info("=" * 60)

    logger.info(f"Pipeline Run ID : {metadata.pipeline_run_id}")
    logger.info(f"Environment     : {metadata.environment}")
    logger.info(f"Source System   : {metadata.source_system}")
    logger.info(f"Execution Time  : {metadata.execution_timestamp}")

    # ---------------------------------------
    # Console
    # ---------------------------------------

    print("=" * 60)
    print("YOUTUBE DATA ENGINEERING PIPELINE")
    print("=" * 60)

    print(f"Pipeline Run ID : {metadata.pipeline_run_id}")

    print(f"Bronze Directory : {BRONZE_DIR}")
    print(f"Silver Directory : {SILVER_DIR}")
    print(f"Gold Directory   : {GOLD_DIR}")
    print(f"Log Directory    : {LOG_DIR}")

    print("=" * 60)

    # ---------------------------------------
    # Extract
    # ---------------------------------------

    logger.info("Starting Extract Pipeline")

    print("\n[1/3] Starting Extract Pipeline...\n")

    ExtractPipeline().run()

    logger.info("Extract Pipeline Completed")

    print("\n[1/3] Extract Pipeline Completed\n")

    # ---------------------------------------
    # Transform
    # ---------------------------------------

    logger.info("Starting Transform Pipeline")

    print("\n[2/3] Starting Transform Pipeline...\n")

    TransformPipeline().run()

    logger.info("Transform Pipeline Completed")

    print("\n[2/3] Transform Pipeline Completed\n")

    # ---------------------------------------
    # Load
    # ---------------------------------------

    logger.info("Starting Load Pipeline")

    print("\n[3/3] Starting Load Pipeline...\n")

    LoadPipeline().run()

    logger.info("Load Pipeline Completed")

    print("\n[3/3] Load Pipeline Completed\n")

    logger.info("Pipeline Completed Successfully")

    print("=" * 60)
    print("PIPELINE EXECUTION COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()