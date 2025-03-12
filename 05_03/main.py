import sys
from pathlib import Path
from hw_05_03 import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts


def main():
    _, file_path, *argv = sys.argv
    file_path = Path(file_path)

    log_type = argv[0] if argv else None
    
    if not file_path.exists():
        print(f'File not exists: {file_path}')
        return
    
    if not file_path.is_file():
        print(f'It is not a file: {file_path}')
        return

    try:
        list_of_logs = load_logs(file_path)
    except Exception as e:
        print(f"Error loading logs: {e}")
        return
    
    logs_info_by_level = count_logs_by_level(list_of_logs)

    display_log_counts(logs_info_by_level)
    
    if argv:
        log_type = argv[0].upper()
        details_list = filter_logs_by_level(list_of_logs, log_type)
        
        if not details_list:
            print(f"No logs with level '{log_type}'")
        else:
            print(f"Log details for '{log_type}' level:")

            for log in details_list:
                item_log_info = " ".join(log.values())
                print(item_log_info)


if __name__ == '__main__':
    main()
