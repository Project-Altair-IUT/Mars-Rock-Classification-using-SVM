
def classify_rock(fe3_fe2_ratio, hydration_index, silica_content):
    """
    Classify a Martian rock based on spectral parameters.
    
    Parameters:
    fe3_fe2_ratio (float): Fe³⁺/Fe²⁺ ratio from spectral analysis
    hydration_index (float): Hydration index from spectral data
    silica_content (float): Silica content (SiO2 proportion)
    
    Returns:
    str: Rock classification - 'volcanic', 'sedimentary', or 'hydrothermal_altered'
    
    Classification logic:
    - hydrothermal_altered: Fe³⁺/Fe²⁺ ratio > 0.8 AND hydration index > 0.6
    - volcanic: silica_content > 0.7
    - sedimentary: otherwise
    """
    # Prioritize hydrothermal alteration detection
    if fe3_fe2_ratio > 0.8 and hydration_index > 0.6:
        return 'hydrothermal_altered'
    
    # Volcanic classification based on high silica content
    if silica_content > 0.7:
        return 'volcanic'
    
    # Default to sedimentary
    return 'sedimentary'


def classify_rock_batch(rock_samples):
    """
    Classify multiple rock samples in batch.
    
    Each sample should be a dict with keys:
    - fe3_fe2_ratio
    - hydration_index
    - silica_content
    
    Parameters:
    rock_samples (list): List of rock sample dictionaries
    
    Returns:
    list: List of classifications corresponding to each sample
    """
    results = []
    for sample in rock_samples:
        classification = classify_rock(
            sample['fe3_fe2_ratio'],
            sample['hydration_index'],
            sample['silica_content']
        )
        results.append({
            'sample': sample,
            'classification': classification
        })
    return results


def get_classification_summary(rock_samples):
    """
    Get a summary of classifications across a batch of rock samples.
    
    Parameters:
    rock_samples (list): List of rock sample dictionaries
    
    Returns:
    dict: Summary with counts of each classification type
    """
    results = classify_rock_batch(rock_samples)
    summary = {
        'volcanic': 0,
        'sedimentary': 0,
        'hydrothermal_altered': 0
    }
    for result in results:
        summary[result['classification']] += 1
    return summary


if __name__ == '__main__':
    # Example usage
    samples = [
        {'fe3_fe2_ratio': 0.9, 'hydration_index': 0.7, 'silica_content': 0.5},
        {'fe3_fe2_ratio': 0.5, 'hydration_index': 0.3, 'silica_content': 0.8},
        {'fe3_fe2_ratio': 0.4, 'hydration_index': 0.2, 'silica_content': 0.4},
    ]
    
    for sample in samples:
        result = classify_rock(sample['fe3_fe2_ratio'], sample['hydration_index'], sample['silica_content'])
        print(f"Sample (Fe3/Fe2={sample['fe3_fe2_ratio']}, H2O={sample['hydration_index']}, SiO2={sample['silica_content']}): {result}")
