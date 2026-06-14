# UI/UX Wireframes - AI Career Development Platform

## Wireframe Design Philosophy
- Modern SaaS Design with clean, minimalist approach
- Bootstrap 5 responsive grid layout
- Dark mode support with CSS variables
- Mobile-first responsive design
- Consistent navigation and branding

---

## 1. HOME PAGE (Landing Page)

```
┌─────────────────────────────────────────────────────────────────┐
│ NAVBAR                                                    [LOGIN]│
│ 🚀 AI Career Platform        [Home][About][Features][Contact]  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│                    HERO SECTION (Full Width)                     │
│                                                                   │
│         Transform Your Career with AI Intelligence               │
│                                                                   │
│      Get personalized job recommendations, skill analysis,       │
│          and career growth roadmap powered by AI                 │
│                                                                   │
│                    [Get Started] [Learn More]                    │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                        FEATURES SECTION                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ 🤖 AI Resume │  │ 💼 Job Board │  │ 📚 Courses   │           │
│  │  Analysis    │  │  & Matching  │  │ & Learning   │           │
│  │              │  │              │  │              │           │
│  │ Extract      │  │ Smart        │  │ Upskill &    │           │
│  │ skills &     │  │ filters &    │  │ certificates │           │
│  │ insights     │  │ recommendations               │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ 📊 Analytics │  │ 🎯 Roadmap   │  │ 📈 Career    │           │
│  │  Dashboard   │  │ Generation   │  │ Growth Path  │           │
│  │              │  │              │  │              │           │
│  │ Track your   │  │ Personalized │  │ Monitor your │           │
│  │ progress     │  │ learning     │  │ progress     │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                       STATS SECTION                              │
│    10,000+ Users  │  5,000+ Jobs  │  500+ Courses  │  95% Match  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FOOTER | About | Privacy | Terms | Contact | Social Links       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. REGISTRATION PAGE

```
┌─────────────────────────────────────────────────────────────────┐
│ NAVBAR (Simplified)                                 [Login]      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      Create Your Account                         │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ First Name           │  Last Name                        │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │ Email Address                                           │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │ Username                                                │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │ Password                                                │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │ Confirm Password                                        │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │ ☐ I agree to Terms & Conditions and Privacy Policy     │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │              [Create Account]                           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                   │
│          Already have an account? [Login Here]                   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. LOGIN PAGE

```
┌─────────────────────────────────────────────────────────────────┐
│ NAVBAR (Simplified)                         [Register]          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      Welcome Back!                               │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Email or Username                                       │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │ Password                            [Forgot Password?]  │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │              [Sign In]                                  │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │          Or continue with: [Google] [LinkedIn]          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                   │
│        Don't have an account? [Create One]                       │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. OTP VERIFICATION PAGE

```
┌─────────────────────────────────────────────────────────────────┐
│ NAVBAR (Simplified)                                              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                  Verify Your Email                               │
│                                                                   │
│   We've sent a 6-digit code to user@example.com                  │
│                                                                   │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐          │
│  │      │ │      │ │      │ │      │ │      │ │      │          │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘          │
│                                                                   │
│                   [Verify & Continue]                            │
│                                                                   │
│        Didn't receive code? [Resend Code]                        │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. USER DASHBOARD

```
┌─────────────────────────────────────────────────────────────────┐
│ NAVBAR                                  [Profile] [Logout]       │
│ 🚀 AI Career Platform                                            │
└─────────────────────────────────────────────────────────────────┘

┌────────┬──────────────────────────────────────────────────────┐
│        │         Welcome Back, John Doe!                       │
│ SIDEBAR│                                                        │
│ [•]    ├──────────────────────────────────────────────────────┤
│        │  QUICK STATS                                          │
│ Home   │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ Jobs   │  │ Resume   │ │  Jobs    │ │ Courses  │ │ Learning │ │
│ Courses│  │ Score    │ │ Applied  │ │ Enrolled │ │ Progress │ │
│ Resume │  │  85%     │ │    5     │ │    3     │ │   45%    │ │
│ Profile│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
│ Help   │                                                        │
│        ├──────────────────────────────────────────────────────┤
│ [Dark] │  RECENT JOB RECOMMENDATIONS                           │
│ [Mode] │  ┌─────────────────────────────────────────────────┐ │
│        │  │ Senior React Developer  - 92% Match              │ │
│        │  │ [View] [Apply] [Save]                            │ │
│        │  ├─────────────────────────────────────────────────┤ │
│        │  │ Full Stack Engineer - 88% Match                 │ │
│        │  │ [View] [Apply] [Save]                            │ │
│        │  ├─────────────────────────────────────────────────┤ │
│        │  │ Tech Lead - 85% Match                            │ │
│        │  │ [View] [Apply] [Save]                            │ │
│        │  └─────────────────────────────────────────────────┘ │
│        │                                                        │
│        ├──────────────────────────────────────────────────────┤
│        │  RECOMMENDED COURSES FOR SKILL GAP                    │
│        │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐  │
│        │  │ Advanced TypeScript                │             │  │
│        │  │ [View] [Enroll]                  │             │  │
│        │  └──────────────┘ └──────────────┘ └──────────────┘  │
│        │                                                        │
└────────┴──────────────────────────────────────────────────────┘
```

