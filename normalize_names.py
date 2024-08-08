# normalize_names.py
import pandas as pd
import logging
from normalize_company_name import normalize_company_name
from compute_distance_matrix import compute_distance_matrix
from determine_canonical_names import determine_canonical_names

# Configure logging for the main script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def normalize_names(input_file, output_file):
    logging.info(f"Processing file: {input_file}")
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Normalize the organization names
        df['Normalized Organization'] = df['organization'].apply(normalize_company_name)
        
        # Determine canonical names
        canonical_names = determine_canonical_names(df, compute_distance_matrix)
        
        # Apply canonical names to the DataFrame
        df['Canonical Organization'] = df['Normalized Organization'].map(canonical_names)
        df = df.drop(columns=['Normalized Organization'])
        df = df.rename(columns={"Canonical Organization":"normalized organization"})
        
        # Write the output to a new CSV file
        df.to_csv(output_file, index=False)
        logging.info(f"Normalized data written to: {output_file}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Normalize company names in a CSV file.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file.')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file.')
    
    args = parser.parse_args()
    
    normalize_names(args.input_file, args.output_file)
