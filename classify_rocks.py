"""
Mars Rock Spectral Classification Module

Classifies Martian rocks based on spectral parameters into volcanic,
sedimentary, or hydrothermally altered categories.
"""


def _is_hydrothermally_altered(fe3_fe2_ratio, hydration_index):
    """Determine if a rock sample shows signs of hydrothermal alteration.

    Hydrothermal alteration is indicated by elevated Fe3+/Fe2+ ratios
    (oxidation from hydrothermal fluids) combined with high hydration
    indices (presence of hydrated minerals such as sulfates, clays,
    and opaline silica formed through water-rock interaction).

    This detection is critical for identifying past aqueous environments
    on Mars, as hydrothermal systems are prime astrobiological targets.

    Args:
        fe3_fe2_ratio: Ratio of ferric to ferrous iron (Fe3+/Fe2+).
        hydration_index: Normalized hydration mineral abundance index.

    Returns:
        True if both thresholds are exceeded, indicating
        hydrothermal alteration.
    """
    return fe3_fe2_ratio > 0.8 and hydration_index > 0.6


def classify_rock(fe3_fe2_ratio, hydration_index, silica_content):
    """Classify a Martian rock based on spectral parameters.

    Args:
        fe3_fe2_ratio: Ratio of ferric to ferrous iron (Fe3+/Fe2+).
        hydration_index: Normalized hydration mineral abundance index.
        silica_content: Normalized silica (SiO2) content fraction.

    Returns:
        'hydrothermal_altered', 'volcanic', or 'sedimentary'.
    """
    if _is_hydrothermally_altered(fe3_fe2_ratio, hydration_index):
        return "hydrothermal_altered"
    elif silica_content > 0.7:
        return "volcanic"
    else:
        return "sedimentary"