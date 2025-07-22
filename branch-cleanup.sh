#!/bin/bash

# Exit script on any error
set -e

# Step 1: Ensure you are on the 'main' branch
git checkout main

# Step 2: Delete all branches except 'main'
for branch in $(git branch | grep -v "\*" | grep -v "main"); do
    git branch -D $branch
done

# Step 3: Confirm remaining branches
echo "Remaining branches:"
git branch