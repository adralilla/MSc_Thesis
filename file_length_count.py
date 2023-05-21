import pandas as pd
import os
from tqdm import tqdm
from Bio import SeqIO

base_folder_path = "./inherit_download/"
base_folders = {
    "test": "data_test/Test/",
    "train": "data_train/Training/",
    "validation": "data_validation/Validation/",
}
folders = ["Bacteria", "Phages"]
df = pd.DataFrame(columns=["id", "label", "length", "group"])
for base, subfolder_path in base_folders.items():
    for folder in folders:
        folder_path = f"{base_folder_path}{subfolder_path}{folder}/"
        for fasta_file in tqdm(os.listdir(folder_path)):
            for seq_record in SeqIO.parse(folder_path + fasta_file, "fasta"):
                df = pd.concat(
                    [
                        df,
                        pd.DataFrame(
                            [
                                {
                                    "id": seq_record.id,
                                    "label": folder,
                                    "length": len(seq_record.seq),
                                    "group": base,
                                }
                            ]
                        ),
                    ],
                    ignore_index=True,
                )

df.to_csv("file_lengths.csv")
