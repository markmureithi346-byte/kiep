# Database connection module for KIEP
# This module handles PostgreSQL database connections

import os
from typing import Optional

import psycopg2
from dotenv import load_dotenv


def load_config():
    """Load database configuration from environment variables."""
    load_dotenv()

    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432"),
        "database": os.getenv("DB_NAME", "kiep_db"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "")
    }


def get_connection():
    """Create and return a database connection."""
    config = load_config()

    try:
        connection = psycopg2.connect(
            host=config["host"],
            port=config["port"],
            database=config["database"],
            user=config["user"],
            password=config["password"]
        )

        print("Database connection successful")
        return connection

    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise


def execute_query(
    connection,
    query: str,
    params: Optional[tuple] = None
):
    """Execute a SQL query."""

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)

            if cursor.description:
                result = cursor.fetchall()
            else:
                result = None

        connection.commit()
        return result

    except psycopg2.Error as e:
        connection.rollback()
        print(f"Query execution failed: {e}")
        raise


def close_connection(connection):
    """Close database connection."""

    if connection:
        connection.close()
        print("Database connection closed")
        