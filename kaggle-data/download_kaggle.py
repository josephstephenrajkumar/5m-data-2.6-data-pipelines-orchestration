import kagglehub
import os
import shutil

def main():
    # Step 1: Download the dataset
    dataset = "olistbr/brazilian-ecommerce"
    print(f"Downloading dataset: {dataset}")

    path = kagglehub.dataset_download(dataset)
    print("\n✔ Dataset downloaded!")
    print("KaggleHub storage path:", path)

    # Step 2: Move files to a project folder (optional)
    target_folder = "kaggle_dataset"
    os.makedirs(target_folder, exist_ok=True)

    for file in os.listdir(path):
        shutil.copy(os.path.join(path, file), target_folder)

    print(f"\n✔ Files copied to: {os.path.abspath(target_folder)}")

if __name__ == "__main__":
    main()
