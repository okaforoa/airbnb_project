
# Airbnb Analytics Engineering Pipeline with dbt & Dagster

This project is a comprehensive implementation of an end-to-end data transformation pipeline using **dbt (Data Build Tool)** and **Dagster**, inspired by the Udemy course *Complete dbt (Data Build Tool) Bootcamp: Zero to Hero*.
It showcases best practices in analytics engineering, focusing on modularity, testing, documentation, and orchestration.

## 📌 Project Overview

The pipeline processes Airbnb data, transforming raw datasets into structured, analytics-ready models.
It emphasizes:

- **Modular SQL Modeling**: Utilizing dbt's capabilities to create reusable and maintainable SQL models.
- **Data Testing**: Implementing both generic and custom tests to ensure data quality.
- **Documentation**: Auto-generating comprehensive documentation with dbt.
- **Orchestration**: Managing and scheduling data workflows using Dagster.

## 🛠️ Tech Stack

- **dbt Core**: For data transformation and modeling.
- **Dagster**: To orchestrate and monitor data workflows.
- **Snowflake**: As the data warehouse solution.
- **Jinja**: For templating within dbt models.
- **VS Code**: Development environment with dbt Power User extension.

## 📁 Project Structure

```
├── dbt_dagster_project/
│   ├── dbtlearn/               # dbt project directory
│   │   ├── models/             # Contains SQL models
│   │   ├── seeds/              # Seed CSV files
│   │   ├── snapshots/          # Snapshot definitions
│   │   ├── macros/             # Custom macros
│   │   ├── tests/              # Custom tests
│   │   ├── dbt_project.yml     # dbt project configuration
│   │   └── profiles.yml        # dbt profiles configuration
│   ├── dagster_project/        # Dagster project directory
│   │   ├── assets.py           # Asset definitions
│   │   ├── jobs.py             # Job definitions
│   │   ├── schedules.py        # Schedule definitions
│   │   └── sensors.py          # Sensor definitions
├── LICENSE
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Snowflake account
- VS Code with dbt Power User extension (optional but recommended)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/airbnb_dbt_dagster.git
   cd airbnb_dbt_dagster
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure dbt profiles**:

   Ensure your `profiles.yml` file is correctly set up to connect to your Snowflake account. Place this file in the appropriate directory as specified by dbt's documentation.

### Running the Pipeline

1. **Navigate to the dbt project directory**:

   ```bash
   cd dbt_dagster_project/dbtlearn
   ```

2. **Run dbt models**:

   ```bash
   dbt run
   ```

3. **Test the models**:

   ```bash
   dbt test
   ```

4. **Generate documentation**:

   ```bash
   dbt docs generate
   dbt docs serve
   ```

5. **Start Dagster for orchestration**:

   From the root directory:

   ```bash
   dagster dev
   ```

   Access the Dagster UI at `http://localhost:3000` to monitor and manage your data workflows.

## 📚 Key Concepts Covered

- **Models**: Building modular SQL models for data transformation.
- **Materializations**: Understanding table, view, incremental, and ephemeral models.
- **Sources & Seeds**: Defining external data sources and static datasets.
- **Snapshots**: Capturing historical data changes.
- **Tests**: Implementing data quality checks.
- **Macros & Jinja**: Creating reusable SQL snippets and logic.
- **Documentation**: Auto-generating project documentation.
- **Orchestration**: Scheduling and monitoring workflows with Dagster.

## 🧪 Testing & Validation

- **Generic Tests**: Utilize built-in dbt tests for nulls, uniqueness, and referential integrity.
- **Custom Tests**: Develop specific tests tailored to business logic.
- **dbt-expectations**: Integrate with the `dbt-expectations` package for advanced testing scenarios.

## 📄 Documentation

After running `dbt docs generate`, serve the documentation with `dbt docs serve` and navigate to `http://localhost:8080` to explore:

- **Model Lineage**: Visualize dependencies between models.
- **Column Descriptions**: Detailed information about each column.
- **Test Coverage**: Overview of applied tests and their statuses.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
