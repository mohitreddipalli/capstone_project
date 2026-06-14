# 📋 DEPLOYMENT COMMAND REFERENCE

Quick copy-paste commands for deploying your AI Career Platform.

---

## ⚡ ONE-LINER SETUP (Copy & Run)

### Configure Git (First Time Only)
```powershell
git config --global user.name "Your Name"; git config --global user.email "your.email@example.com"
```

### Initialize Repository (One Time)
```powershell
cd "c:\Users\mohit\OneDrive\Desktop\New folder\ai-career-platform"; git init; git add .; git commit -m "Initial commit: AI Career Platform"
```

### Connect to GitHub (Replace YOUR_USERNAME)
```powershell
git remote add origin https://github.com/YOUR_USERNAME/ai-career-platform.git; git branch -M main; git push -u origin main
```

---

## 📦 Daily Deployment Workflow

### Step 1: Edit & Test Locally
```powershell
# Start the server
cd "c:\Users\mohit\OneDrive\Desktop\New folder\ai-career-platform"
.\venv\Scripts\Activate.ps1
python backend/run_demo.py

# Server runs at http://localhost:5000
# Test your changes
# Press Ctrl+C to stop
```

### Step 2: Commit Changes
```powershell
git add .
git commit -m "Describe your changes here"
```

### Step 3: Deploy to Live
```powershell
git push origin main

# Wait 1-5 minutes
# Your live site updates automatically!
```

---

## 🔧 Useful Commands

### Check Git Status
```powershell
git status
```

### See Commit History
```powershell
git log --oneline
```

### Undo Last Commit (if not pushed)
```powershell
git reset --soft HEAD~1
git reset HEAD .
```

### Pull Latest from GitHub
```powershell
git pull origin main
```

### View Changes Before Committing
```powershell
git diff
```

---

## 🚀 GitHub URL Format

Replace `YOUR_USERNAME` with your actual GitHub username:

```
https://github.com/YOUR_USERNAME/ai-career-platform
https://github.com/YOUR_USERNAME/ai-career-platform.git
```

---

## 🌐 Render URLs

After deploying to Render:

```
Dashboard:     https://dashboard.render.com
Your App:      https://ai-career-platform-RANDOM.onrender.com
Logs:          https://dashboard.render.com → Select Service → Logs
```

---

## 📱 Testing Endpoints

After deployment, test these URLs:

```
Home Page:          https://your-deployed-app.com/
Register:           https://your-deployed-app.com/auth/register
Login:              https://your-deployed-app.com/auth/login
Dashboard:          https://your-deployed-app.com/user/dashboard
Career Path:        https://your-deployed-app.com/user/career-path
Explore Jobs:       https://your-deployed-app.com/jobs/explore
Find Courses:       https://your-deployed-app.com/courses/explore
Analytics:          https://your-deployed-app.com/user/analytics
Settings:           https://your-deployed-app.com/user/settings

API Endpoints:
Jobs Search:        https://your-deployed-app.com/api/jobs/search?query=python
Courses Search:     https://your-deployed-app.com/api/courses/search?query=react
```

---

## 🔐 Environment Setup

### Create Local .env File
```powershell
# Copy template
cp .env.example .env

# Edit .env with your values
code .env

# Important: .env is never committed (it's in .gitignore)
```

### For Deployment, Set in Platform Dashboard:
```
FLASK_ENV=production
DEBUG=false
SECRET_KEY=<generate-long-random-string>
```

---

## 🐛 Troubleshooting Commands

### Check if Python is Installed
```powershell
python --version
```

### Check if Git is Installed
```powershell
git --version
```

### Reinstall Dependencies
```powershell
pip install -r requirements.txt
```

### Clear Flask Cache
```powershell
# Remove __pycache__ directories
Remove-Item -Recurse __pycache__
Remove-Item -Recurse .pytest_cache
```

### Check Port is Free (if 5000 not working)
```powershell
# Set different port
$env:PORT=8000
python backend/run_demo.py
```

---

## 📊 Common Deployment Scenarios

### Scenario 1: First Time Deploy
```powershell
# 1. Create GitHub repo
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ai-career-platform.git
git branch -M main
git push -u origin main

# 2. Go to https://render.com
# 3. Sign up with GitHub
# 4. Create Web Service
# 5. Select repository
# 6. Deploy (auto-configured)
# 7. Wait 2-5 minutes
# 8. Access your live URL
```

### Scenario 2: Update Live Site
```powershell
# 1. Make changes locally
code backend/app/templates/user/profile.html

# 2. Test locally
python backend/run_demo.py
# Visit http://localhost:5000 to verify

# 3. Commit and push
git add .
git commit -m "Update profile UI"
git push origin main

# 4. Live site updates automatically in 1-5 minutes
```

