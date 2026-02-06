
This module generates fertilizer recommendations based on
soil parameters collected from Terrapod sensors.
"""

def recommend_npk(moisture, temperature, organic_carbon):
    """
    Inputs:
    - moisture (%)
    - temperature (°C)
    - organic_carbon (% estimated)

    Output:
    - Recommended N, P, K percentages
    """

    # Base recommendation (rule-based)
    N = 40
    P = 20
    K = 20

    # Adjust nitrogen based on organic carbon
    if organic_carbon < 0.5:
        N += 10
    elif organic_carbon > 1.0:
        N -= 5

    # Adjust potassium based on moisture
    if moisture < 30:
        K += 5

    # Temperature stress adjustment
    if temperature > 35:
        P += 5

    return {
        "Nitrogen": N,
        "Phosphorus": P,
        "Potassium": K
    }
