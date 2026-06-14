# 🚀 DEPLOYMENT GUIDE - Free Hosting with GitHub Integration

## ✨ Quick Deploy (5 Minutes)

This guide helps you deploy the AI Career Platform to **free hosting with GitHub integration for live updates**.

---

## 📋 FREE HOSTING OPTIONS

### ⭐ **Recommended: Render.com** (Best Option)
- ✅ Free tier available
- ✅ GitHub integration (auto-deploy on push)
- ✅ Python/Flask support
- ✅ Automatic SSL
- ✅ GitHub Actions compatible
- 🔗 https://render.com

### 🟢 **Railway.app**
- ✅ Free tier available
- ✅ GitHub integration
- ✅ Python support
- ✅ Easy deployment
- 🔗 https://railway.app

### 🔵 **PythonAnywhere**
- ✅ Free tier available
- ✅ Python-native hosting
- ✅ MySQL support
- ✅ GitHub integration
- 🔗 https://www.pythonanywhere.com

### 🟣 **Replit**
- ✅ Always free
- ✅ GitHub integration
- ✅ Python support
- ✅ Collaborative
- 🔗 https://replit.com

> **Note**: 000webhost and InfinityFree only support PHP, not Python. Use the above options instead.

---

## 🔧 OPTION 1: Deploy to Render.com (Recommended)

### Step 1: Create GitHub Repository

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: AI Career Platform"

# Create repository on GitHub at https://github.com/new
# Then connect local repo:
git remote add origin https://github.com/YOUR_USERNAME/ai-career-platform.git
git branch -M main
git push -u origin main
```

### Step 2: Update render.yaml

Edit `render.yaml` and replace:
```yaml
repo: https://github.com/YOUR_GITHUB_USERNAME/ai-career-platform.git
```

### Step 3: Deploy on Render

1. Go to https://render.com/
2. Click **"New +"** → **"Web Service"**
3. Select **"Deploy from a Git repository"**
4. Connect your GitHub account
5. Select your `ai-career-platform` repository
6. Render will auto-detect and configure based on `render.yaml`
7. Click **"Deploy Web Service"**

### Step 4: GitHub Integration for Auto-Deploy

Render automatically deploys when you push to GitHub:

```bash
# Make changes locally
# ... edit files ...

# Commit and push
git add .
git commit -m "Update features"
git push origin main

# Render will automatically deploy the changes!
```

---

## 🔧 OPTION 2: Deploy to Railway.app

### Step 1: Create GitHub Repository
(Same as Option 1, Step 1)

### Step 2: Deploy on Railway

1. Go to https://railway.app/
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Authorize GitHub and select your repository
4. Railway will auto-detect Python
5. Set environment variables (if needed):
   - `FLASK_ENV=production`
   - `DEBUG=false`
6. Click **"Deploy"**

### Step 3: GitHub Integration

Railway auto-deploys on every GitHub push. To enable:
1. Go to your Railway project
2. Settings → GitHub Integration
3. Enable "Auto Deploy"

---

## 🔧 OPTION 3: Deploy to PythonAnywhere

### Step 1: Create GitHub Repository
(Same as Option 1, Step 1)

### Step 2: Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com/
2. Sign up (free account)
3. Go to **Web** tab
4. Click **"Add a new web app"**

### Step 3: Configure Web App

1. Choose Python 3.11
2. Framework: Flask
3. Path: `/home/yourusername/ai-career-platform`

### Step 4: Set Up GitHub Auto-Deploy

In PythonAnywhere console:
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ai-career-platform.git

# Install dependencies
pip install -r requirements.txt

# Update WSGI configuration to point to backend.run_demo:app
```

For auto-deploy, set up a GitHub webhook:
1. Go to your GitHub repository
2. Settings → Webhooks → Add webhook
3. Payload URL: Your PythonAnywhere webhook URL
4. Content type: application/json

---

## 🔧 OPTION 4: Deploy to Replit

### Step 1: Go to Replit
1. Visit https://replit.com/
2. Click **"Create Repl"**
3. Select **"Import from GitHub"**
4. Paste your repository URL

### Step 2: Configure

Replit will create a `.replit` file. Update it:
```
run = "cd backend && python run_demo.py"
```

### Step 3: Deploy

