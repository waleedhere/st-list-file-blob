import csv
from azure.storage.blob import BlobServiceClient

ACCOUNT_NAME = "xxx"
SAS_TOKEN = "xxx"

blob_service_client = BlobServiceClient(account_url=f"https://{ACCOUNT_NAME}.blob.core.windows.net", credential=SAS_TOKEN)

def list_blob_metadata_to_csv(csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['Container', 'Blob', 'Metadata']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()

        containers = blob_service_client.list_containers()

        for container in containers:
            container_client = blob_service_client.get_container_client(container.name)
            blobs = container_client.list_blobs()

            for blob in blobs:
                blob_client = container_client.get_blob_client(blob.name)
                blob_properties = blob_client.get_blob_properties()

                metadata = blob_properties.metadata
                writer.writerow({
                    'Container': container.name,
                    'Blob': blob.name,
                    'Metadata': metadata
                })

def main():
    csv_file = 'blob_metadata.csv'
    print(f"\nList metadata for every blob in the Azure Storage account and write to {csv_file}")
    list_blob_metadata_to_csv(csv_file)

if __name__ == "__main__":
    main()