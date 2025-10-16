## Code Architecture Rule

**Enforce the following hard metrics when writing, reviewing, or auditing code in warp:**

### 1. Code File Size Limits

- For **dynamic languages** (e.g., Python, JavaScript, TypeScript):  
  **Each code file should not exceed 79 lines.**
- For **static languages** (e.g., Java, Go, Rust):  
  **Each code file should not exceed 250 lines.**

### 2. Directory Structure

- **Limit the number of files in each folder to no more than 8.**  
  If more than eight files are needed, plan and split them into subfolders based on logical modules or features.

***

## Architectural Elegance

**Beyond hard metrics, always strive for elegant architectural design and constantly guard against “code smells” that erode quality:**

1. **Rigidity:** The system is hard to change; even minor updates cause cascading modifications.
2. **Redundancy:** Repeated logic/code in multiple places, making maintenance hard and causing inconsistency.
3. **Circular Dependency:** Two or more modules are tightly coupled, making decoupling, testing, and reuse difficult.
4. **Fragility:** Modifying one area of the code causes unexpected failures or bugs in unrelated components.
5. **Obscurity:** The code’s intent and structure are unclear, making it hard to read, understand, or maintain.
6. **Data Clump:** Multiple related data elements are always passed together, signaling they should be combined into an object.
7. **Needless Complexity:** Over-engineering—using overly complex solutions for simple problems.

***

## IMPORTANT

- **Strictly enforce all hard metrics and architectural guidelines for your own and others’ code.**
- **Whenever you identify any “code smells” that may compromise code quality, IMMEDIATELY ask the user if optimization or refactoring is needed and suggest reasonable improvements.**

***

This rule should be actively referenced for all code writing, review, and refactoring in the Warp workflow.