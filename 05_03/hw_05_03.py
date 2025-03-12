from collections import defaultdict

def parse_log_line(line: str) -> dict:
    date_log, time_log, type_info, *argv = line.strip().split()
    log_text = " ".join(argv)

    log_info = {
        'date': date_log,
        'time': time_log,
        'type': type_info,
        'text': log_text
    }

    return log_info
    

def load_logs(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as log:
        list_of_logs = [parse_log_line(el) for el in log.readlines()]

    return list_of_logs


def filter_logs_by_level(logs: list, level: str) -> list:
    list_of_type_logs = []
    
    for log in logs:
        for value in log.values():
          if value == level.upper():
              list_of_type_logs.append(log)

    return list_of_type_logs

def count_logs_by_level(logs: list) -> dict:
    logs_info_by_level = defaultdict(int)
    
    for log in logs:
        for key, value in log.items():
            if key == "type":
                logs_info_by_level[value] +=1

    return logs_info_by_level


def display_log_counts(counts: dict):

    level = "Рівень логування"
    count = "Кількість"
    level_length = max(len(level), max((map(len, counts.keys()))))
    count_length = max(len(count), max((map(lambda number: len(str(number)), counts.values()))))
    print(f"{level:<{level_length}} | {count:>{count_length}}")
    print(f"-"*(level_length)+ " | " + f"-"*(count_length))

    for key, value in counts.items():
        print(f"{key:<{level_length}} | {value}" )


