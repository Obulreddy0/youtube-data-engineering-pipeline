from datetime import datetime
from pathlib import Path


def get_partition_path(base_path: Path):

    today = datetime.utcnow()

    partition = (
        base_path
        / f"year={today:%Y}"
        / f"month={today:%m}"
        / f"day={today:%d}"
    )

    partition.mkdir(
        parents=True,
        exist_ok=True
    )

    return partition