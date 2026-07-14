from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Campaign:
    name: str
    spend: float
    conversions: int
    cpa: float
    roas: float
    stability: float
    scale_capacity: float


def score(campaign: Campaign) -> float:
    volume_score = min(campaign.conversions / 50, 1)
    efficiency_score = min(campaign.roas / 4, 1)
    cpa_score = 1 / (1 + campaign.cpa / 100)
    return round((0.35 * efficiency_score + 0.25 * cpa_score + 0.2 * volume_score + 0.1 * campaign.stability + 0.1 * campaign.scale_capacity), 4)


def allocate(campaigns: list[Campaign], total_budget: float) -> list[dict[str, float | str]]:
    scored = [(campaign, max(score(campaign), 0.01)) for campaign in campaigns]
    total_score = sum(item_score for _, item_score in scored)
    recommendations = []
    for campaign, item_score in scored:
        recommended = total_budget * item_score / total_score
        recommendations.append(
            {
                "campaign": campaign.name,
                "current_spend": round(campaign.spend, 2),
                "recommended_budget": round(recommended, 2),
                "change_pct": round((recommended - campaign.spend) / campaign.spend, 4) if campaign.spend else 1.0,
                "score": item_score,
                "decision": decision_label(campaign, item_score),
            }
        )
    return sorted(recommendations, key=lambda row: row["score"], reverse=True)


def decision_label(campaign: Campaign, campaign_score: float) -> str:
    if campaign_score >= 0.7 and campaign.scale_capacity >= 0.6:
        return "prioritize"
    if campaign_score >= 0.45:
        return "observe"
    return "reduce"


def read_campaigns(path: str) -> list[Campaign]:
    with open(path, newline="", encoding="utf-8") as fh:
        return [
            Campaign(
                name=row["campaign"],
                spend=float(row["spend"]),
                conversions=int(row["conversions"]),
                cpa=float(row["cpa"]),
                roas=float(row["roas"]),
                stability=float(row["stability"]),
                scale_capacity=float(row["scale_capacity"]),
            )
            for row in csv.DictReader(fh)
        ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv")
    parser.add_argument("--budget", type=float, required=True)
    args = parser.parse_args()
    for row in allocate(read_campaigns(args.input_csv), args.budget):
        print(row)


if __name__ == "__main__":
    main()