---

## 6. JOB BOARD PAGE

```
┌────────┬────────────────────────────────────────────────────────┐
│        │ Jobs Portal                                  [Saved: 5] │
│ SIDEBAR│                                                         │
│        ├────────────────────────────────────────────────────────┤
│ FILTERS│  ┌──────────────────────────────────────────────────┐  │
│        │  │ Search Jobs...                    🔍             │  │
│        │  └──────────────────────────────────────────────────┘  │
│        │                                                         │
│ [×] Job Type          ├─────────────────────────────────────────┤
│ ☑ Full-time          │ RESULTS (Showing 1-10 of 500+)           │
│ ☐ Part-time          │ [Sort: Relevance ▼] [Grid/List]          │
│ ☐ Contract           │                                           │
│ ☐ Internship         │ ┌──────────────────────────────────────┐ │
│                      │ │ Senior React Developer               │ │
│ [×] Experience       │ │ Tech Solutions Inc. · New York, NY   │ │
│ ☑ Senior             │ │                                      │ │
│ ☐ Mid-Level          │ │ $120K - $160K · Full-time           │ │
│ ☐ Entry Level        │ │                                      │ │
│                      │ │ Skills: React, TypeScript, Node.js   │ │
│ [×] Salary Range     │ │ Match: 92% [View] [Save] [Apply]    │ │
│ ┌─────────────┐      │ └──────────────────────────────────────┘ │
│ │ $ 0    $ 200K│     │ ┌──────────────────────────────────────┐ │
│ │   │───────│ │     │ │ Full Stack Engineer                  │ │
│ └─────────────┘      │ │ StartupXYZ · San Francisco, CA       │ │
│                      │ │                                      │ │
│ [×] Location         │ │ $100K - $140K · Full-time           │ │
│ Search location      │ │                                      │ │
│ ☑ Remote             │ │ Skills: React, Node, MongoDB, AWS   │ │
│ ☑ On-site           │ │ Match: 88% [View] [Save] [Apply]    │ │
│ ☑ Hybrid             │ └──────────────────────────────────────┘ │
│                      │ ┌──────────────────────────────────────┐ │
│        [Clear Filters]                 │ Tech Lead                    │ │
│                      │ │ Big Corp · Multiple Cities          │ │
│                      │ │                                      │ │
│                      │ │ $150K - $200K · Full-time           │ │
│                      │ │                                      │ │
│                      │ │ Skills: Leadership, Architecture     │ │
│                      │ │ Match: 85% [View] [Save] [Apply]    │ │
│                      │ └──────────────────────────────────────┘ │
└────────┴────────────────────────────────────────────────────────┘
```

---

## 7. JOB DETAILS PAGE

```
┌────────┬────────────────────────────────────────────────────────┐
│        │                                           [Save] [Apply]│
│ SIDEBAR│  Senior React Developer                                │
│        │  Tech Solutions Inc. · New York, NY                    │
│        ├────────────────────────────────────────────────────────┤
│        │                                                         │
│        │  ★★★★★ (4.5) | Posted 2 days ago                      │
│        │  💼 Full-time | 💰 $120K-$160K | 🎓 Senior            │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │  ABOUT THE ROLE                                        │
│        │                                                         │
│        │  We're looking for an experienced React developer...   │
│        │  [2-3 paragraphs of job description]                   │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │  REQUIRED SKILLS                                       │
│        │  [React] [TypeScript] [Node.js] [AWS] [Docker]        │
│        │  Match with your skills: 92%                          │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │  REQUIREMENTS                                          │
│        │  • 5+ years of React experience                        │
│        │  • Strong TypeScript knowledge                         │
│        │  • AWS and Docker experience                           │
│        │  • Leadership and mentoring skills                     │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │  COMPANY                                               │
│        │  [Company Logo]                                        │
│        │  Tech Solutions Inc.                                   │
│        │  Awesome company description...                        │
│        │                                                         │
│        │              [Apply Now] [Message Company]             │
│        │                                                         │
└────────┴────────────────────────────────────────────────────────┘
```

