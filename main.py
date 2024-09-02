import argparse
from fpdf import FPDF
from datetime import datetime


def generate_receipt(start_date, end_date, nightly_rate):
    # Calculate the number of nights, including both start and end dates
    start_date_obj = datetime.strptime(start_date, '%d-%m-%Y')
    end_date_obj = datetime.strptime(end_date, '%d-%m-%Y')
    num_nights = (end_date_obj - start_date_obj).days + 1  # Adding 1 to include both start and end date

    # Total cost calculation
    total_cost = num_nights * nightly_rate

    # Get the current date in the desired format (e.g., "Monday 4th December 2023")
    current_date = datetime.now().strftime("%A %d %B %Y")

    # Create a PDF document
    pdf = FPDF()
    pdf.add_page()

    # Address in the top left corner
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, "The Coach House\nSouthbourne House\nHigh Street\nBlakesley\nNorthants\nNN12 8RE")

    # Add the current date below the address
    pdf.ln(5)  # Add a small line break
    pdf.cell(0, 10, current_date, ln=True)

    # Add some spacing after the current date
    pdf.ln(10)

    # Title and headings
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Receipt', ln=True, align='C')
    pdf.ln(10)

    # Body text
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'{num_nights} nights accommodation @ £{nightly_rate}/night', ln=True)
    pdf.cell(0, 10, f'{start_date} - {end_date}', ln=True)
    pdf.cell(0, 10, f'Total: £{total_cost:.2f}', ln=True)

    # Generate the filename based on the date range
    filename = f"The Coach House receipt {start_date} to {end_date}.pdf"

    # Output the PDF to a file
    pdf.output(filename)


if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Generate a PDF receipt for accommodation.")

    # Adding arguments with both long and short options
    parser.add_argument("-s", "--start_date", type=str, required=True, help="Start date in format DD-MM-YYYY")
    parser.add_argument("-e", "--end_date", type=str, required=True, help="End date in format DD-MM-YYYY")
    parser.add_argument("-r", "--nightly_rate", type=float, default=60.0, help="Nightly rate in GBP (default is 60)")

    # Parse the arguments
    args = parser.parse_args()

    # Generate the receipt
    generate_receipt(args.start_date, args.end_date, args.nightly_rate)
