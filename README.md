# Digitalxc Secret Santa Assignment

This project provides a **Secret Santa** assignment functionality for managing a list of employees and assigning them "Secret Children" while ensuring that no employee is assigned to themselves or to someone they were a Secret Santa for previously. 

The program also handles reading and writing employee data from CSV files and generates dynamic file names using an epoch timestamp.

## Features

- **Secret Santa Assignment**: Randomly assigns employees to other employees as "Secret Santa" (Secret Child), while ensuring that previous assignments are taken into account.
- **CSV File Operations**: Supports reading and writing employee data from CSV files, allowing easy import/export of employee lists.
- **Epoch Timestamp Generation**: Generates dynamic file names with epoch timestamps to avoid overwriting previous files.
- **Exception Handling**: Proper error handling to ensure data integrity and graceful failure in case of missing information or incorrect data.

## Project Structure


### Files Overview

- **`secretSanta.py`**: The core logic for the Secret Santa assignment, where employees are randomly assigned to other employees as Secret Santas, avoiding prior assignments.
- **`fileOperation.py`**: Contains logic for reading employee data from CSV files and writing the results back to a new CSV file.
- **`utils.py`**: Contains utility functions, including one to generate dynamic file names based on the current epoch timestamp.
- **`main.py`**: The main entry point for executing the Secret Santa assignment process.
- **`/assets`**: This folder contains CSV files for employee data and previous year’s assignments:
  - `previous_year_data.csv`: Contains the Secret Santa assignments from the previous year.
  - `employee_data.csv`: Contains the current year’s list of employees to be assigned Secret Santas.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/joel2592001/Digitalxc.git


