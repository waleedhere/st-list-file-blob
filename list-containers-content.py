from azure.storage.blob import BlockBlobService

ACCOUNT_NAME = "xxxx"
SAS_TOKEN = 'xxx'

blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=None, sas_token=SAS_TOKEN)

def list_containers_and_contents():
    with open('BlobsNamesFinalcheck.csv', 'w') as f:
        f.write("Container,Blob\n")  # Add header to the CSV file

        containers = blob_service.list_containers()
        for c in containers:
            generator = blob_service.list_blobs(c.name)

            if not any(generator):  # Check if the container is empty
                print(f"\t Empty Container: {c.name}")
                f.write(f"{c.name},\n")
            else:
                for blob in generator:
                    print("\t Blob name: " + c.name + '/' + blob.name)
                    f.write(f"{c.name}/{blob.name}\n")

def main():
    print("\nList blobs in the container")
    list_containers_and_contents()

if __name__ == "__main__":
    main()