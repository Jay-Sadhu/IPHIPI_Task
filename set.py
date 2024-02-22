import os
import shutil

def copy_wav_files(source_dir, destination_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through each folder in the source directory
    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)
        if os.path.isdir(folder_path):
            # Look for the '1m' folder inside each folder
            subfolder_path = os.path.join(folder_path, '7m')
            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                # Iterate through .wav files in the '1m' folder
                for file_name in os.listdir(subfolder_path):
                    if file_name.endswith('.wav'):
                        # Create a unique name for the file in the destination directory
                        unique_name = folder_name + '_' + file_name
                        # Copy the .wav file to the destination directory with the unique name
                        shutil.copy(os.path.join(subfolder_path, file_name), os.path.join(destination_dir, unique_name))

# Example usage:
source_directory = r"C:\Users\jayva\Downloads\IPHIPI_0008_processes\IPHIPI_0008\IPHIPI_0008\wav_files"
destination_directory = r"C:\Users\jayva\Desktop\Personal\data\iphipi_0008\7m"
copy_wav_files(source_directory, destination_directory)
