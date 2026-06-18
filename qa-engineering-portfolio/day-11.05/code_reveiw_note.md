Code Review Findings

Finding 1:
CreateBudgetRequest lacks validation annotations.

Risk:
Invalid budget names may be accepted.

Potential Tests:
- Empty name
- Spaces only
- Null name

----------------------------------

Finding 2:
EditBudgetRequest not annotated with @Valid.

Risk:
Updates may bypass validation.

Potential Tests:
- Empty update payload
- Invalid values

----------------------------------

Finding 3:
GetBudgets endpoint lacks pagination.

Risk:
Performance degradation at scale.

Potential Tests:
- Large dataset retrieval
- Response time analysis