from config.settings import (
    CHANNEL_HANDLE,
    AWS_REGION,
    S3_BUCKET
)


def main():

    print("=" * 40)
    print("Configuration Loaded")
    print("=" * 40)

    print(f"Channel : {CHANNEL_HANDLE}")
    print(f"Region  : {AWS_REGION}")
    print(f"Bucket  : {S3_BUCKET}")


if __name__ == "__main__":
    main()