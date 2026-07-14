from __future__ import annotations

import csv
from itertools import product


MODIFIERS = ["Buy", "Purchase", "Sale Of", "Good", "Delicious"]
PRODUCTS = ["Candy", "Sweet", "Bubble Gum", "Pie", "Child Candy"]


def build_keywords(products: list[str], modifiers: list[str]) -> list[dict[str, str]]:
    rows = []
    for product_name, modifier in product(products, modifiers):
        for keyword in (f"{product_name} {modifier}", f"{modifier} {product_name}"):
            rows.append({"Campaign": "Buying Candy", "Ad Group": product_name, "Keyword": keyword, "Criterion Type": "Exact"})
            rows.append({"Campaign": "Buying Candy", "Ad Group": product_name, "Keyword": keyword, "Criterion Type": "Phrase"})
    return rows


if __name__ == "__main__":
    with open("keywords.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["Campaign", "Ad Group", "Keyword", "Criterion Type"])
        writer.writeheader()
        writer.writerows(build_keywords(PRODUCTS, MODIFIERS))
