***

## Fix Unit Test Workflow (Enhanced)

### Objective
- Identify and fix unit test failures when running `make test`.
- Modify **only** `_test.go` files.
- Repeat the fix-and-test loop until all tests pass.

***

### Steps

1. **Run Unit Tests**

```sh
make test
```

- Observe the output, focusing on which tests fail.
- Collect failure messages, stack traces, and error details.

2. **Identify Failed Tests**

- Use output to locate specific test files and functions causing failure.
- Remember: Only `_test.go` files are allowed to be modified.

3. **Fix the Failures**

- Edit the corresponding `_test.go` file(s).
- Apply fixes such as:
    - Correcting test logic or assertions
    - Updating mocks or test fixtures
    - Fixing race conditions or timing issues
    - Adjusting expected values or setups

4. **Rerun Tests**

```sh
make test
```

- Verify if all tests pass.
- If failures remain, repeat from step 2.
- Continue the fix–test cycle until **all unit tests succeed**.

***

### Best Practices

- Use editor or IDE features for quick navigation to failing tests.
- Prefer writing clear, minimal, and deterministic fixes.
- Avoid changing non-test code files to maintain codebase integrity.
- Document any complex fixes for future maintenance.
- Use modern CLI tools (`rg`, `bat`) to browse test code and failures effectively.

***