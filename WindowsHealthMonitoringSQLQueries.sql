-- Create Database
CREATE DATABASE WindowsMonitoring;
GO

-- Use the newly created database
USE WindowsMonitoring;
GO

-- Create Table
CREATE TABLE usage_data (
    id INT IDENTITY(1,1) PRIMARY KEY,
    timestamp DATETIME,
    cpu_percent FLOAT,
    memory_percent FLOAT,
    bytes_sent BIGINT,
    bytes_received BIGINT,
    read_bytes BIGINT,
    write_bytes BIGINT,
    disk_percent FLOAT
);
GO

select * from usage_data;


SELECT TOP 10 *
FROM usage_data
ORDER BY id DESC
