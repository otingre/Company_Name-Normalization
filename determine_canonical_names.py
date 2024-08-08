# determine_canonical_names.py
from sklearn.cluster import DBSCAN
import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def determine_canonical_names(df, compute_distance_matrix):
    logging.info("Determining canonical names...")
    names = df['Normalized Organization'].tolist()
    cities = df['city'].tolist()
    countries = df['country'].tolist()
    
    # Compute the distance matrix
    distances = compute_distance_matrix(names, cities, countries)
    
    # Apply DBSCAN clustering
    clustering = DBSCAN(eps=30, min_samples=2, metric='precomputed')
    clusters = clustering.fit_predict(distances)
    
    # Determine the canonical name for each cluster
    canonical_names = {}
    for cluster_id in set(clusters):
        if cluster_id != -1:  # Ignore noise points
            cluster_indices = [i for i in range(len(names)) if clusters[i] == cluster_id]
            cluster_names = [names[i] for i in cluster_indices]
            # Choose the most frequent name in the cluster as the canonical name
            canonical_name = max(set(cluster_names), key=cluster_names.count)
            logging.debug(f"Canonical name for cluster {cluster_id}: {canonical_name}")
            for index in cluster_indices:
                canonical_names[names[index]] = canonical_name
    logging.info("Canonical Naming Done.")
    return canonical_names

