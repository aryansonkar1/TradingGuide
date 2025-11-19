# Git Deployment Guide

## Step-by-Step Instructions to Push Your Code to GitHub

### Prerequisites
- Git installed on your system
- GitHub account created
- GitHub repository created (empty or with README)

---

## Step 1: Initialize Git Repository

```bash
git init
```

## Step 2: Add All Files to Git

```bash
git add .
```

## Step 3: Create Your First Commit

```bash
git commit -m "Initial commit: Trading Guide Platform"
```

## Step 4: Add GitHub Remote Repository

**First, create a repository on GitHub:**
1. Go to [github.com](https://github.com)
2. Click the "+" icon → "New repository"
3. Name it (e.g., "Trading_app" or "trading-guide-platform")
4. Choose Public or Private
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

**Then connect your local repo to GitHub:**

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

Replace:
- `YOUR_USERNAME` with your GitHub username
- `YOUR_REPO_NAME` with your repository name

**Example:**
```bash
git remote add origin https://github.com/johnsmith/trading-app.git
```

## Step 5: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

You'll be prompted for your GitHub username and password (use a Personal Access Token, not your password).

---

## Alternative: Using GitHub Desktop

If you prefer a GUI:
1. Download [GitHub Desktop](https://desktop.github.com/)
2. Sign in with your GitHub account
3. File → Add Local Repository
4. Select your `Trading_app` folder
5. Click "Publish repository" button

---

## Troubleshooting

### If you get authentication errors:
1. Generate a Personal Access Token:
   - GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate new token (classic)
   - Select scopes: `repo` (full control)
   - Copy the token
2. Use the token as your password when pushing

### If you need to update remote URL:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### If you want to check your remote:
```bash
git remote -v
```

---

## After Pushing to GitHub

Once your code is on GitHub, you can deploy to Streamlit Cloud:
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file to: `Home.py`
6. Click "Deploy"

Your app will be live in minutes! 🚀

