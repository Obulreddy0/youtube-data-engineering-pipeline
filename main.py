from pipeline.extract_pipeline import ExtractPipeline
from pipeline.transform_pipeline import TransformPipeline
from pipeline.load_pipeline import LoadPipeline

from config.paths import (
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
    LOG_DIR
)


def main():

    print('=' * 60)
    print('YOUTUBE DATA ENGINEERING PIPELINE')
    print('=' * 60)

    print(f'Bronze Directory : {BRONZE_DIR}')
    print(f'Silver Directory : {SILVER_DIR}')
    print(f'Gold Directory   : {GOLD_DIR}')
    print(f'Log Directory    : {LOG_DIR}')
    print('=' * 60)

    # -----------------------------------------------------
    # Extract Stage
    # -----------------------------------------------------
    print('\n[1/3] Starting Extract Pipeline...\n')
    ExtractPipeline().run()
    print('\n[1/3] Extract Pipeline Completed\n')

    # -----------------------------------------------------
    # Transform Stage
    # -----------------------------------------------------
    print('\n[2/3] Starting Transform Pipeline...\n')
    TransformPipeline().run()
    print('\n[2/3] Transform Pipeline Completed\n')

    # -----------------------------------------------------
    # Load Stage
    # -----------------------------------------------------
    print('\n[3/3] Starting Load Pipeline...\n')
    LoadPipeline().run()
    print('\n[3/3] Load Pipeline Completed\n')

    print('=' * 60)
    print('PIPELINE EXECUTION COMPLETED SUCCESSFULLY')
    print('=' * 60)


if __name__ == '__main__':
    main()