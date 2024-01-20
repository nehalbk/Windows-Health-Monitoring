import psutil
import time
from datetime import datetime
import pyodbc


def get_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    net_io_counters = psutil.net_io_counters()

    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv

    disk_io_counters = psutil.disk_io_counters()
    read_bytes = disk_io_counters.read_bytes
    write_bytes = disk_io_counters.write_bytes

    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent

    return cpu_percent, memory_percent, bytes_sent, bytes_recv, read_bytes, write_bytes, disk_percent


def save_to_database(data):
    try:
        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=WindowsMonitoring;"
           # "USER=your_user;"
           # "PASSWORD=your_password;"
            "Trusted_Connection=yes;"
        )
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "INSERT INTO usage_data (timestamp, cpu_percent, memory_percent, bytes_sent, bytes_received, read_bytes, write_bytes, disk_percent) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, data)

        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error saving to database: {e}")


if __name__ == "__main__":
    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            usage_data = (timestamp,) + get_usage()

            print(
                f"Timestamp: {timestamp}, CPU: {usage_data[1]}%, Memory: {usage_data[2]}%, Bytes Sent: {usage_data[3]}, Bytes Received: {usage_data[4]}, Read Bytes: {usage_data[5]}, Write Bytes: {usage_data[6]}, Disk Usage: {usage_data[7]}%")

            save_to_database(usage_data)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped. Data saved to the database.")
