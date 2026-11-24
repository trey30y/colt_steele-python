"""
Exercise 08-01 (v2): Customer Support Bot — Return Policy Gate with pytest
Topic: Booleans and if/elif/else Conditionals (Section 8) + pytest basics
"""


def check_return_policy(
    days_since_delivery: int,
    is_final_sale: bool,
    has_receipt: bool,
    item_category: str,
    is_opened: bool,
) -> tuple[str, str]:
    """Evaluate return eligibility and return (return_status, denial_reason)."""
    return_status = "denied"
    denial_reason = ""

    if not has_receipt:
        denial_reason = "Customer doesn't have a receipt"
    elif is_final_sale:
        denial_reason = "Item is in final sale"
    elif days_since_delivery > 30:
        denial_reason = "Return window expired"
    elif item_category == "software" and is_opened:
        denial_reason = "Opened software cannot be returned"
    elif item_category == "electronics" and is_opened and days_since_delivery > 14:
        return_status = "store_credit_only"
    else:
        return_status = "approved"

    return return_status, denial_reason


def test_missing_receipt():
    status, reason = check_return_policy(
        days_since_delivery=5,
        is_final_sale=False,
        has_receipt=False,
        item_category="apparel",
        is_opened=False,
    )
    assert status == "denied"
    assert reason == "Customer doesn't have a receipt"


def test_final_sale():
    status, reason = check_return_policy(
        days_since_delivery=5,
        is_final_sale=True,
        has_receipt=True,
        item_category="apparel",
        is_opened=False,
    )
    assert status == "denied"
    assert reason == "Item is in final sale"


def test_expired_return_window():
    status, reason = check_return_policy(
        days_since_delivery=31,
        is_final_sale=False,
        has_receipt=True,
        item_category="apparel",
        is_opened=False,
    )
    assert status == "denied"
    assert reason == "Return window expired"


def test_opened_software():
    status, reason = check_return_policy(
        days_since_delivery=10,
        is_final_sale=False,
        has_receipt=True,
        item_category="software",
        is_opened=True,
    )
    assert status == "denied"
    assert reason == "Opened software cannot be returned"


def test_opened_electronics_after_14_days():
    status, reason = check_return_policy(
        days_since_delivery=18,
        is_final_sale=False,
        has_receipt=True,
        item_category="electronics",
        is_opened=True,
    )
    assert status == "store_credit_only"
    assert reason == ""


def test_approved_unopened_electronics_after_14_days():
    status, reason = check_return_policy(
        days_since_delivery=18,
        is_final_sale=False,
        has_receipt=True,
        item_category="electronics",
        is_opened=False,
    )
    assert status == "approved"
    assert reason == ""


def test_approved_opened_electronics_within_14_days():
    status, reason = check_return_policy(
        days_since_delivery=14,
        is_final_sale=False,
        has_receipt=True,
        item_category="electronics",
        is_opened=True,
    )
    assert status == "approved"
    assert reason == ""