---

## 8. COURSE PORTAL PAGE

```
┌────────┬────────────────────────────────────────────────────────┐
│ SIDEBAR│ Courses & Learning                                      │
│        ├────────────────────────────────────────────────────────┤
│ [•] Home        │ ┌──────────────────────────────────────────┐ │
│ [•] Courses     │ │ Filter Courses:                          │ │
│ [•] My Learning │ │ [All] [Beginner] [Intermediate]         │ │
│ [•] Certificates│ │ [Advanced]                               │ │
│        │        ├──────────────────────────────────────────┤ │
│        │        │ ┌──────────────────────────────────────┐ │ │
│        │        │ │ Advanced TypeScript                  │ │ │
│        │        │ │ ⏱ 20 hours | ⭐ 4.8 (250 reviews)     │ │ │
│        │        │ │ [Enroll] [View Details]             │ │ │
│        │        │ └──────────────────────────────────────┘ │ │
│        │        │ ┌──────────────────────────────────────┐ │ │
│        │        │ │ React Performance Optimization       │ │ │
│        │        │ │ ⏱ 15 hours | ⭐ 4.7 (180 reviews)     │ │ │
│        │        │ │ [Enroll] [View Details]             │ │ │
│        │        │ └──────────────────────────────────────┘ │ │
│        │        │ ┌──────────────────────────────────────┐ │ │
│        │        │ │ System Design Masterclass           │ │ │
│        │        │ │ ⏱ 30 hours | ⭐ 4.9 (320 reviews)     │ │ │
│        │        │ │ [Enroll] [View Details]             │ │ │
│        │        │ └──────────────────────────────────────┘ │ │
│        │        │ ┌──────────────────────────────────────┐ │ │
│        │        │ │ Node.js Best Practices              │ │ │
│        │        │ │ ⏱ 18 hours | ⭐ 4.6 (150 reviews)     │ │ │
│        │        │ │ [Enroll] [View Details]             │ │ │
│        │        │ └──────────────────────────────────────┘ │ │
│        │        │                                            │ │
│        │        │        [Load More Courses]                │ │
│        │        └──────────────────────────────────────────┘ │
│        │                                                        │
└────────┴────────────────────────────────────────────────────────┘
```

---

## 9. USER PROFILE PAGE

```
┌────────┬────────────────────────────────────────────────────────┐
│        │                              [Edit Profile] [Settings]│
│ SIDEBAR│  PROFILE OVERVIEW                                      │
│        │  ┌────────────────┐                                    │
│ Profile│  │                │  John Doe                          │
│ (active│  │   [Profile     │  john.doe@example.com              │
│ )      │  │    Picture]    │  Senior React Developer            │
│ Settings        │  │                │  📍 New York, NY · 🔗 LinkedIn   │
│ Security│  └────────────────┘                                    │
│ Billing │                                                        │
│        ├────────────────────────────────────────────────────────┤
│        │  ABOUT ME                                              │
│        │  [Edit]                                                │
│        │  Experienced full-stack developer with 5+ years...    │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │  SKILLS (9 total)                   [+ Add Skill]      │
│        │  ┌────────────┐ ┌────────────┐ ┌────────────┐          │
│        │  │ React      │ │ TypeScript │ │ Node.js    │          │
│        │  │ Advanced   │ │ Advanced   │ │ Advanced   │          │
│        │  └────────────┘ └────────────┘ └────────────┘          │
│        │  ┌────────────┐ ┌────────────┐ ┌────────────┐          │
│        │  │ AWS        │ │ Docker     │ │ MongoDB    │          │
│        │  │ Intermediate │ Intermediate │ Intermediate│          │
│        │  └────────────┘ └────────────┘ └────────────┘          │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │  EXPERIENCE                                            │
│        │  [Edit]                                                │
│        │  • Senior Developer at Tech Corp (2020 - Present)      │
│        │  • Developer at StartupXYZ (2018 - 2020)               │
│        │  • Junior Developer at OldCorp (2015 - 2018)           │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │  EDUCATION                                             │
│        │  B.S. Computer Science, State University (2015)        │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │  RESUME                                                │
│        │  [View Resume] [Download] [Upload New]                │
│        │                                                         │
└────────┴────────────────────────────────────────────────────────┘
```

