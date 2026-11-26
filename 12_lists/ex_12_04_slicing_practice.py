"""
Section 12: Lists - Practice Exercise 04
Topics: List & String Slicing
    1. Basic Slicing (start, stop, negative indices, shallow copy)
    2. Steps & Reversing Lists (step, ::-1, negative steps)
    3. Reversing & Slicing Strings
    4. Modifying Portions of Lists (slice assignment)

Run this file in your terminal to check your outputs:
    python 12_lists/ex_12_04_slicing_practice.py
"""

# ==============================================================================
# PART 1: Basic Slicing & Shallow Copy
# ==============================================================================
chat_history = ["msg_0", "msg_1", "msg_2", "msg_3", "msg_4", "msg_5"]

# TODO: 1. Slice the first 3 messages from chat_history (omit start index)
#          and store them in `first_three`.

# TODO: 2. Slice messages from index 2 up to (not including) index 5
#          and store them in `middle_slice`.

# TODO: 3. Slice the last 2 messages using a negative start index
#          and store them in `last_two`.

# TODO: 4. Create a shallow copy of the entire chat_history using [:]
#          and store it in `history_backup`.

# print("Part 1 - first_three:", first_three)
# print("Part 1 - last_two:", last_two)
# assert first_three == ["msg_0", "msg_1", "msg_2"]
# assert middle_slice == ["msg_2", "msg_3", "msg_4"]
# assert last_two == ["msg_4", "msg_5"]
# assert history_backup == chat_history
# assert history_backup is not chat_history


# ==============================================================================
# PART 2: Steps & Reversing Lists
# ==============================================================================
rag_chunks = [
    "chunk_0",
    "chunk_1",
    "chunk_2",
    "chunk_3",
    "chunk_4",
    "chunk_5",
    "chunk_6",
]

# TODO: 1. Slice every 2nd chunk starting from index 0 and store in `even_chunks`.

# TODO: 2. Slice every 2nd chunk starting from index 1 and store in `odd_chunks`.

# TODO: 3. Reverse the entire rag_chunks list using slicing ([::-1]) and store
#          it in `reversed_chunks`.

# TODO: 4. Slice from index 5 down to (not including) index 1 with a step of -2
#          and store the result in `reverse_stepped`.

# print("Part 2 - reversed_chunks:", reversed_chunks)
# print("Part 2 - reverse_stepped:", reverse_stepped)
# assert even_chunks == ["chunk_0", "chunk_2", "chunk_4", "chunk_6"]
# assert odd_chunks == ["chunk_1", "chunk_3", "chunk_5"]
# assert reversed_chunks == [
#     "chunk_6",
#     "chunk_5",
#     "chunk_4",
#     "chunk_3",
#     "chunk_2",
#     "chunk_1",
#     "chunk_0",
# ]
# assert reverse_stepped == ["chunk_5", "chunk_3"]
# assert rag_chunks == [
#     "chunk_0",
#     "chunk_1",
#     "chunk_2",
#     "chunk_3",
#     "chunk_4",
#     "chunk_5",
#     "chunk_6",
# ]


# ==============================================================================
# PART 3: Reversing & Slicing Strings
# ==============================================================================
policy_code = "REFUND-2026-VIP"

# TODO: 1. Slice "REFUND" from policy_code and store it in `policy_type`.

# TODO: 2. Slice "VIP" from policy_code using negative indexing and store in `tier_tag`.

# TODO: 3. Reverse the entire policy_code string using slicing and store in `reversed_code`.

# TODO: 4. Slice every 2nd character from policy_code and store in `every_second_char`.

# print("Part 3 - reversed_code:", reversed_code)
# print("Part 3 - every_second_char:", every_second_char)
# assert policy_type == "REFUND"
# assert tier_tag == "VIP"
# assert reversed_code == "PIV-6202-DNUFER"
# assert every_second_char == "RFN-06VP"


# ==============================================================================
# PART 4: Modifying Portions of Lists (Slice Assignment)
# ==============================================================================
triage_pipeline = ["greet", "auth", "old_faq", "old_search", "handoff"]

# TODO: 1. Replace the slice containing "old_faq" and "old_search" (indices 2:4)
#          in-place with ["rag_lookup", "policy_check"].

# TODO: 2. Insert "verify_order" at index 1 in-place using an empty slice
#          assignment (triage_pipeline[1:1] = ["verify_order"]).

# TODO: 3. Remove the last item ("handoff") in-place by assigning an empty list
#          to the slice [-1:].

# print("Part 4 - triage_pipeline:", triage_pipeline)
# assert triage_pipeline == [
#     "greet",
#     "verify_order",
#     "auth",
#     "rag_lookup",
#     "policy_check",
# ]
