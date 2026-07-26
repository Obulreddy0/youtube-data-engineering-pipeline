import os

# Base Directories
BASE_DIR = os.getcwd()

DATA_DIR = os.path.join(BASE_DIR, "data")

BRONZE_DIR = os.path.join(DATA_DIR, "bronze")
SILVER_DIR = os.path.join(DATA_DIR, "silver")
GOLD_DIR = os.path.join(DATA_DIR, "gold")

# File Names
CHANNEL_FILE = "channel.json"
VIDEOS_FILE = "videos.json"
VIDEO_STATS_FILE = "video_statistics.json"