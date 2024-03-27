import zipfile
import requests
import os

DOWNLOAD_URL = "https://www.fda.gov/media/76860/download?attachment"
DOWNLOAD_FILE = "orange_book_data.zip"
EXTRACT_DIR = "orange_book_data"
FILENAMES = ["exclusivity.txt", "patent.txt", "products.txt"]

# https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
print(f"Downloading file {DOWNLOAD_URL}")
response = requests.get(DOWNLOAD_URL)

print(f"Writing file to disk {DOWNLOAD_FILE}")
with open(DOWNLOAD_FILE, "wb") as f:
    f.write(response.content)

print("Extracting files")
with zipfile.ZipFile(DOWNLOAD_FILE, "r") as z:
    z.extractall(EXTRACT_DIR)

print("Processsing files")
for filename in FILENAMES:
    file_path = os.path.join(EXTRACT_DIR, filename)
    print(f"Reading file {file_path}")
    with open(file_path, "r") as f:
        num_lines = sum(1 for line in f)
        print(f"Number of lines: {num_lines}")
