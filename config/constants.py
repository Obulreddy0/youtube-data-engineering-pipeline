"""
Application constants.
No file paths should be defined here.
"""

# ==========================================================
# YouTube API
# ==========================================================

YOUTUBE_API_SERVICE = "youtube"
YOUTUBE_API_VERSION = "v3"

# ==========================================================
# API Configuration
# ==========================================================

MAX_RESULTS_PER_REQUEST = 50
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 3

# ==========================================================
# Pipeline
# ==========================================================

PIPELINE_NAME = "youtube-data-engineering-pipeline"
SOURCE_SYSTEM = "YouTube Data API v3"
ENVIRONMENT = "local"