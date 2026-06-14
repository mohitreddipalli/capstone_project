# 🔗 GitHub Repository Setup Guide

## Complete Guide to Setting Up GitHub and Deploying with Live Updates

---

## 📋 Table of Contents

1. [Create GitHub Repository](#create-repository)
2. [Configure Git Locally](#configure-git)
3. [First Commit and Push](#first-push)
4. [Connect to Render/Railway](#connect-hosting)
5. [Enable Auto-Deploy](#enable-auto-deploy)
6. [Workflow for Live Updates](#live-updates)
7. [Troubleshooting](#troubleshooting)

---

## 🔧 Create GitHub Repository {#create-repository}

### Step 1: Create Account (if needed)
- Go to https://github.com/
- Click **Sign up**
- Complete registration

### Step 2: Create New Repository
1. Click **"+"** in top-right corner
2. Select **"New repository"**
3. Fill in details:
   - **Repository name**: `ai-career-platform`
   - **Description**: AI-powered career development platform
   - **Visibility**: Public (for easy sharing)
   - Check: **Add a README file** (optional)
4. Click **"Create repository"**

### Step 3: Copy Repository URL
- You'll see something like:
  ```
  https://github.com/YOUR_USERNAME/ai-career-platform.git
  ```
- **Copy this URL** - you'll need it next

---

## ⚙️ Configure Git Locally {#configure-git}

### Step 1: Install Git (if not already installed)
- Download from https://git-scm.com/download/win
- Run installer and accept defaults

### Step 2: Configure Git User
Open PowerShell and run:
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Generate SSH Key (Recommended)
```powershell
# Generate SSH key
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Press Enter for all prompts (keep defaults)
```

### Step 4: Add SSH Key to GitHub
1. Copy your public key:
   ```powershell
   Get-Content $env:USERPROFILE\.ssh\id_rsa.pub | Set-Clipboard
   ```
2. Go to GitHub → Settings → SSH and GPG keys
3. Click **New SSH key**
4. Paste and click **Add SSH key**

---

## 📤 First Commit and Push {#first-push}

### Step 1: Navigate to Project
```powershell
cd "c:\Users\mohit\OneDrive\Desktop\New folder\ai-career-platform"
```

### Step 2: Initialize Git Repository
```powershell
# Only if not already a git repo
git init
```

### Step 3: Add All Files
```powershell
git add .
```

### Step 4: Create Initial Commit
```powershell
git commit -m "Initial commit: AI Career Platform - full implementation

- 11 user-facing pages
- 16 routes with AJAX endpoints
- Dark mode support
- Mobile responsive design
- Complete documentation"
```

### Step 5: Connect to GitHub
```powershell
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/ai-career-platform.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 6: Verify on GitHub
1. Go to your repository on GitHub
2. You should see all your files listed!

---

## 🌐 Connect to Render/Railway {#connect-hosting}

### For Render.com:

1. Go to https://render.com/
2. Click **Sign up** (connect with GitHub)
3. Authorize Render to access your GitHub repositories
4. Click **New +** → **Web Service**
5. Select **Connect a repository**
6. Find `ai-career-platform` in the list
7. Click **Connect**
8. Configure:
   - **Name**: `ai-career-platform`
   - **Runtime**: Python
   - **Start Command**: `gunicorn backend.run_demo:app`
   - **Free plan**: Selected
9. Click **Create Web Service**
10. Wait for deployment (2-5 minutes)
11. Once done, you'll get a live URL! 🎉

### For Railway.app:

1. Go to https://railway.app/
2. Click **Login with GitHub**
3. Authorize Railway
4. Click **New Project** → **Deploy from GitHub repo**
5. Select your `ai-career-platform` repository
6. Configure (Railway auto-detects):
   - Runtime: Python
   - Start Command: Auto-detected
7. Click **Deploy**
8. You'll get a public URL! 🎉

---

## ⚡ Enable Auto-Deploy {#enable-auto-deploy}

### Render.com Auto-Deploy (Default)
- ✅ Already enabled!
- When you push to GitHub, Render automatically redeploys

### Railway.app Auto-Deploy (Default)
- ✅ Already enabled!
- When you push to GitHub, Railway automatically redeploys

### PythonAnywhere Webhook Setup
1. Go to Settings → Webhooks in your GitHub repo
2. Add webhook with:
   - **Payload URL**: Your PythonAnywhere webhook URL
   - **Content type**: `application/json`
   - **Events**: Push events
3. Save webhook

---

## 🔄 Workflow for Live Updates {#live-updates}

Now that everything is set up, here's how to push updates live:

### Make Changes Locally

```powershell
# Edit any file(s)
# For example, edit a template:
code backend/app/templates/user/profile.html
```

### Test Locally

```powershell
# Run server to test changes
python backend/run_demo.py

# Visit http://localhost:5000 to verify
# Press Ctrl+C when done testing
```

### Commit Changes

```powershell
git add .
git commit -m "Update profile page with new features"
```

### Push to GitHub

```powershell
git push origin main
```

### Wait for Auto-Deploy

- **Render**: 2-5 minutes
- **Railway**: 1-3 minutes
- Your live site updates automatically! ✅

### Verify Live Changes

1. Go to your Render/Railway dashboard
2. Check deployment status
3. Click your live URL to see updates

---

## 📂 Project Structure on GitHub

Your repository will contain:

```
ai-career-platform/
├── .github/
│   └── workflows/
│       └── deploy.yml          (CI/CD pipeline)
├── backend/
│   ├── run_demo.py             (Main Flask app)
│   └── app/
│       └── templates/          (All 15 pages)
├── database/
│   └── schema.sql              (Database schema)
├── .gitignore                  (Files to ignore)
├── .env.example                (Environment template)
├── Procfile                    (For Heroku/Render)
├── render.yaml                 (Render config)
├── runtime.txt                 (Python version)
├── requirements.txt            (Dependencies)
├── DEPLOYMENT_GUIDE.md         (Deployment instructions)
├── GITHUB_SETUP.md             (This file)
└── ... (documentation)
```

---

## 🔑 Security Best Practices

### Never Commit Secrets!

**DO NOT commit**:
- `.env` (with real secrets)
- Database passwords
- API keys
- Private tokens

**DO create**:
- `.env.example` (without real values)
- `.env` (in .gitignore, local only)

### Example .env.example:
```
FLASK_ENV=production
SECRET_KEY=<generate-a-secret-key>
DEBUG=False
```

### Generate Secret Key:
```python
import secrets
print(secrets.token_hex(32))
```

---

## 🆘 Troubleshooting {#troubleshooting}

### Problem: "fatal: not a git repository"
**Solution**: Run `git init` in your project directory

### Problem: "Permission denied (publickey)"
**Solution**: Set up SSH key (see Configure Git section)

### Problem: "Updates not deploying automatically"
**Solution**: 
1. Check GitHub repository is connected
2. Go to hosting dashboard and check webhook status
3. Try manual redeploy from dashboard

### Problem: "Git push rejected"
**Solution**:
```powershell
# Pull latest changes
git pull origin main

# Then try pushing again
git push origin main
```

### Problem: "Can't access files from Windows path"
**Solution**:
```powershell
# Use PowerShell commands, not Windows paths
cd (Resolve-Path "c:\Users\mohit\OneDrive\Desktop\New folder\ai-career-platform")
```

---

## 📊 Git Commands Reference

```bash
# View status
git status

# Add files
git add .                  # All files
git add filename.txt       # Specific file

# Commit changes
git commit -m "Message"

# Push to GitHub
git push origin main

# Pull changes
git pull origin main

# View commit history
git log

# Create branch
git checkout -b branch-name

# Switch branch
git checkout main

# View branches
git branch

# Delete branch
git branch -d branch-name
```

---

## 🎯 Quick Start Checklist

- [ ] GitHub account created
- [ ] Repository created
- [ ] Git configured locally
- [ ] SSH key added to GitHub
- [ ] Initial commit and push done
- [ ] Connected to Render/Railway
- [ ] Deployment successful
- [ ] Live URL working
- [ ] Auto-deploy enabled
- [ ] Made and pushed a test change
- [ ] Live update worked

---

## 🚀 Next Steps

1. **Complete the checklist above**
2. **Make a test change** (e.g., update a page)
3. **Commit and push** to see auto-deploy in action
4. **Share your live URL** with others!

---

## 📞 Support Resources

- **Git Help**: https://git-scm.com/book/en/v2
- **GitHub Docs**: https://docs.github.com/
- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app/

---

**Your GitHub repository is now ready for deployment with live updates!** 🎉

When you push to GitHub, your live site updates automatically. You're all set!
