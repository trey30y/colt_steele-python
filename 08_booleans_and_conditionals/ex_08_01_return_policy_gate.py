"""
Exercise 08-01: Customer Support Bot — Return Policy Gate
Topic: Booleans and if/elif/else Conditionals (Section 8)

Scenario:
You are building a deterministic policy guardrail for an AI customer support bot.
Before the bot promises a refund to a customer, your script must evaluate the
company's return policy rules using booleans, comparison operators, logical
operators (`and`, `or`, `not`), and `if`/`elif`/`else` statements.
"""

# Customer Return Request (Order #CS-4092)
days_since_delivery = 18
is_final_sale = False
has_receipt = True
item_category = "electronics"  # Possible values: "electronics", "apparel", "software"
is_opened = True

# Output variables to set in your if/elif/else block
return_status = ""  # Must be set to: "approved", "store_credit_only", or "denied"
denial_reason = ""  # Set a short reason if denied, otherwise leave as ""


# TODO: Write an if/elif/else chain to enforce the return policy rules in order:
# 1. If the customer does NOT have a receipt OR the item is final sale:
#    - Set return_status to "denied"
#    - Set denial_reason to "Missing receipt or final sale item"
# 2. Else if days_since_delivery is greater than 30:
#    - Set return_status to "denied"
#    - Set denial_reason to "Return window expired"
# 3. Else if item_category is "software" AND the item is opened:
#    - Set return_status to "denied"
#    - Set denial_reason to "Opened software cannot be returned"
# 4. Else if item_category is "electronics" AND the item is opened AND days_since_delivery is greater than 14:
#    - Set return_status to "store_credit_only"
#    - Set denial_reason to ""
# 5. Else (all other eligible returns):
#    - Set return_status to "approved"
#    - Set denial_reason to ""
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

# Verification tests (do not modify below this line)
assert return_status == "store_credit_only", (
    f"Expected 'store_credit_only', got '{return_status}'"
)
assert denial_reason == "", f"Expected empty denial_reason, got '{denial_reason}'"
print(f"Policy check passed! Status: {return_status}")
