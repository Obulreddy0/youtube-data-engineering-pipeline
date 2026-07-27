from pathlib import Path

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
# Bronze
# ==========================================================

BRONZE_CHANNEL_FILE = BRONZE_DIR / "channel.json"
BRONZE_VIDEOS_FILE = BRONZE_DIR / "videos.json"
BRONZE_VIDEO_STATISTICS_FILE = BRONZE_DIR / "video_statistics.json"

# ==========================================================
# Silver
# ==========================================================

SILVER_CHANNEL_FILE = SILVER_DIR / "channel.parquet"
SILVER_VIDEOS_FILE = SILVER_DIR / "videos.parquet"
SILVER_VIDEO_STATISTICS_FILE = SILVER_DIR / "video_statistics.parquet"

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
# Create folders automatically
# ==========================================================

directories = [
    DATA_DIR,
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
    GOLD_DIMENSION_DIR,
    GOLD_FACT_DIR,
    LOG_DIR,
]

for directory in directories:
    directory.mkdir(parents=True, exist_ok=True)