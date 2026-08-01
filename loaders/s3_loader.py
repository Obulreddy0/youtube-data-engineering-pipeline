from pathlib import Path
import boto3

from config.settings import (
    AWS_REGION,
    S3_BUCKET
)


class S3Loader:

    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            region_name=AWS_REGION
        )

    def upload_directory(self, local_directory: Path, s3_prefix: str):

        local_directory = Path(local_directory)

        if not local_directory.exists():
            print(f"Directory not found: {local_directory}")
            return

        files = list(local_directory.rglob("*"))

        files = [file for file in files if file.is_file()]

        if not files:
            print(f"No files found in {local_directory}")
            return

        print(f"\nUploading {len(files)} files to S3...\n")

        for file in files:

            relative_path = file.relative_to(local_directory)

            s3_key = f"{s3_prefix}/{relative_path.as_posix()}"

            self.s3.upload_file(
                str(file),
                S3_BUCKET,
                s3_key
            )

            print(f"✔ {s3_key}")

        print("\nS3 upload completed.\n")