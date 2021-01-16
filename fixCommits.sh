#!/bin/sh

#reference https://stackoverflow.com/questions/750172/how-to-change-the-author-and-committer-name-and-e-mail-of-multiple-commits-in-gi
# to fix the commit history in GitHub
# 1st step, run the following to recover in local.

git filter-branch --env-filter '
OLD_EMAIL="phys395@sandbox.phys.sfu.ca"
CORRECT_NAME="Takehiro"
CORRECT_EMAIL="narutonaruto717@gmail.com"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

# 2nd step: git push --force --tags origin HEAD:master