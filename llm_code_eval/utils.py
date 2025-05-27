TASK_PROMPTS = {
    "code-gen": {
        "functional correctness": 
            {
                "reference-free":
"""\
You will be given the code snippet for a problem. 
Your task is to rate the code snippet only on one metric.
Please make sure you read and understand these instructions carefully.
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
Functional Correctness (0-4) - Execution-based quality of the code snippet combined with the problem. The correctness is measured by the all possible unit tests, and the comparison of the reference code. The combination of the code snippet and the problem should pass all the possible tests based on your understanding of the reference code. The length of the code snippet can not determine the correctness. You need to assess the logics line by line.
- A score of 0  (failing all possible test) means that the code snippet is totally incorrect and meaningless.
- A score of 4  (passing all possible test) means that the code snippet is totally correct and can handle all cases.


Evaluation Steps:
1. Read the problem carefully and identify required functionalities of the implementation.
2. Read the code snippet and compare it to the problem. Check if the code snippet covers all required functionalities of the problem. 
3. Assign a score for functional correctness on a scale of 0 to 4, where 0 is the lowest and 4 is the highest based on the Evaluation Criteria.

Problem:

{{PROBLEM}}

Code Snippet:

{{OUTPUT}}

Evaluation Form:
Functional Correctness (scores ONLY):
""",
                "reference-enhanced":
"""\
You will be given the code snippet for a problem. 
Your task is to rate the code snippet only on one metric.
Please make sure you read and understand these instructions carefully.
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
Functional Correctness (0-4) - Execution-based quality of the code snippet combined with the problem. The correctness is measured by the all possible unit tests, and the comparison of the reference code. The combination of the code snippet and the problem should pass all the possible tests based on your understanding of the reference code. The length of the code snippet can not determine the correctness. You need to assess the logics line by line.
- A score of 0  (failing all possible test) means that the code snippet is totally incorrect and meaningless.
- A score of 4  (passing all possible test) means that the code snippet is totally correct and can handle all cases.


Evaluation Steps:
1. Read the problem carefully and identify required functionalities of the implementation.
2. Read the code snippet and compare it to the reference code. Check if the code snippet covers all required functionalities of the problem, and if it is as good as the reference code. 
3. Assign a score for functional correctness on a scale of 0 to 4, where 0 is the lowest and 4 is the highest based on the Evaluation Criteria.

Problem:

{{PROBLEM}}

Reference Code:

{{REFERENCE}}

Code Snippet:

{{OUTPUT}}

Evaluation Form:
Functional Correctness (scores ONLY):
"""
            },
        "usefulness":
            {
                "reference-free":
"""\
You will be given the code snippet for a problem.
Your task is to rate the code snippet only on one metric.
Please make sure you read and understand these instructions carefully.
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
Usefulness (0-4) Usefulness of the code snippet based on the problem description.

- A score of 0: Snippet is not at all helpful, it is irrelevant to the problem.
- A score of 1: Snippet is slightly helpful, it contains information relevant to the problem, but it is easier to write the solution from scratch.
- A score of 2: Snippet is somewhat helpful, it requires significant changes (compared to the size of the snippet), but is still useful.
- A score of 3: Snippet is helpful, but needs to be slightly changed to solve the problem.
- A score of 4: Snippet is very helpful, it solves the problem.

Evaluation Steps:
1. Read the problem carefully and identify required functionalities of the implementation.
2. Read the code snippet and compare it to the problem. Check if the code snippet covers all required functionalities of the problem, and if it presents them in a clear and logical order. 
3. Assign a score for usefulness on a scale of 0 to 4, where 0 is the lowest and 4 is the highest based on the Evaluation Criteria.

Problem:

{{PROBLEM}}

Code Snippet:

{{OUTPUT}}

Evaluation Form:
Usefulness (scores ONLY):
""",
                "reference-enhanced":
"""\
You will be given the code snippet for a problem.
Your task is to rate the code snippet only on one metric.
Please make sure you read and understand these instructions carefully.
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
Usefulness (0-4) Usefulness of the code snippet based on the problem description and the comparison of reference code.

- A score of 0: Snippet is not at all helpful, it is irrelevant to the problem.
- A score of 1: Snippet is slightly helpful, it contains information relevant to the problem, but it is easier to write the solution from scratch.
- A score of 2: Snippet is somewhat helpful, it requires significant changes (compared to the size of the snippet), but is still useful.
- A score of 3: Snippet is helpful, but needs to be slightly changed to solve the problem.
- A score of 4: Snippet is very helpful, it solves the problem.

Evaluation Steps:
1. Read the problem carefully and identify required functionalities of the implementation.
2. Read the code snippet and compare it to the problem and reference code. Check if the code snippet covers all required functionalities of the problem, and if it presents them in a clear and logical order. 
3. Assign a score for usefulness on a scale of 0 to 4, where 0 is the lowest and 4 is the highest based on the Evaluation Criteria.

Problem:

{{PROBLEM}}

Reference Code:

{{REFERENCE}}

Code Snippet:

{{OUTPUT}}

Evaluation Form:
Usefulness (scores ONLY):
"""                  
            }
    },
"code-translation": {
        "functional correctness":
            {
                "reference-free":
"""\
You will be given the translated code snippet in JAX given the input source code in pytorch. 
Your task is to rate the code snippet only on one metric.
Please make sure you read and understand these instructions carefully.
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
Functional Correctness (0-4) - Execution-based quality of the translated code snippet behaved consistenly with the source code. The correctness is measured by the all possible unit tests, and the comparison of the reference code. The translated code snippet should pass all the possible tests with similar output to the source code snippet based on your understanding of the reference code. The length of the translated code snippet can not determine the correctness. You need to assess the logics line by line.
- A score of 0  (failing all possible test) means that the code snippet is totally incorrect and meaningless.
- A score of 4  (passing all possible test) means that the code snippet is totally correct and can handle all cases.


Evaluation Steps:
1. Read the problem carefully and identify required functionalities of the implementation.
2. Read the translated code snippet and compare it to the source code snippet. Check if the code snippet covers all required functionalities of the input source code. 
3. Assign a score for functional correctness on a scale of 0 to 4, where 0 is the lowest and 4 is the highest based on the Evaluation Criteria.

Input source code snippet:

{{SOURCE_CODE}}

Translated Code Snippet:

{{TRANSLATED_CODE}}

Evaluation Form:
Functional Correctness (scores ONLY):
""",
                "reference-enhanced":
"""\
You will be given the translated code snippet from a given source code. 
Your task is to rate the code snippet only on one metric.
Please make sure you read and understand these instructions carefully.
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
Functional Correctness (0-4) - Execution-based quality of the  translated code snippet compared to the source code snippet. The correctness is measured by the all possible unit tests, and the comparison of the reference code. The translated code snippet should pass all the possible tests and return similar output to the input source code, based on your understanding of the reference code. The length of the code snippet can not determine the correctness. You need to assess the logics line by line.
- A score of 0  (failing all possible test) means that the code snippet is totally incorrect and meaningless.
- A score of 4  (passing all possible test) means that the code snippet is totally correct and can handle all cases.


Evaluation Steps:
1. Read the input source code carefully and identify required functionalities of the implementation.
2. Read the translated code snippet and compare it to the reference code. Check if the translated code snippet covers all required functionalities of the problem, and if it is as good as the reference code. 
3. Assign a score for functional correctness on a scale of 0 to 4, where 0 is the lowest and 4 is the highest based on the Evaluation Criteria.

Source Code Snippet:

{{SOURCE_CODE}}

Reference Code:

{{REFERENCE}}

Translated Code Snippet:

{{TRANSLATED_CODE}}

Evaluation Form:
Functional Correctness (scores ONLY):
"""
            },
        "usefulness":
            {
                "reference-free":
"""\
You will be given the translated code snippet for an input source code snippet.
Your task is to rate the code snippet only on one metric.
Please make sure you read and understand these instructions carefully.
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
Usefulness (0-4) Usefulness of the translated code snippet based on the input source code snippet.

- A score of 0: Translated Code Snippet is not at all helpful, it is irrelevant to the problem.
- A score of 1: Translated Code Snippet is slightly helpful, it contains information relevant to the input source code, but it is easier to write the solution from scratch.
- A score of 2: Translated Code Snippet is somewhat helpful, it requires significant changes (compared to the size of the snippet), but is still useful.
- A score of 3: Translated Code Snippet is helpful, but needs to be slightly changed to be consistent with input source code snippet.
- A score of 4: Translated Code Snippet is very helpful, it solves the same tasks that input source code performed.

Evaluation Steps:
1. Read the input source code carefully and identify required functionalities of the implementation.
2. Read the translated code snippet and compare it to the source code snippet. Check if the translated code snippet covers all required functionalities of the source code snippet, and if it presents them in a clear and logical order. 
3. Assign a score for usefulness on a scale of 0 to 4, where 0 is the lowest and 4 is the highest based on the Evaluation Criteria.

Input Source Code Snippet:

{{SOURCE_CODE}}

Translated Code Snippet:

{{TRANSLATED_CODE}}

Evaluation Form:
Usefulness (scores ONLY):
""",
                "reference-enhanced":
"""\
You will be given the translated code snippet for an input source code snippet.
Your task is to rate the code snippet only on one metric.
Please make sure you read and understand these instructions carefully.
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
Usefulness (0-4) Usefulness of the code snippet based on the input source code snippet and the comparison of reference code.

- A score of 0: Translated code snippet is not at all helpful, it is irrelevant to the input source code.
- A score of 1: Translated code snippet is slightly helpful, it contains information relevant to the input source code, but it is easier to write the translated code from scratch.
- A score of 2: Translated code snippet is somewhat helpful, it requires significant changes (compared to the size of the translated code snippet), but is still useful.
- A score of 3: Translated code snippet is helpful, but needs to be slightly changed to be consistent with the input source code.
- A score of 4: Translated code snippet is very helpful, it reflects the work of input source code.

Evaluation Steps:
1. Read the input source code snippet carefully and identify required functionalities of the implementation.
2. Read the translated code snippet and compare it to the input source code and reference code snippet. Check if the code snippet covers all required functionalities of the input source code snippet, and if it presents them in a clear and logical order. 
3. Assign a score for usefulness on a scale of 0 to 4, where 0 is the lowest and 4 is the highest based on the Evaluation Criteria.

Input source code:

{{SOURCE_CODE}}

Reference Code:

{{REFERENCE_CODE}}

Translated Code Snippet:

{{TRANSLATED_CODE_SNIPPET}}

Evaluation Form:
Usefulness (scores ONLY):
"""
            }
    }
}