# compute_distance_matrix.py
import numpy as np
from itertools import product
from fuzzy_distance import fuzzy_distance
import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting Distance matrix computation...")

def compute_distance_matrix(names, cities, countries):
    n = len(names)
    distances = np.zeros((n, n))
    
    for i, j in product(range(n), repeat=2):
        if i != j:
            if countries[i] != countries[j]:  # Different countries, definitely not the same company
                distances[i, j] = 100
            else:
                name_distance = fuzzy_distance(names[i], names[j])
                city_distance = fuzzy_distance(cities[i], cities[j])
                distances[i, j] = max(name_distance, city_distance)
    
    logging.info("Distance matrix computation complete.")
    return distances

