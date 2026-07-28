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
# Partition Directories
# ==========================================================

BRONZE_PARTITION = get_partition_path(BRONZE_DIR)
SILVER_PARTITION = get_partition_path(SILVER_DIR)

# ==========================================================
# Bronze Files
# ==========================================================

BRONZE_CHANNEL_FILE = BRONZE_PARTITION / "channel.json"
BRONZE_VIDEOS_FILE = BRONZE_PARTITION / "videos.json"
BRONZE_VIDEO_STATISTICS_FILE = BRONZE_PARTITION / "video_statistics.json"

# ==========================================================
# Silver Files
# ==========================================================

SILVER_CHANNEL_FILE = SILVER_PARTITION / "channel.parquet"
SILVER_VIDEOS_FILE = SILVER_PARTITION / "videos.parquet"
SILVER_VIDEO_STATISTICS_FILE = SILVER_PARTITION / "video_statistics.parquet"

# ==========================================================
# Gold
# ==========================================================

GOLD_DIMENSION_DIR = GOLD_DIR / "dimensions"
GOLD_FACT_DIR = GOLD_DIR / "facts"

# ==========================================================
# Logs
# ==========================================================

LOG_DIR = PROJECT_ROOT / "logs"

# ==========================================================
# Create directories automatically
# ==========================================================

directories = [
    DATA_DIR,
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
    GOLD_DIMENSION_DIR,
    GOLD_FACT_DIR,
    LOG_DIR,
    BRONZE_PARTITION,
    SILVER_PARTITION,
]

for directory in directories:
    directory.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Gold Files
# ==========================================================

DIM_CHANNEL_FILE = GOLD_DIMENSION_DIR / "dim_channel.parquet"

DIM_VIDEO_FILE = GOLD_DIMENSION_DIR / "dim_video.parquet"

DIM_DATE_FILE = GOLD_DIMENSION_DIR / "dim_date.parquet"

FACT_VIDEO_PERFORMANCE_FILE = (
    GOLD_FACT_DIR / "fact_video_performance.parquet"
)    