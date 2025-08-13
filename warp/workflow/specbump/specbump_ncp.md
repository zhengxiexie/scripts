***

## Specbump NCP Workflow (Enhanced)

### Objective
Bump NSX Operator version in the NSX UJO repository by synchronizing commits between repositories and creating a proper spec bump commit.

***

### Steps

#### 0. Create a New Branch from nsx-magnus-wcp

```sh
cd /Users/zhengxie/Code/nsx-ujo/
git checkout origin/nsx-magnus-wcp
git checkout -b topic/zhengxie/nsx-magnus-wcp/$(date +%Y%m%d)
```

#### 1. Get Current NSX Operator Version (clnA)

```sh
cd /Users/zhengxie/Code/nsx-ujo/
# Extract NSX_OPERATOR_CLN value from spec file
clnA=$(rg "NSX_OPERATOR_CLN.*=.*['\"]([a-f0-9]+)['\"]" support/gobuild/specs/nsx_ujo.py -o -r '$1')
echo "Current NSX Operator CLN: $clnA"
```

#### 2. Get Latest NSX Operator Commit (clnB)

```sh
cd /Users/zhengxie/Code/nsx-operator
git fetch origin
git checkout origin/main
clnB=$(git rev-parse HEAD)
echo "Latest NSX Operator CLN: $clnB"
```

#### 3. Generate Commit Message Diff

```sh
cd /Users/zhengxie/Code/nsx-operator
# Get commit messages between current and latest
commit_messages=$(git log --oneline $clnA..$clnB)
echo "Commits to include:"
echo "$commit_messages"
```

#### 4. Update Spec File and Create Commit

```sh
cd /Users/zhengxie/Code/nsx-ujo/
# Update NSX_OPERATOR_CLN in spec file
sd "NSX_OPERATOR_CLN.*=.*['\"][a-f0-9]+['\"]" "NSX_OPERATOR_CLN = '$clnB'" support/gobuild/specs/nsx_ujo.py

# Create commit with proper format
cat > /tmp/commit_message << EOF
Spec bump NSX Operator to include recent changes

$commit_messages
EOF

git add support/gobuild/specs/nsx_ujo.py
git commit -F /tmp/commit_message
rm /tmp/commit_message
```

#### 5. Submit for Review

```sh
cd /Users/zhengxie/Code/nsx-ujo/
git review nsx-magnus-wcp
```

***

### Enhanced Features & Best Practices

1. **Error Handling:**
    - Verify git operations succeed before proceeding
    - Check if branches exist and are up to date
    - Validate commit hashes are valid

2. **Automation Improvements:**
    - Use `date +%Y%m%d` for consistent branch naming
    - Use `rg` and `sd` for efficient text processing
    - Template commit messages for consistency

3. **Validation Steps:**
   ```sh
   # Verify the spec file was updated correctly
   rg "NSX_OPERATOR_CLN" support/gobuild/specs/nsx_ujo.py
   
   # Confirm we have commits to bump
   if [[ -z "$commit_messages" ]]; then
       echo "No new commits to bump - already up to date"
       exit 0
   fi
   ```

4. **Pre-flight Checks:**
   ```sh
   # Ensure clean working directory
   if ! git diff --quiet; then
       echo "Working directory not clean. Please commit or stash changes."
       exit 1
   fi
   ```