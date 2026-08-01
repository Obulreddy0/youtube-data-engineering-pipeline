# youtube-data-engineering-pipeline


An end-to-end Data Engineering project that extracts data from the YouTube Data API v3, processes it through a Medallion Architecture (Bronze → Silver → Gold), and uploads curated datasets to Amazon S3.

---

# Project Architecture

YouTube Data API
        │
        ▼
Extract Pipeline
        │
        ▼
Bronze Layer (JSON)
        │
        ▼
Transform Pipeline
        │
        ▼
Silver Layer (Parquet)
        │
        ▼
Gold Pipeline
        │
        ▼
Dimension & Fact Tables
        │
        ▼
Amazon S3

---

# Tech Stack

- Python
- YouTube Data API v3
- Pandas
- PyArrow
- Amazon S3
- AWS Secrets Manager
- Boto3
- Logging
- Git & GitHub

Upcoming

- AWS Managed Apache Airflow (MWAA)
- AWS Glue Catalog
- Amazon Athena
- Amazon QuickSight

---

# Project Structure

```text
youtube-data-engineering-pipeline/

config/
extractors/
loaders/
pipeline/
transform/
utils/

data/
    bronze/
    silver/
    gold/

logs/

main.py
requirements.txt
README.md
```

---

# Current Pipeline

## Extract

Downloads

- Channel Information
- Videos
- Video Statistics

Stores data as JSON in Bronze Layer.

Example

```
data/
└── bronze/
    └── year=2026/
        └── month=08/
            └── day=01/
                channel.json
                videos.json
                video_statistics.json
                metadata.json
```

---

## Transform

Transforms Bronze JSON into structured Parquet files.

Creates

- Channel Dataset
- Videos Dataset
- Video Statistics Dataset

Stored in Silver Layer.

Example

```
data/
└── silver/
    └── year=2026/
        └── month=08/
            └── day=01/
                channel.parquet
                videos.parquet
                video_statistics.parquet
                metadata.json
```

---

## Gold Layer

Creates analytical tables.

Dimensions

- dim_channel
- dim_video
- dim_date

Fact

- fact_video_performance

Output

```
data/
└── gold/
    ├── dimensions/
    │      dim_channel.parquet
    │      dim_video.parquet
    │      dim_date.parquet
    │
    └── facts/
           fact_video_performance.parquet
```

---

## Metadata

Each pipeline execution generates metadata including

- Pipeline Run ID
- Execution Timestamp
- Environment
- Source System

---

## Logging

Logs are generated for every execution.

Example

```
logs/

pipeline.log
```

---

# Amazon S3

The pipeline uploads all datasets to Amazon S3.

```
s3://youtube-data-engineering-pipeline-644266601735/

bronze/
silver/
gold/
```

---

# AWS Services Used

- Amazon S3
- AWS Secrets Manager
- IAM
- Boto3

---

# Pipeline Flow

```
Extract
   │
   ▼
Bronze (JSON)
   │
   ▼
Silver (Parquet)
   │
   ▼
Gold (Dimension & Fact)
   │
   ▼
Amazon S3
```

---

# Features

✔ Modular pipeline architecture

✔ Bronze, Silver and Gold layers

✔ Date partitioning

✔ Metadata generation

✔ Logging

✔ Secrets Manager integration

✔ Amazon S3 upload

✔ Dimension & Fact tables

✔ Fully automated pipeline

---

# Running the Project

Clone repository

```bash
git clone https://github.com/<your-username>/youtube-data-engineering-pipeline.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run pipeline

```bash
python main.py
```

---

# Sprint Progress

## Sprint 1

- Project Setup
- YouTube API Connection
- Configuration

## Sprint 2

- Extract Pipeline
- Bronze Layer

## Sprint 3

- Silver Layer
- Transformations

## Sprint 4

- Metadata
- Logging
- Date Partitioning

## Sprint 5

- Gold Layer
- Dimension Tables
- Fact Table
- Amazon S3 Upload
- AWS Secrets Manager Integration

## Sprint 6 (In Progress)

- Managed Apache Airflow (MWAA)
- DAG Orchestration
- Production Scheduling

---

# Future Enhancements

- AWS Managed Apache Airflow
- AWS Glue Catalog
- Amazon Athena
- Amazon QuickSight Dashboard
- Data Quality Checks
- CI/CD Pipeline
- Docker
- Terraform
- Unit Testing

---

# Author

Badri

Data Engineering Portfolio Project