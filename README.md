
# Windows Health Monitoring

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

Windows Health Monitoring is a real-time system monitoring project that tracks and visualizes key performance metrics on a Windows machine. The project provides insights into CPU usage, memory consumption, network activity, disk I/O, and more.

## Features

- Real-time monitoring of CPU, memory, network, and disk.
- Data collection using Python and psutil library.
- Storage of metrics in SQL Server database using pyodbc.
- Visualization of insights through Power BI.

## Prerequisites

Ensure you have the following installed:

- Python (version 3.11)
- psutil library (install using `pip install psutil`)
- pyodbc library (install using `pip install pyodbc`)
- SQL Server for data storage
- Power BI for visualization

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/nehalbk/Windows-Health-Monitoring.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure SQL Server connection run the SQL queries required in the [WindowsHealthMonitoringSQLQueries.sql](WindowsHealthMonitoringSQLQueries.sql) file.

4. Run the monitoring script:

    ```bash
    python monitor.py
    ```

## Usage

1. Start the monitoring script to collect real-time data.

2. Access Power BI to visualize the collected metrics.

3. Analyze the insights for efficient system performance.

## Contributing

Contributions are welcome! Please check the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
