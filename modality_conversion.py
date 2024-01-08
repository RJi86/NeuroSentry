import nibabel as nib
import os
from tqdm import tqdm

input_folder = os.path.expanduser('~/media/nnUNet_raw/Task003_BrainTumour/imagesTr')
output_folder = os.path.expanduser('~/media/nnUNet_raw/Task003_BrainTumour/imagesTr')

def split_modalities(input_folder, output_folder):
    filenames = os.listdir(input_folder)
    for filename in tqdm(filenames, desc="Processing images"):
        if filename.endswith(".nii.gz") and not filename.startswith("._"):
            img = nib.load(os.path.join(input_folder, filename))
            data = img.get_fdata()
            # Check if the image has 4 modalities
            if data.shape[-1] == 4:
                for i in range(data.shape[-1]):
                    new_data = data[..., i]
                    new_img = nib.Nifti1Image(new_data, img.affine, img.header)
                    new_filename = f'{filename.replace(".nii.gz", "")}_{str(i).zfill(4)}.nii.gz'
                    new_filepath = os.path.join(output_folder, new_filename)
                    # Check if the file already exists
                    if not os.path.exists(new_filepath):
                        nib.save(new_img, new_filepath)

split_modalities(input_folder, output_folder)
