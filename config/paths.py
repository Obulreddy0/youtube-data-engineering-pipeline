from pathlib import Path

from utils.date_partition import get_partition_path

# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# Data Directories
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

# ==========================================================
# Bronze Dataset Directories
# ==========================================================

BRONZE_CHANNEL_DIR = BRONZE_DIR / "channel"
BRONZE_VIDEOS_DIR = BRONZE_DIR / "videos"
BRONZE_VIDEO_STATISTICS_DIR = BRONZE_DIR / "video_statistics"
BRONZE_METADATA_DIR = BRONZE_DIR / "metadata"

# ==========================================================
# Silver Dataset Directories
# ==========================================================

SILVER_CHANNEL_DIR = SILVER_DIR / "channel"
SILVER_VIDEOS_DIR = SILVER_DIR / "videos"
SILVER_VIDEO_STATISTICS_DIR = SILVER_DIR / "video_statistics"
SILVER_METADATA_DIR = SILVER_DIR / "metadata"

# ==========================================================
# Bronze Files (Partitioned)
# ==========================================================

BRONZE_CHANNEL_FILE = (
    get_partition_path(BRONZE_CHANNEL_DIR)
    / "channel.json"
)

BRONZE_VIDEOS_FILE = (
    get_partition_path(BRONZE_VIDEOS_DIR)
    / "videos.json"
)

BRONZE_VIDEO_STATISTICS_FILE = (
    get_partition_path(BRONZE_VIDEO_STATISTICS_DIR)
    / "video_statistics.json"
)

# ==========================================================
# Silver Files (Partitioned)
# ==========================================================

SILVER_CHANNEL_FILE = (
    get_partition_path(SILVER_CHANNEL_DIR)
    / "channel.parquet"
)

SILVER_VIDEOS_FILE = (
    get_partition_path(SILVER_VIDEOS_DIR)
    / "videos.parquet"
)

SILVER_VIDEO_STATISTICS_FILE = (
    get_partition_path(SILVER_VIDEO_STATISTICS_DIR)
    / "video_statistics.parquet"
)

# ==========================================================
# Gold Directories
# ==========================================================

GOLD_DIMENSION_DIR = GOLD_DIR / "dimensions"
GOLD_FACT_DIR = GOLD_DIR / "facts"

# ==========================================================
# Gold Files
# ==========================================================

DIM_CHANNEL_FILE = GOLD_DIMENSION_DIR / "dim_channel.parquet"

DIM_VIDEO_FILE = GOLD_DIMENSION_DIR / "dim_video.parquet"

DIM_DATE_FILE = GOLD_DIMENSION_DIR / "dim_date.parquet"

FACT_VIDEO_PERFORMANCE_FILE = (
    GOLD_FACT_DIR / "fact_video_performance.parquet"
)

# ==========================================================
# Logs
# ==========================================================

LOG_DIR = PROJECT_ROOT / "logs"

# ==========================================================
# Create Directories
# ==========================================================

directories = [
    DATA_DIR,

    BRONZE_DIR,
    BRONZE_CHANNEL_DIR,
    BRONZE_VIDEOS_DIR,
    BRONZE_VIDEO_STATISTICS_DIR,
    BRONZE_METADATA_DIR,

    SILVER_DIR,
    SILVER_CHANNEL_DIR,
    SILVER_VIDEOS_DIR,
    SILVER_VIDEO_STATISTICS_DIR,
    SILVER_METADATA_DIR,

    GOLD_DIR,
    GOLD_DIMENSION_DIR,
    GOLD_FACT_DIR,

    LOG_DIR,
]

for directory in directories:
    directory.mkdir(parents=True, exist_ok=True)