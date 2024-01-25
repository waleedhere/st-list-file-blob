# st-list-file-blob
This repo contains script which can perform number of action regarding Azure storage account and blob.
# Python Script for Listing Containers and its content
- **'list-containers-content'** This script will list all the files and the blob inside the Azure Storage Account.
- **'list-containers-content-v1'** This script will list all the files and the blob inside the Azure Storage Account and create new output .csv file for every 1 million entries.
- **'list-metadata-from-output.py'** This script list metadata for the blob by reading it from an input file and generate output file.

**Here are the folloing requirements to run the sccript:**
- pip install azure-storage-blob
- pip install pandas
- SAS token with 'list' right and to have acces
- SAS token with 'list' and 'read' to have access to read metadata for the script 'list-metadata-from-output.py'