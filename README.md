# Coach House Receipt Generator

This script generates a PDF receipt for accommodation based on the start and end dates, and a nightly rate. It calculates the total cost and dynamically generates the filename based on the date range.

## Features

- Automatically calculates the number of nights, including both start and end dates.
- Generates a receipt in PDF format with the accommodation details and total cost.
- Includes the current date and address in the PDF.
- Dynamically generates the filename based on the date range.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

- Run the script with the required parameters for start date, end date, and optionally a nightly rate (default is £60):

```bash
python main.py -s <start_date> -e <end_date> -r <nightly_rate>
```

## Example:

```bash
python main.py -s 21-08-2024 -e 22-08-2024 -r 60
```