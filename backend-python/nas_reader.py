from ptahlib import Path

def list_nas_files(nas_path_str):
    """
    list all the files and directories under the specific NAS path
    """
    nas_path = Path(nas_path_str)

    # Check if the path exists
    if not nas_path.exists():
        print(f"路徑不存在")
        return
    
    # Use iterdir() to list sub-items
    for entry in nas_path.iterdir():
        if entry.is_dir():
            print(f"路徑如下：{entry.name}")
        else:
            print(f"檔案： {entry.name}")

if __name__ == "__main__":
    # fill in the NAS path
    nas_network_path = r"\\200"
    list_nas_files(nas_network_path)
            
