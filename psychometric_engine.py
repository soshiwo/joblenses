import statistics

def process_assessment(selected_options):
    """
    Transforms raw situational judgment choices into an analytical executive report.
    
    Args:
        selected_options (list of dict): List containing the selected options from 10 scenarios.
                                         Expected format: [{'s': [Int, Pas, Team, Res, Saf]}, ...]
                                         
    Returns:
        dict: A dictionary containing the computed metrics and the executive report string.
    """
    
    # Define benchmark vector mapping
    values_map = ["Integrity", "Passion", "Team", "Results", "Safety"]
    
    # Extract the scoring arrays
    try:
        scores = [opt['s'] for opt in selected_options]
    except KeyError:
        raise ValueError("Input dictionaries must contain an 's' key with the scoring array.")
        
    if len(scores) != 10:
        pass # The logic works for any length, but optimally designed for 10
        
    # Metric 1: Dimension Mastery
    # Transpose scores to group by dimension
    dimension_scores = list(zip(*scores))
    dimension_sums = [sum(dim) for dim in dimension_scores]
    mastery = dict(zip(values_map, dimension_sums))
    
    # Metric 2: Dimensional Variances & Dominant Trait Reliability
    # Calculate variance for each dimension across the scenarios
    dimension_variances_list = [statistics.pvariance(dim) for dim in dimension_scores]
    dimensional_variances = dict(zip(values_map, dimension_variances_list))
    
    # Identify dominant trait (highest score)
    dominant_trait = max(mastery, key=mastery.get)
    dominant_variance = dimensional_variances[dominant_trait]
    
    # Flag 'Low Profile Stability' if the dominant trait is highly inconsistent
    is_unstable = dominant_variance >= 5.0
    stability_flag = "Low Profile Stability" if is_unstable else "High Profile Stability"
    
    # Metric 3: Strategic Trade-offs
    # Identify specific conflicts (e.g., Results vs. Integrity/Safety)
    results_score = mastery["Results"]
    integrity_score = mastery["Integrity"]
    safety_score = mastery["Safety"]
    
    risk_insight = None
    if results_score > (integrity_score + 20) or results_score > (safety_score + 20):
        risk_insight = (
            f"Candidate prioritizes outcomes (Results: {results_score}) over "
            f"governance and risk management (Integrity: {integrity_score}, Safety: {safety_score})."
        )
    elif integrity_score > (results_score + 20) or safety_score > (results_score + 20):
        risk_insight = (
            f"Candidate heavily indexes on governance and risk aversion "
            f"(Integrity: {integrity_score}, Safety: {safety_score}) at the potential expense of "
            f"execution speed and business outcomes (Results: {results_score})."
        )
    else:
        risk_insight = "Candidate demonstrates a calibrated equilibrium between business outcomes and corporate governance."

    # Executive Report Generation
    # Sort values to find dominant traits
    sorted_mastery = sorted(mastery.items(), key=lambda item: item[1], reverse=True)
    top_value_1 = sorted_mastery[0]
    top_value_2 = sorted_mastery[1]
    
    # Paragraph 1: Overall behavioral style
    p1 = (
        f"The candidate demonstrates a persistent cognitive preference for {top_value_1[0]} "
        f"({top_value_1[1]}/100) and {top_value_2[0]} ({top_value_2[1]}/100). Dimension mastery "
        f"analysis indicates that these vectors act as the primary drivers in complex, high-stakes "
        f"situational judgment scenarios. Decision patterns suggest a behavioral style strongly "
        f"oriented towards these core competencies when navigating organizational friction."
    )
    
    # Paragraph 2: Strength and stability of the profile
    stability_desc = "highly context-dependent and fluid" if is_unstable else "consistent and predictable"
    p2 = (
        f"Reliability index calculations yield a classification of '{stability_flag}' for the candidate's "
        f"primary driver ({dominant_trait}). The statistical variance for this dominant trait across the "
        f"assessment lifecycle is {dominant_variance:.2f}, pointing to {stability_desc} decision-making "
        f"patterns. This distribution denotes the degree to which their core values fluctuate when "
        f"exposed to competing organizational pressures."
    )
    
    # Paragraph 3: Specific risks and cultural fit insights
    fit_evaluation = "concerning deviations from" if is_unstable and "prioritizes outcomes over" in risk_insight else "strong theoretical alignment with"
    p3 = (
        f"Strategic trade-off analysis reveals that the {risk_insight.lower()} "
        f"In the context of company operational environment, this psychometric profile suggests "
        f"{fit_evaluation} core health, safety, and ethical benchmarks. The quantitative data "
        f"recommends utilizing targeted behavioral interviewing to probe the candidate's "
        f"risk-tolerance thresholds and historical adherence to compliance frameworks under pressure."
    )
    
    executive_report = f"{p1}\n\n{p2}\n\n{p3}"
    
    return {
        "mastery_metrics": mastery,
        "dimensional_variances": dimensional_variances,
        "reliability_metrics": {
            "dominant_trait": dominant_trait,
            "dominant_variance": round(dominant_variance, 2),
            "stability_flag": stability_flag
        },
        "strategic_trade_offs": risk_insight,
        "executive_report": executive_report
    }