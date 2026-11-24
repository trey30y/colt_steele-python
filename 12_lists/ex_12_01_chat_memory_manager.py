"""
Exercise 12-01: AI Agent / Chatbot — Chat Memory Manager
Topic: Lists (Section 12) + pytest

Scenario:
An AI customer support chatbot stores the conversation in a `messages` list.
Before sending the history to the LLM, your memory manager must:
- Undo the last message when requested (`.pop()`)
- Block unsafe messages and skip duplicates (`for` loop + `in`)
- Append valid new messages (`.append()`)
- Keep only the most recent N messages using slicing (`[-max_history:]`)
- Return the updated history and the latest message (`[-1]`)
"""


def manage_chat_history(
    messages: list[str],
    new_message: str | None = None,
    max_history: int = 4,
    undo_last: bool = False,
    blocked_words: list[str] | None = None,
) -> tuple[list[str], str | None]:
    """Update and trim the chatbot's `messages` list.

    Requirements:
    1. Start from a copy of `messages` (e.g., `history = messages[:]`) so the original list is not mutated.
    2. If `undo_last` is True and `history` is not empty, remove the last message using `.pop()`.
    3. If `new_message` is not None:
        - If `blocked_words` is provided, loop over `blocked_words` with `for` and check with `in` whether any blocked word appears inside`new_message`. If one is found, do NOT append `new_message`.
        - Also check with `in` whether `new_message` is already in `history`. If it is not blocked and not already in `history`, add it with `.append()`.
    4. Trim `history` to keep at most the last `max_history` messages using slicing (`[-max_history:]`). If `max_history <= 0`, set `history` to `[]`.
    5. Set `last_message` to `history[-1]` if `history` is not empty, else `None`
    6. Return `(history, last_message)`.
    """
    # TODO: Step 1 - Copy `messages` into `history`

    # TODO: Step 2 - If `undo_last` is True and `history` has items, use `.pop()`

    # TODO: Step 3 - If `new_message` is not None, check `blocked_words` using `for` + `in`,check duplicates using `in`, and `.append(new_message)` if allowed

    # TODO: Step 4 - Trim `history` to the last `max_history` items using slicing

    # TODO: Step 5 - Get `last_message` using `[-1]` (or `None` if `history` is empty)

    # TODO: Step 6 - Return `history, last_message` pass


# --- pytest Test Suite (do not modify below this line) ---


def test_append_new_message():
    history, last_msg = manage_chat_history(
        messages=["user: Hi", "bot: Hello!"],
        new_message="user: Where is my order?",
        max_history=4,
        undo_last=False,
        blocked_words=["password"],
    )
    assert history == [
        "user: Hi",
        "bot: Hello!",
        "user: Where is my order?",
    ]
    assert last_msg == "user: Where is my order?"


def test_trim_history_with_slicing():
    history, last_msg = manage_chat_history(
        messages=["m1", "m2", "m3", "m4", "m5"],
        new_message="m6",
        max_history=3,
        undo_last=False,
        blocked_words=None,
    )
    assert history == ["m4", "m5", "m6"]
    assert last_msg == "m6"


def test_undo_last_message_with_pop():
    history, last_msg = manage_chat_history(
        messages=["user: Hi", "bot: Hello!", "user: Typo"],
        new_message=None,
        max_history=4,
        undo_last=True,
        blocked_words=None,
    )
    assert history == ["user: Hi", "bot: Hello!"]
    assert last_msg == "bot: Hello!"


def test_empty_history_and_undo():
    history, last_msg = manage_chat_history(
        messages=[],
        new_message=None,
        max_history=4,
        undo_last=True,
        blocked_words=None,
    )
    assert history == []
    assert last_msg is None


def test_blocked_word_not_appended():
    history, last_msg = manage_chat_history(
        messages=["user: Hi"],
        new_message="user: My api_key is 12345",
        max_history=4,
        undo_last=False,
        blocked_words=["password", "api_key"],
    )
    assert history == ["user: Hi"]
    assert last_msg == "user: Hi"


def test_duplicate_message_not_appended():
    history, last_msg = manage_chat_history(
        messages=["user: Hi", "bot: Hello!"],
        new_message="user: Hi",
        max_history=4,
        undo_last=False,
        blocked_words=None,
    )
    assert history == ["user: Hi", "bot: Hello!"]
    assert last_msg == "bot: Hello!"
