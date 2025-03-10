import sys
from pathlib import Path
from hw_05_03 import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts

def main():
    _, file_path, *argv = sys.argv
    file_path = Path(file_path)

    [log_type, ] = argv

    print(f'Found file: {file_path}') if file_path.exists() else print(f'File not exists: {file_path}')
    print(f'It is a file: {file_path}') if file_path.is_file() else print(f'It is not a file: {file_path}')

    list_of_logs = load_logs(file_path)
    logs_info_by_level = count_logs_by_level(list_of_logs)
    print(logs_info_by_level)

    display_log_counts(logs_info_by_level)
    
    if log_type:
        details_list = filter_logs_by_level(list_of_logs, log_type)
        
        print(f"Log details for '{log_type.upper()}' level:")
        
        for log in details_list:
            item_log_info = []
            for value in log.values():
                item_log_info.append(value)
            item_log_info = " ".join(item_log_info)
            print(item_log_info)





if __name__ == '__main__':
    main()