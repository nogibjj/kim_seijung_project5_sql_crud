"""
Extract a dataset from a URL like Kaggle or data.gov.
JSON or CSV formats tend to work well.
"""
import os
import requests

# Extracts the Titanic dataset
def extract(
    url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
    file_path="data/titanic.csv",
):
    """Extract a dataset from a URL to a specified file path."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with requests.get(url) as response:
        with open(file_path, 'wb') as file:
            file.write(response.content)
    return file_path

if __name__ == "__main__":
    extract()