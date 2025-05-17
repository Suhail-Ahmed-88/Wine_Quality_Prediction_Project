from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    return requirements_list


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

Repo_Name = "Wine_Quality_Prediction_Project"
Author_Name = "Suhail Ahmed"
Src_Repo = "mlproject"
Author_Email = "rajpar.suhail.ahmed@gmail.com"

setup(
    name=Src_Repo,  # Your project name
    version=__version__,
    author=Author_Name,
    author_email=Author_Email,
    description="A machine learning project to predict wine quality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/wine_quality_prediction",  # Replace with your repo
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/wine_quality_prediction/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements(),
    python_requires=">=3.10",
)