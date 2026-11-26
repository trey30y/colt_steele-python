"""
Section 12: Lists - Practice Exercise 03
Topics (in numerical order):
    11. List Methods: append, insert, and extend
    14. List Methods: clear, pop, and remove
    16. List Methods: index, count, sort, reverse, and join

Run this file in your terminal to check your print outputs:
    python 12_lists/ex_12_03_list_methods_practice.py
"""

# ==============================================================================
# PART 11: List Methods - append, insert, and extend
# ==============================================================================
support_queue = ["ticket_101", "ticket_102"]

# TODO: 1. Use .append() to add "ticket_103" to the end of support_queue.
support_queue.append("ticket_103")

# TODO: 2. Use .insert() to place "VIP_ticket_001" at index 0 of support_queue.
support_queue.insert(0, "VIP_ticket_001")

# TODO: 3. Use .extend() to add ["ticket_104", "ticket_105"] to support_queue
#          as individual items (not as a nested list).
support_queue.extend(["ticket_104", "ticket_105"])

print("Part 11 - support_queue:", support_queue)
assert support_queue == [
    "VIP_ticket_001",
    "ticket_101",
    "ticket_102",
    "ticket_103",
    "ticket_104",
    "ticket_105",
]


# ==============================================================================
# PART 14: List Methods - clear, pop, and remove
# ==============================================================================
active_alerts = [
    "timeout_error",
    "spam_flag",
    "policy_violation",
    "duplicate_msg",
    "low_confidence",
]

# TODO: 1. Use .remove() to delete "spam_flag" from active_alerts by value.
active_alerts.remove("spam_flag")

# TODO: 2. Use .pop() with an index to remove the first item (index 0) and
#          store it in a variable called `handled_alert`. Print `handled_alert`.
handled_alert = active_alerts.pop(0)

# TODO: 3. Use .pop() without any argument to remove the last item and store it
#          in a variable called `last_alert`. Print `last_alert`.
last_alert = active_alerts.pop()

# TODO: 4. Use .clear() to remove all remaining items from active_alerts.
active_alerts.clear()

print("Part 14 - active_alerts:", active_alerts)
assert handled_alert == "timeout_error"
assert last_alert == "low_confidence"
assert active_alerts == []


# ==============================================================================
# PART 16: List Methods - index, count, sort, reverse, and join
# ==============================================================================
intent_tags = ["refund", "billing", "refund", "shipping", "cancel", "refund"]

# TODO: 1. Use .count() to find how many times "refund" appears in intent_tags.
#          Store the result in `refund_count` and print it.
refund_count = intent_tags.count("refund")

# TODO: 2. Use .index() to find the position of "shipping" in intent_tags.
#          Store the result in `shipping_pos` and print it.
shipping_pos = intent_tags.index("shipping")

# TODO: 3. Use .sort() to sort intent_tags alphabetically in-place.
#          Print intent_tags after sorting.
intent_tags.sort()

# TODO: 4. Use .reverse() to reverse the order of intent_tags in-place.
#          Print intent_tags after reversing.
intent_tags.reverse()

# TODO: 5. Use .join() on " | " to combine all items in intent_tags into a
#          single string called `summary_line`. Print `summary_line`.
summary_line = " | ".join(intent_tags)

assert refund_count == 3
assert shipping_pos == 3
assert intent_tags == ["shipping", "refund", "refund", "refund", "cancel", "billing"]
assert summary_line == "shipping | refund | refund | refund | cancel | billing"
