from validate_rules import apply_rules


def test_section8_funds_mortgage_account():
    rules = [{"source": "1312-operating", "dest": "1312-mortgage", "type": "fixed", "amount": 2310.94, "trigger": "monthly"}]
    deposits = [{"account": "1312-operating", "amount": 970.00}, {"account": "1312-operating", "amount": 1340.94}]
    balances = apply_rules(deposits, rules)
    assert round(balances["1312-mortgage"], 2) == 2310.94
    assert round(balances["1312-operating"], 2) == 0.00


def test_percentage_split_profit_first():
    rules = [
        {"source": "main", "dest": "taxes", "type": "percent", "amount": 15, "trigger": "by_transaction"},
        {"source": "main", "dest": "profit", "type": "percent", "amount": 5, "trigger": "by_transaction"},
    ]
    deposits = [{"account": "main", "amount": 1000.00}]
    balances = apply_rules(deposits, rules)
    assert round(balances["taxes"], 2) == 150.00
    assert round(balances["profit"], 2) == 50.00
    assert round(balances["main"], 2) == 800.00