---

## 10. ADMIN DASHBOARD

```
┌────────┬────────────────────────────────────────────────────────┐
│ SIDEBAR│ Admin Dashboard                                         │
│        ├────────────────────────────────────────────────────────┤
│ [👨‍💼]   │ ┌──────────────────────────────────────────────────┐ │
│ Users  │ │ KEY METRICS                                      │ │
│ [💼]   │ │ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────┐ │ │
│ Jobs   │ │ │ Total    │ │ Active   │ │ Job Apps │ │ Top  │ │ │
│ [📚]   │ │ │ Users    │ │ Jobs     │ │ This Mo. │ │ Skill│ │ │
│ Courses│ │ │ 10,234   │ │ 1,542    │ │ 4,521    │ │ React│ │ │
│ [📊]   │ │ └──────────┘ └──────────┘ └──────────┘ └──────┘ │ │
│ Reports│ └──────────────────────────────────────────────────┘ │
│ [⚙️]    │                                                        │
│ Settings    ├────────────────────────────────────────────────────┤
│        │ ANALYTICS CHARTS                                   │
│        │ ┌──────────────────────┐ ┌──────────────────────┐ │
│        │ │ User Growth (30 days)│ │ Job Applications     │ │
│        │ │                      │ │ by Status            │ │
│        │ │  [Line Chart]        │ │  [Pie Chart]         │ │
│        │ │                      │ │  Applied 45%         │ │
│        │ │                      │ │  Reviewed 30%        │ │
│        │ └──────────────────────┘ │  Accepted 20%        │ │
│        │                          │  Rejected 5%         │ │
│        │                          └──────────────────────┘ │
│        ├────────────────────────────────────────────────────┤
│        │ RECENT ACTIONS                                     │
│        │ • 2 new jobs posted by admins                      │
│        │ • 150 new user registrations                       │
│        │ • 5 course enrollments                             │
│        │ • 12 job applications reviewed                     │
│        │                                                     │
│        ├────────────────────────────────────────────────────┤
│        │ [Manage Users] [Manage Jobs] [Manage Courses]      │
│        │ [View Logs] [Export Report]                        │
│        │                                                     │
└────────┴────────────────────────────────────────────────────┘
```

---

## 11. ANALYTICS DASHBOARD (User)

```
┌────────┬────────────────────────────────────────────────────────┐
│ SIDEBAR│ Analytics & Insights                                    │
│        ├────────────────────────────────────────────────────────┤
│        │ YOUR CAREER METRICS                                    │
│        │ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐    │
│        │ │ Resume Score │ │ Job Match    │ │ Applications │    │
│        │ │   85/100     │ │ Avg: 89%     │ │ This Month: 5│    │
│        │ │              │ │              │ │              │    │
│        │ └──────────────┘ └──────────────┘ └──────────────┘    │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │ SKILLS DISTRIBUTION                                    │
│        │ ┌────────────────────────────────────────────────────┐ │
│        │ │ [Donut/Pie Chart]                                 │ │
│        │ │  Frontend: 35%                                    │ │
│        │ │  Backend: 40%                                     │ │
│        │ │  DevOps: 15%                                      │ │
│        │ │  Soft Skills: 10%                                 │ │
│        │ └────────────────────────────────────────────────────┘ │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │ JOB APPLICATION TIMELINE                               │
│        │ ┌────────────────────────────────────────────────────┐ │
│        │ │ [Line Chart - Applications Over Time]              │ │
│        │ │ Jan: 5 | Feb: 8 | Mar: 12 | Apr: 15 | May: 20   │ │
│        │ └────────────────────────────────────────────────────┘ │
│        │                                                         │
│        ├────────────────────────────────────────────────────────┤
│        │ LEARNING PROGRESS                                      │
│        │ Courses Enrolled: 3                                    │
│        │ • Advanced TypeScript ████████░░ 80% (Completed)       │
│        │ • React Performance  ██████░░░░ 60% (In Progress)      │
│        │ • System Design      ████░░░░░░ 40% (In Progress)      │
│        │ Certificates Earned: 2                                 │
│        │                                                         │
└────────┴────────────────────────────────────────────────────────┘
```

