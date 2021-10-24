# Create Issue

This action creates the body of the issue message in html format.

# Inputs

* `github_actor`: **Required**. People to whom the issue will be assigned.  

* `github_hash_commit`: **Required**. The commit hash where we should revert.

# Outputs
* `body:`: The body of the issue in html format

# Usage

Usage Example:
```yaml
      - name: 'Get the body of the issue'
        id: issue_body
        uses: ./sisifo_actions/gh/issue/create-issue-revert-html-body
        with:
          github_actor: $GITHUB_ACTOR
          github_hash_commit: ${{ steps.get-commit-hash.outputs.HASH_COMMIT_NUM }}
```
