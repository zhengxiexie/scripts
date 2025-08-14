***

## Analyze Bugzilla Workflow (Enhanced)

### 1. Retrieve and Summarize Bug Information

**Input**:
- `{{bug_url}}` — Bugzilla bug URL
- (Optional: `{{bug_id}}` for API requests)

**Steps:**
0. **Obtain the bug token:**
```sh
curl -X POST "https://bugzilla-rest.lvn.broadcom.net/rest/v1/token" \
  -H "Content-Type: application/json" \
  -d '{"username": "xz037905", "password": "p#nx5G%Now4sgBzf$T8"}'
{"issued_at": "2025-08-14T01:13:23.990473", "token_type": "Bearer", "expired_in": 604800, "accesstoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTUxMzQwMDMsInN1YiI6Inh6MDM3OTA1IiwiZXhwIjoxNzU1NzM4ODAzfQ.-fR8hqvTh-SiGvEcSZlTkS97HwTYy1IMWLQvLUSB9vY"}
```
1. **Obtain the bug information:**
    - Use the Bugzilla REST API to fetch bug details and comments.
    - Example API calls (using a valid token):
      ```sh
      curl -X GET "{{bug_url}}" -H "Authorization: Bearer <TOKEN>"
      curl -X GET "{{bug_url}}/getcomment" -H "Authorization: Bearer <TOKEN>"
      ```
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

### 2. Analyze Repository with Debug Logs

**Input:**
- `{{log_location}}` — Local path or URL to running logs related to this bug

**Steps:**
1. **Parse and examine the downloaded logs:**
    - Use modern CLI tools for processing:
        - Use `bat` for log viewing
        - Use `rg` for searching error patterns, stack traces, or bug-specific markers
        - Use `fd` to quickly locate log files or relevant code

2. **Correlate with bug information:**
    - Link observed log anomalies or errors with details in the bug summary.
    - If relevant, identify which module/file/commit is indicated by the logs.

3. **Formulate debugging hypotheses:**
    - List potential root causes or code paths
    - Suggest next steps for experiment or investigation

***

### 3. Interactive Loop

- **Pause after each major phase:**  
  Wait for user confirmation/input before proceeding to the next stage.  
  (E.g., `Let me first read it.`)

***

### 4. Output

**Structured output should include:**
- Bug summary (background, detail, reproduction steps, status)
- Key insights from log analysis (with code/repo correlation)
- Clear, actionable suggestions for the next debugging step

***

### 5. Automation and Best Practices

- **Re-use tokens:** Automate Bugzilla token renewal and reuse if possible.
- **Script toolchains:** Use 21st-century tools (`bat`, `rg`, `fd`) for rapid, clear, and colorized diagnostics.
- **Documentation:** If a root cause or workaround is found, propose updating Confluence or other engineering documentation.
- **User Prompt:** For repeated/related bugs, suggest searching previous analysis for similar signatures.

***

#### Sample Enhanced Flow (Warp-Style)

```
Analyze bugzilla workflow

1. Fetch and summarize Bugzilla entry at {{bug_url}}:
   - Extract summary, background, comments, metadata.
   - Present structured summary. Pause for user review.

2. Analyze repository using running log at {{log_location}}:
   - Parse logs with modern CLI tools (bat, rg, fd).
   - Correlate errors, stack traces, warnings with bug summary.
   - Identify relevant modules, code paths.
   - Output main findings and debugging suggestions.
   - Pause for user next steps.

3. Automate token re-use for Bugzilla and prefer modern CLI in all log/code operations.
```

***