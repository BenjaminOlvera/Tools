import os
import config

def search(path, ext):
    """Search for files within the given path and with the given extension. Distingish
    between capital and lower letters.

    Args:
        path (string): PATH to search
        ext (string): File extension
    """
    keyword = input("Search For?: ")  # ask the user for keyword

    root_dir = path  # path to the root directory to search
    extension = ext

    for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
        for filename in files:  # iterate over the files in the current dir
            if (filename.endswith(ext)) and (keyword in filename):
                file_path = os.path.join(root, filename)  # build the file path
                print(file_path)
    print("\n")

if __name__ == "__main__":
    # paths
    root      = config.root
    documents = config.documents
    downloads = config.downloads
    school    = config.school
    
    while(True):
        search(downloads, ".pdf")