from pathlib import Path

def list_nas_files(nas_path_str):
    """
    list all the files and directories under the specific NAS path
    """
    nas_path = Path(nas_path_str)

    # Check if the path exists
    if not nas_path.exists():
        print(f"路徑{nas_network_path}不存在")
        return
    
    # Use iterdir() to list sub-items
    # for entry in nas_path.iterdir():
    for entry in nas_path.rglob('*'):
        if entry.is_dir():
            print(f"資料夾：{entry.name} @ {entry}")
        else:
            print(f"檔案： {entry.name} @ {entry.parent}")

if __name__ == "__main__":
    # fill in the NAS path
    # nas_network_path = r"/home/jfy/Desktop"
    nas_network_path = r"/media/nas/200/1_Projects/2_Ongoing/2025"
    list_nas_files(nas_network_path)
            
