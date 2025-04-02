!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <branch-name> <commit-message>"
    exit 1
fi

# Assign arguments to variables
BRANCH_NAME=$1
COMMIT_MESSAGE=$2

# Add all changes to staging
git add .

# Commit changes
git commit -m "$COMMIT_MESSAGE"

# Push changes to the specified branch
git push origin "$BRANCH_NAME"

# Success message
echo "Changes pushed to branch '$BRANCH_NAME' successfully."
