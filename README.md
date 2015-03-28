# medlyte
Source Code for the webapp of medlyte

## Setting Up

These commands assume you've cloned the repository and are inside the cloned folder

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install Django
```
## Development Guidelines

So the basic workflow for development should be:
* Create a new feature branch.
* Work on this feature branch.
* Add tests.
* Send a PR.
* Merged once reviewed.

## Writing Commit Messages.

The commit message has two parts: a title (first line) and the body. The two are separated by a blank line. The first line should start with either of the following keywords:
* [A] - Added some file(s)
* [D] - Deleted some file(s)
* [E] - Edited some existent file(s)

Needless to say if you're adding some files and editing some too, ship them in different commits.

There are only two formatting rules for commit messages:

* There should be a single line summary of 71 characters or less which allows the one-line form of the log to display the summary without wrapping. A common convention is to not end the summary with a period (full stop).
* Additional details can be given after the summary. Make sure to leave a blank line after the summary and to keep all lines to 78 characters or less so they can be easily be read in terminals which don't automatically wrap lines.


