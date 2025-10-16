***

## Make a PR from Current Branch Workflow (Enhanced)

### Objective
Create a professional pull request from the current branch with automated diff analysis, professional PR description generation, and seamless GitHub integration.

***

### Steps

#### 0. Combine bug info as a bug info background(if applicable)
Analyze `{{bug_info}}` using workflow in warp as the bug background description to attach in PR.

#### 1. Pre-flight Configuration
- Ensure `gh` CLI is configured with proper pager settings[1]After the job is done, revert it.
- Authentication with GitHub via `gh auth login`[2]
- The current branch has committed changes ready for PR


#### 2. Analyze Current Branch and Generate Diff

```sh
# Get current branch name
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Get base branch (usually main or master)
base_branch=$(gh repo view --json defaultBranchRef --jq '.defaultBranchRef.name')

# Generate detailed diff summary
git diff --stat $base_branch..$current_branch > /tmp/diff_summary.txt
git log --oneline $base_branch..$current_branch > /tmp/commit_log.txt

echo "Current branch: $current_branch"
echo "Base branch: $base_branch"
echo "Changes summary:"
cat /tmp/diff_summary.txt
```

#### 3. Fetch PR Template and Draft Description

Beautify the pr_description with the template of ~/Code/scripts/warp/template/pr_template.md

#### 4. Push to Remote 'zx' Repository

```sh
# Push current branch to zx remote instead of origin
git push zx $current_branch

# Set upstream tracking if needed
git branch --set-upstream-to=zx/$current_branch $current_branch
```

#### 5. Create Pull Request with gh CLI

```sh
# Create PR with generated description and open in browser
gh pr create \
  --base $base_branch \
  --head $current_branch \
  --title "$(git log -1 --pretty=%s)" \
  --body-file /tmp/pr_description.txt \

```

#### 6. Post-Creation Verification

```sh
# Verify PR was created successfully
gh pr status

# Get PR URL for sharing
pr_url=$(gh pr view --json url --jq '.url')
echo "Pull Request created: $pr_url"

# Clean up temporary files
rm -f /tmp/diff_summary.txt /tmp/commit_log.txt /tmp/pr_template.txt /tmp/pr_description.txt
```

***

### Enhanced Features & Best Practices

1. **Automated Description Generation:**
    - Fetches PR template from reference repository[3]
    - Includes commit history and file changes automatically
    - Uses the structured checklist format for consistency

2. **Smart Branch Detection:**
    - Automatically detects base branch from repository settings[1]
    - Handles different default branch names (main/master)

3. **Modern CLI Integration:**
    - Uses `jq` for JSON parsing
    - Uses `rg` for efficient text searching when needed

4. **Remote Management:**
    - Ensures push goes to `zx` remote instead of `origin`[4]
    - Sets proper upstream tracking

5. **Browser Integration:**
    - Automatically opens PR in the default browser for final review[5]
    - Provides direct URL for sharing

***