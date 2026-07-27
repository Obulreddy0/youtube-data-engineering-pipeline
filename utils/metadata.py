import uuid
from datetime import datetime, timezone

from config.constants import (
    PIPELINE_NAME,
    PIPELINE_VERSION,
    ENVIRONMENT,
    SOURCE_SYSTEM
)


class PipelineMetadata:

    def __init__(self):

        self.pipeline_run_id = str(uuid.uuid4())

        self.pipeline_name = PIPELINE_NAME

        self.environment = ENVIRONMENT

        self.source_system = SOURCE_SYSTEM

        self.execution_timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        self.execution_date = datetime.now(
            timezone.utc
        ).strftime("%Y-%m-%d")

        self.version = PIPELINE_VERSION

    def to_dict(self):

        return {
            "pipeline_run_id": self.pipeline_run_id,
            "pipeline_name": self.pipeline_name,
            "environment": self.environment,
            "source_system": self.source_system,
            "execution_timestamp": self.execution_timestamp,
            "execution_date": self.execution_date,
            "version": self.version
        }