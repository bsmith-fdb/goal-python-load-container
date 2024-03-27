import zipfile
import requests

DOWNLOAD_URL = "https://www.fda.gov/media/76860/download?attachment"
DOWNLOAD_FILE = "orange_book.zip"
EXTRACT_DIR = "orange_book"
FILENAMES = ["exclusivity.txt", "patent.txt", "products.txt"]

# https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
print("Downloading file")
response = requests.get("https://www.fda.gov/media/76860/download?attachment")

print("Writing to disk")
with open("orange_book.zip", "wb") as f:
    f.write(response.content)

print("Extracting files")
with zipfile.ZipFile("orange_book.zip", "r") as z:
    z.extractall("orange_book")

print("Processsing files")
for filename in FILENAMES:
    print(f"Reading {filename}")
    with open(f"{EXTRACT_DIR}/{filename}", "r") as f:
        num_lines = sum(1 for line in f)
        print(f"Number of lines: {num_lines}")
