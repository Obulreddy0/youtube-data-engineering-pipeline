from config.secrets_manager import SecretsManager

SECRET_NAME = "Youtube-API-KEY"

secret = SecretsManager(
    secret_name=SECRET_NAME
).get_secret()

YOUTUBE_API_KEY = secret["youtube_api_key"]
CHANNEL_HANDLE = secret["channel_handle"]
AWS_REGION = secret["aws_region"]
S3_BUCKET = secret["s3_bucket"]