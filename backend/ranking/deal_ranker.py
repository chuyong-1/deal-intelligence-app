def score_deal(item):
    """
    Lower score = better deal
    """
    price = item.get("price", float("inf"))

    # Weights (can be tuned later or personalized)
    PRICE_WEIGHT = 1.0

    score = price * PRICE_WEIGHT

    explanation = {
        "price": price,
        "price_weight": PRICE_WEIGHT,
        "final_score": score
    }

    return score, explanation


def rank_deals(items):
    ranked_items = []

    for item in items:
        score, explanation = score_deal(item)
        item["score"] = score
        item["explanation"] = explanation
        ranked_items.append(item)

    ranked_items.sort(key=lambda x: x["score"])
    return ranked_items
