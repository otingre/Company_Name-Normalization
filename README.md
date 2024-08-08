# Company Name Normalization

This project provides an algorithm to normalize company name variations in a CSV file, so that we can accurately attribute the patents granted to the canonical company names. The solution is implemented in Python and leverages fuzzy matching and clustering to handle noisy variations in company names.


- **normalize_company_name.py**: Contains the function to normalize company names.
- **fuzzy_distance.py**: Contains the function to compute fuzzy distances.
- **compute_distance_matrix.py**: Contains the function to compute the distance matrix with parallel processing.
- **determine_canonical_names.py**: Contains the function to determine canonical names using clustering.
- **normalize_names.py**: The main script that orchestrates the normalization process.
- **requirements.txt**: Lists all required Python packages.
- **README.md**: This file with instructions.

## This Script takes approximatley 5 minutes to generate the output file

## Requirements

- Python 3.x
- pip (Python package installer)

## Installation

1. pip install -r requirements.txt


## Instrctions to run the script

To normalize the company names in your CSV file, follow these steps:

1. Prepare Your CSV File: Ensure your input CSV file has the following columns: patent_id, organization, city, country.

2. Run the Main Script: Use the Python interpreter to run the normalize_names.py script. You need to have the input.csv and output.csv file under the same directory 

3. Command to run the script : python3 -u "normalize_names.py" "input.csv" "output.csv"


## Limitations of the Code

Performance Issues:
Distance Computation: The nested loops in compute_distance_matrix result in an O(n^2) time complexity, which can be slow for large datasets.
Redundant Calculations: The code recomputes the combined strings for each pair of organizations, leading to inefficiencies.

Scalability:
Memory Usage: The distance matrix is an NxN matrix, which can become very large and consume significant memory for large datasets.
Computational Cost: The fuzzy_distance function is applied pairwise, leading to high computational costs as the number of entries grows.

Accuracy and Robustness:
Fuzzy Matching Limitations: Fuzzy matching can produce false positives, especially with similar-sounding company names. This might lead to incorrect canonicalization.
DBSCAN Parameters: The eps parameter in DBSCAN is set to 25, which might not be suitable for all datasets, leading to suboptimal clustering.

Configurability:
Hardcoded Parameters: The DBSCAN parameters and the fuzzy distance threshold are hardcoded, which limits the flexibility of the script for different datasets and use cases.



## Possible Improvements

Optimize Distance Calculation:
Vectorization: Use more efficient data structures or algorithms to calculate distances in parallel or in a more optimized manner.

Improve Scalability:
Sparse Matrices: Use sparse matrix representations if the matrix is large and mostly empty.
Approximate Matching: Implement approximate nearest neighbor algorithms for faster distance computation.

Enhance Accuracy:
Better Clustering: Tune the clustering parameters or use different algorithms to improve the accuracy of canonical name determination.
Advanced Matching: Use more sophisticated text matching techniques or domain-specific knowledge to handle similar company names better.

Parameterization: Allow users to specify parameters like eps for DBSCAN and distance thresholds via command-line arguments or configuration files.

