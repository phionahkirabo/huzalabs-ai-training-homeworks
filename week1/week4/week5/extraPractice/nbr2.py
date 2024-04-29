import os

def countFiles(path):
    # Base case: if the path does not exist or is not a directory, return 0
    if not os.path.exists(path) or not os.path.isdir(path):
        return 0
    
    total_files = 0
    
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
       
        if os.path.isdir(full_path):
            total_files += countFiles(full_path)
        
        elif os.path.isfile(full_path):
            total_files += 1
    
    return total_files
