from setuptools import find_packages, setup

setup(
    name="dbt_dagster_project",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "dbt_dagster_project": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-postgres<1.10",
        "dbt-bigquery<1.10",
        "dbt-snowflake<1.10",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)