#!/bin/bash

# Exit script on any error
set -e

# Step 1: Create branches
# Create and switch to 'feature-branch'
git checkout -b feature-branch

# Step 2: Make a commit on 'feature-branch'
echo "# Feature work" >> app.py
git add app.py
git commit -m "Add feature work to app.py"

# Step 3: Create another branch 'experimental-branch' from 'feature-branch'
git checkout -b experimental-branch

# Step 4: Make a commit on 'experimental-branch'
echo "# Experimental changes" >> app.py
git add app.py
git commit -m "Add experimental changes to app.py"

# Step 5: Go back to 'feature-branch' and make another commit
git checkout feature-branch
echo "# Additional feature" >> app.py
git add app.py
git commit -m "Add additional feature to app.py"

# Step 6: Go back to 'main' and make a commit to create divergence
git checkout main
echo "# Main branch changes" >> app.py
git add app.py
git commit -m "Add main branch changes to app.py"

# Step 7: Create additional branches for advanced merge strategies
git checkout -b branch1

echo "# Branch1 changes" >> app.py
git add app.py
git commit -m "Add branch1 changes to app.py"

# Create branch2 and make changes
git checkout -b branch2

echo "# Branch2 changes" >> app.py
git add app.py
git commit -m "Add branch2 changes to app.py"

# Create branch3 and make changes
git checkout -b branch3

echo "# Branch3 changes" >> app.py
git add app.py
git commit -m "Add branch3 changes to app.py"

# Step 8: Go back to 'main' branch
git checkout main

# Step 9: Summary of created branches and commits
echo "Setup complete! The following branches were created:"
git branch --list

echo "Run 'git log --graph --oneline --all' to see the commit tree."