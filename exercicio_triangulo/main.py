def total_price(area: float) -> tuple[int, float]:
    quantity_tinta = area / 3
    quantity_latas = quantity_tinta // 18
    if quantity_tinta % 18 != 0:
        quantity_latas += 1
    total_price = quantity_latas * price_tinta
    return quantity_latas, total_price


# 1 l to 3m2

price_tinta = 80
qtity_latao = 18
