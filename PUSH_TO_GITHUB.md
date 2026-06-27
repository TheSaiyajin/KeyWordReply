# Push to GitHub

1. Initialize Git:
   - `git init`
2. Add the files:
   - `git add .`
3. Commit:
   - `git commit -m "Initial keyword reply cog"`
4. Create a GitHub repository and connect it:
   - `git branch -M main`
   - `git remote add origin https://github.com/YourUsername/YourRepoName.git`
   - `git push -u origin main`

After pushing, install it in Red with:
- `[p]cog install https://github.com/YourUsername/YourRepoName`
- `[p]load keywordreply`
