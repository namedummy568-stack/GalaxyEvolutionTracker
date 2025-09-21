def process_galaxy_data(data):
    # Simulate data processing
    print(f"Processing {len(data)} data points...")
    processed_data = [d.upper() for d in data] # Example processing
    return processed_data

if __name__ == "__main__":
    sample_data = ["galaxy_a_spectrum", "galaxy_b_luminosity", "galaxy_c_redshift"]
    result = process_galaxy_data(sample_data)
    print("Processed data:", result)