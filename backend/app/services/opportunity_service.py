def score_opportunity(industry_impact: int, customer_importance: int, investment_scale: int, steel_demand: int, product_fit: int, timing: int) -> dict:
    components = {"industry_impact": industry_impact, "customer_importance": customer_importance, "investment_scale": investment_scale, "steel_demand": steel_demand, "product_fit": product_fit, "timing": timing}
    weights = {"industry_impact": .20, "customer_importance": .15, "investment_scale": .15, "steel_demand": .20, "product_fit": .20, "timing": .10}
    total = round(sum(components[k] * weights[k] for k in components), 2)
    return {**components, "total": total}


def opportunity_level(score: float) -> str:
    if score >= 90: return "STRATEGIC"
    if score >= 80: return "HIGH"
    if score >= 70: return "WATCH"
    return "INFORMATION"

