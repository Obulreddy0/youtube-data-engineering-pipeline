from functools import lru_cache

from config.secrets_manager import SecretsManager

SECRET_NAME = "Youtube-API-KEY"


@lru_cache(maxsize=1)
def get_settings():
    """
    Load secrets from AWS Secrets Manager once and cache them.
    """
    return SecretsManager(
        secret_name=SECRET_NAME
    ).get_secret()


def get_youtube_api_key():
    return get_settings()["youtube_api_key"]


def get_channel_handle():
    return get_settings()["channel_handle"]


def get_aws_region():
    return get_settings()["aws_region"]


def get_s3_bucket():
    return get_settings()["s3_bucket"]