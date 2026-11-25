"""
Exercise 12-02: AI Customer Support — Simple Ticket Queue
Topic: Lists Basics (Section 12)

Scenario:
Your customer support bot manages a queue of incoming support tickets.
This module provides `process_ticket_queue` to update the queue and return
the updated queue, the cancelled ticket, and the next ticket to handle.
"""


def process_ticket_queue(
    queue: list[str],
    new_ticket: str,
    vip_ticket: str,
) -> tuple[list[str], str, str]:
    """Update the support ticket queue with a new ticket and a VIP ticket.

    Steps:
    1. Copy `queue` into `updated_queue` so the original list is not mutated.
    2. Append `new_ticket` to the end of `updated_queue`.
    3. Insert `vip_ticket` at index 0 (the front of the queue).
    4. Remove the last ticket with `.pop()` and save it in `cancelled_ticket`.
    5. Get the first ticket (`updated_queue[0]`) as `next_ticket`.
    6. Return `(updated_queue, cancelled_ticket, next_ticket)`.
    """
    # Ai o listă simplă (ca queue = ["ticket_101", "ticket_102"]) → folosești shallow copy (queue[:]).
    # Ai liste în liste sau dicționare în liste și le modifici în interior → folosești deep copy (copy.deepcopy(...)).
    updated_queue = queue[:]
    updated_queue.append(new_ticket)
    updated_queue.insert(0, vip_ticket)
    cancelled_ticket = updated_queue.pop()
    next_ticket = updated_queue[0]
    return updated_queue, cancelled_ticket, next_ticket
