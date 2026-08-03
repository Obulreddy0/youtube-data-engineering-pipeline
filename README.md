# YouTube Data Engineering Pipeline

An end-to-end AWS Data Engineering project that extracts YouTube channel data using the YouTube Data API v3, builds a Medallion Architecture (Bronze, Silver, Gold), stores data in Amazon S3, catalogs datasets using AWS Glue Crawlers, and enables SQL analytics through Amazon Athena.

---

# Architecture

```
                YouTube Data API
                        │
                        ▼
              Python Extract Pipeline
                        │
                        ▼
               Bronze Layer (JSON)
          (Partitioned by Year/Month/Day)
                        │
                        ▼
            Silver Layer (Parquet)
          (Cleaned & Standardized Data)
                        │
                        ▼
              Gold Layer (Star Schema)
        ┌─────────────────────────────┐
        │      Dimension Tables       │
        │      Fact Table             │
        └─────────────────────────────┘
                        │
                        ▼
                  Amazon S3
                        │
                        ▼
               AWS Glue Crawlers
                        │
                        ▼
             AWS Glue Data Catalog
                        │
                        ▼
                 Amazon Athena
```

---

# Tech Stack

- Python
- Pandas
- YouTube Data API v3
- Amazon S3
- AWS Secrets Manager
- AWS Glue Crawlers
- AWS Glue Data Catalog
- Amazon Athena
- Parquet
- JSON
- Git & GitHub

---

# Project Structure

```
youtube-data-engineering-pipeline/

├── clients/
├── config/
├── extractors/
├── loaders/
├── pipeline/
├── transform/
├── utils/
├── logs/
│
├── data/
│
│   ├── bronze/
│   │   ├── channel/
│   │   ├── videos/
│   │   ├── video_statistics/
│   │   └── metadata/
│   │
│   ├── silver/
│   │   ├── channel/
│   │   ├── videos/
│   │   ├── video_statistics/
│   │   └── metadata/
│   │
│   └── gold/
│       ├── dim_channel/
│       ├── dim_video/
│       ├── dim_date/
│       └── fact_video_performance/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Medallion Architecture

## Bronze Layer

Raw data extracted from YouTube API.

Format:

- JSON

Datasets:

- Channel
- Videos
- Video Statistics
- Pipeline Metadata

Partitioning:

```
year=YYYY/month=MM/day=DD
```

---

## Silver Layer

Cleaned and standardized datasets.

Format:

- Parquet

Datasets:

- Channel
- Videos
- Video Statistics
- Metadata

Transformations:

- Data type conversion
- Column selection
- Schema standardization
- Data cleaning

---

## Gold Layer

Analytics-ready dimensional model.

### Dimension Tables

- dim_channel
- dim_video
- dim_date

### Fact Table

- fact_video_performance

Metrics:

- Views
- Likes
- Comments
- Video Duration

---

# AWS Services Used

## Amazon S3

Acts as the Data Lake storing:

- Bronze
- Silver
- Gold

---

## AWS Secrets Manager

Secure storage for:

- YouTube API Key

---

## AWS Glue Crawlers

Automatically discover schemas for:

- Bronze Layer
- Silver Layer
- Gold Layer

---

## AWS Glue Data Catalog

Creates metadata tables for Athena queries.

---

## Amazon Athena

Run SQL queries directly on S3 datasets.

Example:

```sql
SELECT *
FROM dim_video_parquet
LIMIT 10;
```

---

# Pipeline Flow

```
Extract
      │
      ▼
Bronze (JSON)
      │
      ▼
Transform
      │
      ▼
Silver (Parquet)
      │
      ▼
Gold (Star Schema)
      │
      ▼
Upload to Amazon S3
      │
      ▼
Glue Crawlers
      │
      ▼
Glue Catalog
      │
      ▼
Athena Analytics
```

---

# Features

- Modular ETL architecture
- Bronze/Silver/Gold design
- Incremental date partitioning
- Metadata generation
- Structured logging
- Retry handling for API failures
- Parquet optimization
- AWS Secrets Manager integration
- AWS Glue Crawlers
- AWS Glue Data Catalog
- Amazon Athena integration

---

# Current Status

## Sprint 1

- Project Setup
- YouTube API Integration

Completed

---

## Sprint 2

- Bronze Layer
- JSON Storage
- Metadata
- Logging

Completed

---

## Sprint 3

- Silver Layer
- Parquet Conversion
- Data Cleaning

Completed

---

## Sprint 4

- Gold Layer
- Star Schema
- Fact & Dimension Tables

Completed

---

## Sprint 5

- Amazon S3 Integration
- AWS Glue Crawlers
- AWS Glue Data Catalog
- Amazon Athena
- End-to-End AWS Data Lake

Completed

---

## Sprint 6 (Next)

- Amazon MWAA
- Apache Airflow DAG
- Workflow Scheduling
- Pipeline Orchestration

---

# Future Enhancements

- Amazon MWAA
- CI/CD using GitHub Actions
- Docker support
- Unit Testing
- Data Quality Validation
- Monitoring & Alerting
- Infrastructure as Code (Terraform)

---

# Author

**Obul Reddy**

Data Engineering Portfolio Project
