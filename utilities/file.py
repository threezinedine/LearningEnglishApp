import os 


def create_folder_if_not_exist(folder_name):
    if os.path.isdir(folder_name):
        return
    else:
        os.makedirs(folder_name)

def get_list_file_paths(folder_name):
    try:
        files = os.listdir(folder_name)
        results = [os.path.join(folder_name, file) for file in files]
        return results
    except Exception as e:
        print(e)
        return []
