# normalize_company_name.py
import re
import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting Normalizing..")
# Legal structure suffixes
legal_suffixes = ["INC", "LLC", "LLP", "CORP", "CORPORATION", "LTD", "LIMITED", "CO", "COMPANY"]

def normalize_company_name(name):
    logging.debug(f"Normalizing company name: {name}")
    # Remove legal structure suffixes
    for suffix in legal_suffixes:
        name = re.sub(r'\b' + suffix + r'\b', '', name, flags=re.IGNORECASE)
    # Remove punctuation and extra whitespace
    name = re.sub(r'[^\w\s]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    normalized_name = name.upper()
    logging.debug(f"Normalized company name: {normalized_name}")
    return normalized_name
