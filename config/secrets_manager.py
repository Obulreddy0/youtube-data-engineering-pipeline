import json
import boto3
from botocore.exceptions import ClientError


class SecretsManager:
    """
    Handles retrieving secrets from AWS Secrets Manager.
    """

    def __init__(self,
                 secret_name: str,
                 region_name: str = "ap-south-1"):

        self.secret_name = secret_name
        self.region_name = region_name

        self.client = boto3.client(
            service_name="secretsmanager",
            region_name=self.region_name
        )

    def get_secret(self):

        try:

            response = self.client.get_secret_value(
                SecretId=self.secret_name
            )

            return json.loads(response["SecretString"])

        except ClientError as e:
            raise Exception(f"Unable to retrieve secret: {e}")