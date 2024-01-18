from azure.storage.blob import BlockBlobService
import csv

ACCOUNT_NAME = "xx"
SAS_TOKEN = 'xxxx'

blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=None, sas_token=SAS_TOKEN)


def list_containers_and_contents(file_index):
    csv_file_name = f'BlobsNames_{file_index}.csv'
    row_count = 0

    with open(csv_file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Container", "Blob"])  # Add header to the CSV file

        containers = blob_service.list_containers()
        for c in containers:
            generator = blob_service.list_blobs(c.name)

            if not any(generator):  # Check if the container is empty
                print(f"\t Empty Container: {c.name}")
                writer.writerow([c.name, ""])
                row_count += 1
            else:
                for blob in generator:
                    print("\t Blob name: " + c.name + '/' + blob.name)
                    writer.writerow([f"{c.name}/{blob.name}"])
                    row_count += 1

                    if row_count >= 1000000:
                        print("Reached 1 million rows. Creating a new CSV file.")
                        return True

    return False

def main():
    print("\nList blobs in the container")
    file_index = 1

    while True:
        print(f"Processing CSV File {file_index}")
        need_new_file = list_containers_and_contents(file_index)

        if not need_new_file:
            break

        file_index += 1

if __name__ == "__main__":
    main()