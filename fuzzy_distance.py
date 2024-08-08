# fuzzy_distance.py
from fuzzywuzzy import fuzz
import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting Fuzzy Distance Calculation...")

def fuzzy_distance(name1, name2):
    distance = 100 - fuzz.token_set_ratio(name1, name2)
    logging.debug(f"Fuzzy distance between '{name1}' and '{name2}': {distance}")
    return distance

