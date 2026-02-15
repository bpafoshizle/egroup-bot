---
description: Create branch, commit, push, and submit a PR with pipeline monitoring
---

# Submit PR

This workflow automates the process of creating a new branch, committing changes, pushing to origin, creating a pull request, and monitoring the CI pipeline.

## Steps

1. **Create and Switch to Branch**
   ```bash
   git checkout -b <branch-name>
   ```

2. **Stage and Commit Changes**
   ```bash
   git add .
   git commit -m "<commit-message>"
   ```

3. **Push to Origin**
   ```bash
   git push -u origin <branch-name>
   ```

4. **Create Pull Request**
   ```bash
   gh pr create --title "<pr-title>" --body "<pr-body>"
   ```

5. **Monitor Pipeline**
   Monitor the status of GitHub Actions checks for the PR.
   ```bash
   gh pr checks --watch
   ```
