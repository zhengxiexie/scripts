## 1. CLI Tooling Standards
Use modern, efficient 21st-century CLI tools for routine operations.
Here are recommended **21st-century CLI tooling standards**. 
These tools provide modern, fast, and user-friendly alternatives to traditional Unix commands,
improving productivity and usability in the terminal.

| Traditional Command | Modern Alternative | Install Command (brew) | Key Features                                                 |
|---------------------|--------------------|------------------------|--------------------------------------------------------------|
| cat                 | **bat**            | brew install bat       | Syntax highlighting, line numbers, Git integration           |
| less, more          | **bat**            | brew install bat       | Modern pager with preview; use as a replacement              |
| grep                | **rg** (ripgrep)   | brew install ripgrep   | Fast recursive search, sensible defaults, ignores .gitignore |
| find                | **fd**             | brew install fd        | Intuitive syntax, color output, smart ignoring               |
| ls                  | **exa**            | brew install exa       | Tree view, colors, better file info                          |
| du                  | **dua**            | brew install dua-cli   | Interactive disk usage analyzer                              |
| htop, top           | **btop**           | brew install btop      | Modern resource monitor, mouse support, graphs               |
| ps                  | **procs**          | brew install procs     | Easy-to-read, colored process listing                        |
| curl/wget           | **httpie**         | brew install httpie    | Easier REST API interaction with JSON, colors                |
| sed/awk             | **sd**             | brew install sd        | Intuitive, fast find-and-replace                             |
| diff                | **delta**          | brew install git-delta | Syntax highlighting, side-by-side diffs                      |
| head/tail           | **hck**            | brew install hck       | Fast and flexible text viewing                               |
| tree                | **tre**            | brew install tre       | Fast directory tree with git integration                     |
| man                 | **tldr**           | brew install tldr      | Community-driven simple man pages                            |
| df                  | **duf**            | brew install duf       | Colorful, interactive disk usage info                        |
•	Always prefer the recommended tool.
•	If not installed, use brew, tdnf, apt, or yum.


## 2. Pager Behavior (gh & git) 
Use `gh config set pager cat`,  this avoids paginated output, ensuring compatibility with scriptable workflows. After the job is done, revert it.

## 3. GitHub & Pull Requests
When push to remote branch, always push PR branches to `zx`, NOT `origin`.

## 4. Bugzilla Automation

**Token Handling:**

- Get a token with:

```sh
curl -X POST "https://bugzilla-rest.lvn.broadcom.net/rest/v1/token" \
  -H "Content-Type: application/json" \
  -d '{"username": "xz037905", "password": "p#nx5G%Now4sgBzf$T8"}'
```
- **Reuse token until expiry**; otherwise, refresh.

**Bug Info Retrieval:**

```sh
curl -X GET "https://bugzilla-rest.lvn.broadcom.net/rest/v1/bug/<BUG_ID>" \
  -H "Authorization: Bearer <TOKEN>"
```

**Bug Comments:**

```sh
curl -X GET "https://bugzilla-rest.lvn.broadcom.net/rest/v1/bug/<BUG_ID>/getcomment" \
  -H "Authorization: Bearer <TOKEN>"
```
- **Automate token reuse/refresh in scripts to avoid manual steps.**

##  5. Confluence Page Automation

**Read (GET example):**

```sh
get token from env CONFLUENCE_TOKEN
curl -X GET \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Accept: application/json" \
  "https://vmw-confluence.broadcom.net/display/<SPACE>/<PAGE_TITLE>"
```

**Publish:**

```sh
/Users/zhengxie/Code/scripts/publish_confluence/publish-to-confluence <args>
```
- **Automate authentication where possible**.
- Convert Markdown to a Confluence-compatible format for publishing.

## 6. Build Log Analysis

**Standard usage:**

```sh
python /Users/zhengxie/Code/scripts/build_analyzer.py vc ob-24838820
```
- **Integrate with modern CLI tools as needed**.
- For log searching/parsing, use `rg`, `fd`, and `bat` for enhanced logs.
