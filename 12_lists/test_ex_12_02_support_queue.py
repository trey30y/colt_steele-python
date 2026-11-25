"""
Tests for Exercise 12-02: AI Customer Support — Simple Ticket Queue
Run with: pytest 12_lists/test_ex_12_02_support_queue.py
"""

from ex_12_02_support_queue import process_ticket_queue


def test_basic_ticket_queue():
    updated_queue, cancelled_ticket, next_ticket = process_ticket_queue(
        queue=["ticket_101", "ticket_102", "ticket_103"],
        new_ticket="ticket_104",
        vip_ticket="ticket_999",
    )
    assert updated_queue == ["ticket_999", "ticket_101", "ticket_102", "ticket_103"]
    assert cancelled_ticket == "ticket_104"
    assert next_ticket == "ticket_999"
    assert "ticket_102" in updated_queue
    assert len(updated_queue) == 4


def test_empty_initial_queue():
    updated_queue, cancelled_ticket, next_ticket = process_ticket_queue(
        queue=[],
        new_ticket="ticket_201",
        vip_ticket="ticket_888",
    )
    assert updated_queue == ["ticket_888"]
    assert cancelled_ticket == "ticket_201"
    assert next_ticket == "ticket_888"


def test_original_queue_not_mutated():
    original_queue = ["ticket_101", "ticket_102"]
    updated_queue, _, _ = process_ticket_queue(
        queue=original_queue,
        new_ticket="ticket_103",
        vip_ticket="ticket_999",
    )
    assert original_queue == ["ticket_101", "ticket_102"]
    assert updated_queue == ["ticket_999", "ticket_101", "ticket_102"]
