# SKILL: generate-exercise

When the user tells you which Colt Steele section/chapter or Python topic they just studied:

1. **Map to the Official Chapter Folder:**
   Always place the exercise inside the matching folder from the Colt Steele curriculum (create the folder if it does not exist yet):
   - Section 6 -> `06_numbers_and_operators/`
   - Section 7 -> `07_variables_and_strings/`
   - Section 8 -> `08_booleans_and_conditionals/`
   - Section 10 -> `10_looping/`
   - Section 12 -> `12_lists/`
   - Section 13 -> `13_list_comprehensions/`
   - Section 14 / 15 -> `14_dictionaries/`
   - Section 17 -> `17_functions_part_1/`
   - Section 19 -> `19_functions_part_2/`
   - Section 21 -> `21_error_handling/`
   - Section 22 -> `22_modules/`
   - Section 23 -> `23_http_requests/`
   - Section 30 -> `30_file_io/`

2. **Auto-Increment Exercise File Name:**
   - Check the target chapter folder for existing `ex_<section_num>_*.py` files.
   - Count them and assign the next two-digit sequence number (`01`, `02`, `03`, etc.).
   - Format the filename strictly as: `ex_<section_num>_<next_num>_<short_topic>.py`
   - *Example:* If `08_booleans_and_conditionals/` is empty, create `ex_08_01_return_policy_gate.py`. If `ex_08_01_...py` already exists, create `ex_08_02_escalation_rules.py`.

3. **Generate the Exercise Scaffold ONLY:**
   - Populate the file ONLY with:
     - Starter variables using a realistic customer support bot, company policy enforcement, RAG lookup, or order triage scenario.
     - Clear `# TODO:` comments in English describing the exact logic the user must write in VS Code.
     - `assert` statements directly after each section (or at the bottom for single-topic exercises) so the user can test their code via `python <folder>/<filename>.py` without separate `test_*` files unless explicitly requested.
     - When the user asks for multiple lectures/sub-chapters at once, order the sections in **ascending numerical order**, using **one single starter list/structure per section**.
   - **Mandatory Rule:** In any test function (`test_*`) or multi-parameter function call, use keyword arguments (`key=value`) exclusively. Unlabeled positional arguments are prohibited.
   - NEVER write completed solutions unless the user explicitly types "SHOW SOLUTION".

4. **Stop & Hand Off:**
   - Tell the user the exact file path created and instruct them to open it in VS Code and complete the `# TODO` blocks.
