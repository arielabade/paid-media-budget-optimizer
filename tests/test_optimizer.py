from paid_media_budget_optimizer.optimizer import Campaign, allocate


def test_budget_is_conserved():
    campaigns = [
        Campaign("A", 100, 10, 10, 4, 0.9, 0.8),
        Campaign("B", 100, 2, 50, 1.2, 0.4, 0.2),
    ]
    rows = allocate(campaigns, 1000)
    assert round(sum(row["recommended_budget"] for row in rows), 2) == 1000
    assert rows[0]["campaign"] == "A"