Click **"Run"** to start your app. Replit generates a public URL automatically.

---

## 📝 PREPARE YOUR PROJECT FOR DEPLOYMENT

### 1. Update app.py for Production

The current `backend/run_demo.py` needs one change:

**Change this line:**
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

**To this:**
```python
if __name__ == '__main__':
    debug = os.getenv('DEBUG', 'False') == 'True'
    app.run(debug=debug, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```

### 2. Create runtime.txt (for Render/Heroku)
```
python-3.11.0
```

### 3. Update environment variables

Create `.env.example`:
```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=sqlite:///demo.db
```

---

## 🔗 GITHUB SETUP INSTRUCTIONS

### Create Repository

```bash
# In your project directory
cd "c:\Users\mohit\OneDrive\Desktop\New folder\ai-career-platform"

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AI Career Platform - full implementation"

# Go to GitHub.com and create new repository:
# Name: ai-career-platform
# Description: AI-powered career development platform

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/ai-career-platform.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Enable GitHub Actions (Optional CI/CD)

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to Render

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Render
        run: |
          curl https://api.render.com/deploy/YOUR_RENDER_DEPLOY_KEY?ref=main
```

---

## 🌐 ENVIRONMENT VARIABLES

Set these on your hosting platform:

```
FLASK_ENV=production
SECRET_KEY=generate-a-random-string
DEBUG=False
PORT=5000
DATABASE_URL=sqlite:///demo.db (for now, using demo)
FLASK_APP=backend.run_demo
```

---

## 📊 DEPLOYMENT CHECKLIST

- [ ] GitHub repository created
- [ ] `.gitignore` committed
- [ ] `requirements.txt` updated
- [ ] `Procfile` added
- [ ] `render.yaml` configured (if using Render)
- [ ] Environment variables set on hosting
- [ ] Application deployed successfully
- [ ] Live URL working
- [ ] All pages accessible
- [ ] Dark mode functioning
- [ ] AJAX search working

---

## 🧪 TEST AFTER DEPLOYMENT

Once deployed, test:

```
1. Register new account
2. Verify OTP
3. Login
4. Navigate to all pages
5. Test dark mode
6. Test AJAX search on job board
7. View analytics dashboard
8. Check responsive design on mobile
```

---

## 🔄 LIVE UPDATES WITH GITHUB INTEGRATION

Once deployed with GitHub integration:

```bash
# Make changes locally
nano backend/app/templates/user/profile.html

# Test locally
python backend/run_demo.py

# Commit and push
git add .
git commit -m "Update profile page styling"
git push origin main

# Wait 1-2 minutes...
# Your live site automatically updates! ✅
```

---

## 📈 SCALING OPTIONS

### Upgrade from Free Tier When Needed:

| Hosting | Free Tier | Paid Tier |
|---------|-----------|-----------|
| Render | 0.1 CPU, 512MB RAM | $7/mo (1 CPU, 1GB RAM) |
| Railway | $5 free credits | Pay as you go |
| PythonAnywhere | 100MB disk | $5-50/mo |
| Replit | Community | $7-50/mo |

---

## 🆘 TROUBLESHOOTING

### Port Issues
Most free hostings assign port automatically. Don't hardcode port 5000.

**Solution**: Use `int(os.getenv('PORT', 5000))`

### Database Issues
Free tier uses SQLite. Upgrade to PostgreSQL on paid tier.

### Memory Issues
Keep demo mode enabled (no database = less memory).

### Slow Deployment
First deployment can take 2-5 minutes. Subsequent deployments faster.

---

## 📞 NEXT STEPS

1. **Choose a platform** (Render recommended)
2. **Create GitHub repository**
3. **Deploy using platform's instructions**
4. **Share your live link!**

---

## 🎯 QUICK COMMANDS

```bash
# Create repo
git init && git add . && git commit -m "Initial commit"

# Connect to GitHub
git remote add origin https://github.com/USERNAME/repo.git

# Push changes
git push origin main

# Deploy via Render/Railway/etc (follow their UI)

# For live updates, just:
git push origin main
```

---

**Server**: Your free hosting URL
**Updated**: On every GitHub push
**Monitoring**: Check hosting dashboard for logs

**Ready to deploy? Choose Render and follow Step 1!** 🚀