---

## 12. ADMIN USER MANAGEMENT PAGE

```
┌────────┬────────────────────────────────────────────────────────┐
│        │ Manage Users                    [+ New User] [Export]   │
│ SIDEBAR│                                                         │
│ (Admin)├────────────────────────────────────────────────────────┤
│        │ ┌──────────────────────────────────────────────────┐   │
│ [×] Users       │ │ Search: [_____] Role: [All ▼] Status: [All ▼] │ │
│ [×] Jobs        │ └──────────────────────────────────────────────┘   │
│ [×] Courses     │                                                        │
│ [×] Reports     │ ┌────┬──────────┬───────────┬────────┬───────────┐   │
│        │        │ │ ID │ Name     │ Email     │ Role   │ Status    │   │
│ Search │        ├────┼──────────┼───────────┼────────┼───────────┤   │
│        │        │ │ 1  │ John Doe │ john@...  │ User   │ Verified  │   │
│        │        │ │ 2  │ Jane S.  │ jane@...  │ User   │ Verified  │   │
│        │        │ │ 3  │ Admin1   │ admin@... │ Admin  │ Verified  │   │
│        │        │ │ 4  │ Bob M.   │ bob@...   │ User   │ Pending   │   │
│        │        │ │ 5  │ Alice W. │ alice@... │ User   │ Verified  │   │
│        │        ├────┼──────────┼───────────┼────────┼───────────┤   │
│        │        │ │ 6  │ Mike H.  │ mike@...  │ User   │ Verified  │   │
│        │        │ │ 7  │ Sarah J. │ sarah@... │ User   │ Verified  │   │
│        │        └────┴──────────┴───────────┴────────┴───────────┘   │
│        │                                                                │
│        │ [◄ Prev] [1] [2] [3] ... [Next ►]                           │
│        │                                                                │
│        │ Selected Users: 0  [Delete Selected] [Change Role]            │
│        │                                                                │
└────────┴────────────────────────────────────────────────────────────┘
```

---

## Responsive Design Considerations

### Desktop (1920px+)
- Full sidebar navigation (collapsible)
- Multi-column layouts
- Complete data tables
- Side-by-side charts

### Tablet (768px - 1024px)
- Sidebar collapses to hamburger menu
- Single column for some sections
- Simplified tables (fewer columns)
- Stacked charts

### Mobile (Below 768px)
- Full-screen sidebar (overlay)
- Single column layout
- Simplified forms
- Vertical charts
- Touch-friendly buttons (min 44px)
- Stack all elements vertically

---

## Color Scheme (Dark Mode Support)

**Light Mode:**
- Primary: #007AFF (Blue)
- Secondary: #5AC8FA (Light Blue)
- Success: #34C759 (Green)
- Warning: #FF9500 (Orange)
- Danger: #FF3B30 (Red)
- Background: #FFFFFF
- Text: #000000

**Dark Mode:**
- Primary: #0A84FF (Bright Blue)
- Secondary: #30B0C0 (Teal)
- Success: #30B0C0 (Green)
- Warning: #FF9500 (Orange)
- Danger: #FF453A (Red)
- Background: #1C1C1E
- Text: #FFFFFF

---

## Component Patterns

### Forms
- Clear labels with placeholders
- Inline validation messages
- Visual feedback on errors
- Loading states for submissions

### Tables
- Sortable columns
- Selectable rows
- Pagination controls
- Action buttons (view, edit, delete)

### Modals/Dialogs
- Centered, overlaid on page
- Focus trap
- ESC to close
- Clear action buttons (Primary, Secondary, Cancel)

### Cards/Sections
- Subtle borders or shadows
- Consistent padding
- Clear hierarchy
- Hover effects for interactivity

---

## Navigation Hierarchy

**Main Navigation:**
1. Logo/Brand (Link to home)
2. Primary Menu (Home, Jobs, Courses, Dashboard)
3. User Menu (Profile, Settings, Logout)

**Sidebar (When applicable):**
1. Primary sections
2. Active section indicator
3. Collapsible subsections
4. Logout at bottom

**Dark Mode Toggle:**
- Accessible from navbar or settings
- Persistent across sessions
