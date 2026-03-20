import tabula
import argparse
import sys

def convert_pdf_to_csv(input_pdf, output_csv):
    try:
        print(f"Reading tables from {input_pdf}...")
        # pages='all' ensures it captures tables from both Page 1 and Page 2
        tabula.convert_into(input_pdf, output_csv, output_format="csv", pages='all')
        print(f"Successfully saved to {output_csv}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF tables to a CSV file.")
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument("output", help="Name/Path for the output CSV file")
    
    args = parser.parse_args()
    convert_pdf_to_csv(args.input, args.output)
