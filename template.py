# import libraries
import os
from pathlib import Path
import logging

# logging for files
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project name
project_name = "mlproject"

project_structure = [
    ".github/workflows/.gitkeep",  # Placeholder for GitHub Actions workflows

    # Source Code Structure
    f"src/{project_name}/__init__.py",  # Initialize main package
    f"src/{project_name}/components/__init__.py",  # Data ingestion, transformation, etc.
    f"src/{project_name}/utils/__init__.py",  # Utility functions package
    f"src/{project_name}/utils/common.py",  # Common reusable utilities
    f"src/{project_name}/config/__init__.py",  # Configuration package
    f"src/{project_name}/config/configuration.py",  # Configuration loading and validation
    f"src/{project_name}/pipeline/__init__.py",  # ML pipeline stages
    f"src/{project_name}/entity/__init__.py",  # Entity/data schema package
    f"src/{project_name}/entity/config_entity.py",  # Configuration entities as dataclasses
    f"src/{project_name}/constant/__init__.py",  # Constants used across modules

    # Configuration and Parameters
    "config/config.yaml",  # Project configuration file
    "params.yaml",         # ML model parameters (e.g., alpha, n_estimators)
    "schema.yaml",         # Schema definition for input data

    # Entry Points
    "main.py",  # Main script to trigger training pipeline
    "app.py",   # REST API for prediction using Flask or FastAPI

    # Environment & Deployment
    "Dockerfile",         # Docker setup for containerization
    "requirements.txt",   # Python dependencies
    "setup.py",           # Project setup for pip install

    # Experiments and Visualization
    "notebook/eda.ipynb",      # Jupyter notebook for exploratory data analysis
    "templates/index.html"     # Web interface (for Flask/FastAPI frontend)
]

for filepath in project_structure:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")

    # Create the empty file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # creates empty file or updates the timestamp
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")


