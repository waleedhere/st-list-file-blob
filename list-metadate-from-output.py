import pandas as pd
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError


ACCOUNT_NAME = "xxx"
SAS_TOKEN = "xxx"

blob_service_client = BlobServiceClient(account_url=f"https://{ACCOUNT_NAME}.blob.core.windows.net", credential=SAS_TOKEN)

blob_service_client = BlobServiceClient(account_url=f"https://{ACCOUNT_NAME}.blob.core.windows.net", credential=SAS_TOKEN)

def fetch_blob_metadata(input_excel, output_excel):
    df = pd.read_excel(input_excel)

    result = []
    for _, row in df.iterrows():
        blob_name = row['Blob']
        container_name = row['Container']

        try:
            container_client = blob_service_client.get_container_client(container_name)
            container_client.get_container_properties()  # Check if the container exists
        except ResourceNotFoundError:
            print(f"Container '{container_name}' does not exist.")
            continue

        blob_client = container_client.get_blob_client(blob_name)

        try:
            blob_properties = blob_client.get_blob_properties()
            metadata = blob_properties.metadata
            result.append({
                'Container': container_name,
                'Blob': blob_name,
                'Metadata': metadata
            })
        except Exception as e:
            print(f"Error fetching metadata for blob '{blob_name}' in container '{container_name}': {str(e)}")

    result_df = pd.DataFrame(result)
    result_df.to_excel(output_excel, index=False)

def main():
    input_excel_file = 'input_blobs.xlsx'  # Replace with your input Excel file
    output_excel_file = 'output_blob_metadata.xlsx'  # Replace with your desired output Excel file

    fetch_blob_metadata(input_excel_file, output_excel_file)
    print(f"Blob metadata fetched and saved to {output_excel_file}")

if __name__ == "__main__":
    main()