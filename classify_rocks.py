"""Spectral classification of Martian rocks."""







def is_hydrothermally_altered(fe3_fe2_ratio, hydration_index):
    """Check if a rock shows signs of hydrothermal alteration.
    
    Hydrothermal alteration is indicated by elevated Fe3+/Fe2+
    ratio (>0.8) combined with high hydration index (>0.6),
    consistent with aqueous alteration processes observed by
    MER rovers at Meridiani Planum and Gusev crater.
    
    Args:
        fe3_fe2_ratio: Ratio of ferric to ferrous iron
        hydration_index: Measure of water-related spectral features
    
    Returns:
        bool: True if hydrothermal alteration is detected
    """
    return fe3_fe2_ratio > 0.8 and hydration_index > 0.6






def classify_rock(fe3_fe2_ratio, hydration_index, silica_content):
    """Classify a Martian rock based on spectral parameters.
    
    Args:
        fe3_fe2_ratio: Ratio of ferric to ferrous iron
        hydration_index: Measure of water-related spectral features
        silica_content: Silica content as a fraction (0-1)
    
    Returns:
        str: 'hydrothermal_altered', 'volcanic', or 'sedimentary'
    """
    if is_hydrothermally_altered(fe3_fe2_ratio, hydration_index):
        return 'hydrothermal_altered'
    elif silica_content > 0.7:
        return 'volcanic'
    else:
        return 'sedimentary'