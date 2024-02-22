import os

def change_extension_to_wav(folder_path):
    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, file_name)
        # Check if the item is a file
        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(file_path)
            # If the file doesn't have a .wav extension
            if extension != '.wav':
                # Rename the file with .wav extension
                new_file_path = file_path + '.wav'
                os.rename(file_path, new_file_path)
                print(f"Changed extension of '{file_path}' to '{new_file_path}'.")

# Example usage:
folder_path = r"C:\Users\jayva\Desktop\Personal\data\mallika (no distance)\5m"
change_extension_to_wav(folder_path)