### Scenario 3: Fix Error on Live Site
```powershell
# 1. Pull latest code
git pull origin main

# 2. Test locally
python backend/run_demo.py

# 3. Find and fix bug
code backend/run_demo.py

# 4. Test again locally

# 5. Commit fix
git add .
git commit -m "Fix: handle empty search results"
git push origin main

# 6. Platform auto-deploys
# 7. Visit your live URL to verify fix
```

---

## 🎯 Deployment Verification

### Check if Deployment Succeeded
1. Go to your Render dashboard
2. Look at the **Logs** tab
3. Should see: "Listening on http://0.0.0.0:PORT"
4. Visit your URL: `https://ai-career-platform-RANDOM.onrender.com`
5. Should load without errors

### Common Deployment Errors

**Error: `ModuleNotFoundError: No module named 'flask'`**
```powershell
# Fix: requirements.txt not deployed
# Solution: Ensure requirements.txt is in repo root
git add requirements.txt
git commit -m "Ensure requirements.txt is tracked"
git push origin main
```

**Error: `Port is already in use`**
```powershell
# Fix for local testing only
$env:PORT=8000
python backend/run_demo.py
```

**Error: `Template not found`**
```powershell
# Verify template directories exist
ls backend/app/templates/
# Should show: auth, user, jobs, courses, etc.
```

---

## 📋 Pre-Deployment Checklist

- [ ] All changes tested locally
- [ ] All files committed: `git status` (should be clean)
- [ ] `.env` file NOT committed (in .gitignore)
- [ ] `requirements.txt` up to date
- [ ] `Procfile` exists and correct
- [ ] `runtime.txt` specifies Python 3.11
- [ ] GitHub repository created
- [ ] All commits pushed: `git push origin main`
- [ ] Ready to deploy to Render/Railway

---

## 🚀 Quick Deploy Script

Save as `deploy.ps1`:

```powershell
#!/usr/bin/env pwsh

# Quick deploy script
Write-Host "🚀 Deploying to GitHub..." -ForegroundColor Green

# Check git status
if (git status --porcelain) {
    Write-Host "📝 Staging changes..."
    git add .
    
    $message = Read-Host "Commit message"
    git commit -m $message
}

Write-Host "📤 Pushing to GitHub..."
git push origin main

Write-Host "✅ Pushed to GitHub!"
Write-Host "⏳ Render will auto-deploy in 1-5 minutes..."
Write-Host "🌐 Check: https://dashboard.render.com/services"
```

**Run with**:
```powershell
.\deploy.ps1
```

---

## 📚 More Resources

**Git Cheat Sheet**: https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf

**GitHub CLI**: https://cli.github.com/ (optional, for advanced users)

**Render Deployment**: https://render.com/docs/deploy-flask

**Railway Deployment**: https://docs.railway.app/

---

## 💡 Pro Tips

### Tip 1: Use `.gitignore` Properly
```
# Never commit these:
.env
__pycache__/
*.pyc
.pytest_cache/
venv/
```

### Tip 2: Meaningful Commit Messages
```
Good:   git commit -m "Fix: handle null values in job search"
Bad:    git commit -m "update"
```

### Tip 3: Push Frequently
```
Don't wait until you have 100 commits
Push every logical change
Easier to revert if something breaks
```

### Tip 4: Check Logs When Deployment Fails
```
Render Dashboard → Logs → Scroll down
Shows exactly what went wrong
Copy error message into search engine
```

---

## 🎯 Success Indicators

After deploying, verify:
- [ ] App loads without errors
- [ ] All pages accessible
- [ ] AJAX search works
- [ ] Charts display
- [ ] Mobile view responsive
- [ ] Dark mode toggles
- [ ] Can make changes and see them live

---

## 🆘 Emergency Commands

### If Everything is Broken
```powershell
# Start over with latest from GitHub
git reset --hard origin/main
```

### If Deployment Stuck
```powershell
# Check logs
# Usually auto-fixes within 5 minutes
# If not: Re-push with a small change
git commit --allow-empty -m "Trigger redeploy"
git push origin main
```

### If Can't Push to GitHub
```powershell
# Update remote URL
git remote set-url origin https://github.com/YOUR_USERNAME/ai-career-platform.git
git push -u origin main
```

---

## 📞 Command Help

```powershell
# Get help for any git command
git --help <command>

# Examples:
git --help commit
git --help push
git --help branch
```

---

**Ready to deploy?** Just copy-paste the commands above! 🚀

**Questions?** Check [MASTER_DEPLOYMENT.md](MASTER_DEPLOYMENT.md) for detailed explanations.
