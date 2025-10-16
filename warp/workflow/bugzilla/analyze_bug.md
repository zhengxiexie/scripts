***

## Analyze Bugzilla Workflow (Enhanced)

### 1. Retrieve and Summarize Bug Information

**Input**:
- `{{bug_url}}` — Bugzilla bug URL

**Steps:**
1. **Collect the bug information:**
2. **Summarize the bug background:**
    - Extract and present:
        - Bug summary and description
        - Reproduction steps (if available)
        - Reported severity/priority
        - Current status and assignees
        - Key comments or discussions

3. **Output the bug summary for review:**
    - Present a clear, formatted summary (background, details, context).
    - Pause, allowing you time to read the summary before further steps.

***

### 2. Analyze Repository with Debug Logs (Optional)

**Input:**
- `{{log_location}}` — Local path or URL to running logs related to this bug

**Steps:**
1. **Parse and examine the downloaded logs:**

2. **Extract critical log evidence:**
    - Identify and extract the most critical log entries that directly relate to the bug
    - Focus on error messages, stack traces, warning signs, and anomalous behavior patterns
    - Preserve original timestamps and context for each critical log entry

3. **Correlate with bug information:**
    - Link observed log anomalies or errors with details in the bug summary.
    - If relevant, identify which module/file/commit is indicated by the logs.

4. **Formulate debugging hypotheses:**
    - List potential root causes or code paths
    - Suggest next steps for experiment or investigation

***

### 3. Output

**Structured output should include:**
- Bug summary (background, detail, reproduction steps, status)
- Key insights from log analysis (with code/repo correlation)
- **Critical log evidence** (most important log entries with timestamps and context as supporting evidence)
- Clear, actionable suggestions for the next debugging step

***