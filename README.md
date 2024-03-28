# jupytext_github_actions
workflow to convert script files to notebooks for changes on main using github actions

Instead of calling jupytext manually, we can now create notebooks from scripts files using github actions.

Only changes in the script files will add a commit to the PR, at least in theory.

Jupytext with `--update` will not change the notebook, if the contents didn't change.
