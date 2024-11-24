# Digitalxc Secret Santa Assignment

This project provides a **Secret Santa** assignment functionality for managing a list of employees and assigning them "Secret Children" while ensuring that no employee is assigned to themselves or to someone they were a Secret Santa for previously. 

The program also handles reading and writing employee data from CSV files and generates dynamic file names using an epoch timestamp.

## Features

- **Secret Santa Assignment**: Randomly assigns employees to other employees as "Secret Santa" (Secret Child), while ensuring that previous assignments are taken into account.
- **CSV File Operations**: Supports reading and writing employee data from CSV files, allowing easy import/export of employee lists.
- **Epoch Timestamp Generation**: Generates dynamic file names with epoch timestamps to avoid overwriting previous files.
- **Exception Handling**: Proper error handling to ensure data integrity and graceful failure in case of missing information or incorrect data.

## Project Structure

