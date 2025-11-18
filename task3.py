import sys

def parse_log_line(line: str) -> dict:
    # Парсить один рядок лог-файлу
    # Повертає словник або None, якщо рядок некоректний
    try:
        parts = line.strip().split(" ", 3)
        if len(parts) < 4:
            return None

        date, time, level, message = parts

        return {
            "date": date,
            "time": time,
            "level": level,
            "message": message
        }

    except Exception:
        return None

def load_logs(file_path: str) -> list:
    # Зчитує лог-файл і повертає список словників
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)

    except FileNotFoundError:
        print("Файл не знайдено")
        sys.exit(1)

    except PermissionError:
        print("Недостатньо прав для читання файлу")
        sys.exit(1)

    except Exception as e:
        print(f"Помилка під час читання файлу: {e}")
        sys.exit(1)

    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    # Повертає всі записи вказаного рівня логування
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))

def count_logs_by_level(logs: list) -> dict:
    #Підраховує кількість записів для кожного рівня
    counts = {}
    for log in logs:
        lvl = log["level"]
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts

def display_log_counts(counts: dict):
    # Виводить таблицю з підрахунком логів за рівнями
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до лог-файлу у форматі: python main.py path/to/logfile.log error")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Перевіряємо, чи передано фільтр
    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered = filter_logs_by_level(logs, level)

        if not filtered:
            print(f"\nЛогів рівня '{level.upper()}' не знайдено")
            return

        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
