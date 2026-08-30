# KIEP — Kenya Economic Intelligence Platform

A data engineering and analytics platform that collects, stores, transforms, and analyzes Kenyan economic and financial data to generate actionable insights.

## 🎯 Project Overview

KIEP is designed to demonstrate end-to-end data engineering skills by building a pipeline that:

- **Collects** real Kenyan economic data from various sources (APIs, government databases)
- **Stores** data in a PostgreSQL database with proper schema design
- **Transforms** raw data into analytics-ready tables
- **Analyzes** relationships between economic indicators
- **Visualizes** insights through interactive dashboards

## 🏗️ Architecture

```
┌─────────────┐    ┌──────────────┐    ┌────────────┐    ┌───────────┐
│ Data Sources │───▶│ Python Ingest│───▶│ PostgreSQL │───▶│ Dashboard │
│  (APIs/CSV)  │    │  (Extract)   │    │ (Store +   │    │ (Display) │
└─────────────┘    └──────────────┘    │ Transform) │    └───────────┘
                                       └────────────┘
```

## 📊 Data Areas

1. Kenyan inflation rates
2. USD/KES exchange rates
3. Kenyan interest rates
4. Fuel prices
5. Food prices
6. Nairobi Securities Exchange (NSE) market data
7. Imports and exports
8. Economic events and announcements

## 🛠️ Technologies

- **Python 3.10+** — Data ingestion and pipeline automation
- **PostgreSQL 15+** — Relational database
- **Pandas** — Data manipulation
- **SQL** — Data transformations and analytics
- **Git/GitHub** — Version control
- **Power BI** — Dashboard visualization
- **Docker** — Reproducible environment (future)

## 📁 Project Structure

```
kiep/
├── README.md
├── .gitignore
├── requirements.txt
├── docs/
│   ├── data_dictionary.md
│   └── architecture.md
├── src/
│   ├── ingestion/        # Data collection scripts
│   ├── transformation/   # Data cleaning/transformation
│   └── utils/            # Helper functions
├── data/
│   ├── raw/              # Raw downloaded data
│   └── processed/        # Cleaned/transformed data
├── sql/                  # SQL scripts and queries
└── tests/                # Data validation tests
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL 15+
- Git
### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/markmureithi346-byteclea/kiep.git
   cd kiep
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL database
   ```bash
   # Create database
   createdb kiep_db
   ```

## 📈 Example Questions This Project Answers

- How does inflation relate to fuel prices in Kenya?
- How does USD/KES movement affect inflation?
- Do interest rate changes impact the NSE?
- Which economic indicators move together?
- Can we forecast economic trends from historical data?

## ⚠️ Limitations

- Data availability depends on public sources
- Historical data may have gaps
- This is a learning project, not production-grade

##  Mark Mureithi Mwangi

[Your Name] — Computer Engineering Student

## 📝 License

This project is for educational purposes.