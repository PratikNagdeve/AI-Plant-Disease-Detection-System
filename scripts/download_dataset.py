import kagglehub

print("Downloading PlantVillage dataset...")

path = kagglehub.dataset_download(
    "adilmubashirchaudhry/plant-village-dataset"
)

print("Dataset downloaded at:")
print(path)