import re
import pandas as pd

from loaders.gold_loader import GoldLoader

from config.paths import (
    SILVER_CHANNEL_FILE,
    SILVER_VIDEOS_FILE,
    SILVER_VIDEO_STATISTICS_FILE,
    DIM_CHANNEL_FILE,
    DIM_VIDEO_FILE,
    DIM_DATE_FILE,
    FACT_VIDEO_PERFORMANCE_FILE
)


class SilverToGoldTransformer:

    def transform(self):

        print("=" * 60)
        print("STARTING GOLD TRANSFORMATION")
        print("=" * 60)

        self._build_dim_channel()
        self._build_dim_video()
        self._build_dim_date()
        self._build_fact_video_performance()

        print("\n✅ Silver → Gold Transformation Completed Successfully")

    # =====================================================
    # Dimension : Channel
    # =====================================================

    def _build_dim_channel(self):

        df = pd.read_parquet(
            SILVER_CHANNEL_FILE
        )

        df.insert(
            0,
            "channel_key",
            range(1, len(df) + 1)
        )

        dim_channel = df[
            [
                "channel_key",
                "channel_id",
                "channel_title",
                "country",
                "subscriber_count",
                "view_count",
                "video_count"
            ]
        ]

        GoldLoader.save_parquet(
            dim_channel,
            DIM_CHANNEL_FILE
        )

        print("✔ dim_channel created")

    # =====================================================
    # Dimension : Video
    # =====================================================

    def _build_dim_video(self):

        videos = pd.read_parquet(
            SILVER_VIDEOS_FILE
        )

        channels = pd.read_parquet(
            DIM_CHANNEL_FILE
        )

        videos = videos.merge(
            channels[
                [
                    "channel_key",
                    "channel_id"
                ]
            ],
            on="channel_id",
            how="left"
        )

        videos.insert(
            0,
            "video_key",
            range(1, len(videos) + 1)
        )

        dim_video = videos[
            [
                "video_key",
                "video_id",
                "channel_key",
                "title",
                "description",
                "published_at",
                "thumbnail_url"
            ]
        ]

        GoldLoader.save_parquet(
            dim_video,
            DIM_VIDEO_FILE
        )

        print("✔ dim_video created")

    # =====================================================
    # Dimension : Date
    # =====================================================

    def _build_dim_date(self):

        videos = pd.read_parquet(
            SILVER_VIDEOS_FILE
        )

        dates = pd.to_datetime(
            videos["published_at"]
        ).dt.date

        unique_dates = sorted(
            dates.unique()
        )

        dim_date = pd.DataFrame({

            "full_date": pd.to_datetime(
                unique_dates
            )

        })

        dim_date.insert(

            0,

            "date_key",

            dim_date["full_date"]
                .dt.strftime("%Y%m%d")
                .astype(int)

        )

        dim_date["day"] = dim_date["full_date"].dt.day
        dim_date["month"] = dim_date["full_date"].dt.month
        dim_date["month_name"] = dim_date["full_date"].dt.month_name()
        dim_date["quarter"] = dim_date["full_date"].dt.quarter
        dim_date["year"] = dim_date["full_date"].dt.year
        dim_date["weekday"] = dim_date["full_date"].dt.day_name()

        dim_date["is_weekend"] = (
            dim_date["full_date"]
                .dt.weekday >= 5
        )

        GoldLoader.save_parquet(
            dim_date,
            DIM_DATE_FILE
        )

        print("✔ dim_date created")

    # =====================================================
    # Fact : Video Performance
    # =====================================================

    def _build_fact_video_performance(self):

        statistics = pd.read_parquet(
            SILVER_VIDEO_STATISTICS_FILE
        )

        videos = pd.read_parquet(
            SILVER_VIDEOS_FILE
        )

        dim_video = pd.read_parquet(
            DIM_VIDEO_FILE
        )

        # -------------------------------------
        # Join Video Dimension
        # -------------------------------------

        fact = statistics.merge(

            dim_video[
                [
                    "video_key",
                    "video_id"
                ]
            ],

            on="video_id",

            how="left"

        )

        # -------------------------------------
        # Join Published Date
        # -------------------------------------

        fact = fact.merge(

            videos[
                [
                    "video_id",
                    "published_at"
                ]
            ],

            on="video_id",

            how="left"

        )

        fact["published_at"] = pd.to_datetime(
            fact["published_at"]
        )

        fact["date_key"] = (

            fact["published_at"]

                .dt.strftime("%Y%m%d")

                .astype(int)

        )

        # -------------------------------------
        # Convert Duration
        # -------------------------------------

        fact["duration_seconds"] = fact[
            "duration"
        ].apply(
            self._duration_to_seconds
        )

        # -------------------------------------
        # Select Final Columns
        # -------------------------------------

        fact = fact[
            [
                "video_key",
                "date_key",
                "view_count",
                "like_count",
                "comment_count",
                "duration_seconds"
            ]
        ]

        GoldLoader.save_parquet(
            fact,
            FACT_VIDEO_PERFORMANCE_FILE
        )

        print("✔ fact_video_performance created")

    # =====================================================
    # Helper Function
    # =====================================================

    def _duration_to_seconds(self, duration):

        pattern = re.compile(

            r"PT"

            r"(?:(\d+)H)?"

            r"(?:(\d+)M)?"

            r"(?:(\d+)S)?"

        )

        match = pattern.match(duration)

        if not match:

            return 0

        hours = int(match.group(1) or 0)

        minutes = int(match.group(2) or 0)

        seconds = int(match.group(3) or 0)

        return (

            hours * 3600 +

            minutes * 60 +

            seconds

        )