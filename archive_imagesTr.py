import os
import shutil
from tqdm import tqdm

input_folder = os.path.expanduser('~/media/nnUNet_raw/Task003_BrainTumour/imagesTr')
archive_folder = os.path.expanduser('~/media/nnUNet_raw/Task003_BrainTumour/archive')

def move_files(input_folder, archive_folder):
    filenames = os.listdir(input_folder)
    for filename in tqdm(filenames, desc="Moving files"):
        if filename.endswith(".nii.gz") and not any(filename.endswith(f"_{str(i).zfill(4)}.nii.gz") for i in range(4)):
            # Move the original file to the archive folder
            shutil.move(os.path.join(input_folder, filename), os.path.join(archive_folder, filename))

move_files(input_folder, archive_folder)
