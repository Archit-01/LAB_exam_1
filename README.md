# 🚀 Jenkins Automated Testing with Docker — SmartCalc-Services

This project demonstrates a **Dockerized CI/CD pipeline** using **Jenkins**, where automated tests run for both a **Python Flask app** and a **Node.js Express app** inside containers.

---

## 🧩 Project Overview

**Repository:** `Jenkins-auto-test`  
**Application:** `SmartCalc-Services` (Python + Node.js)  
**Automation Tool:** Jenkins  
**Containerization:** Docker & Docker Compose  
**Testing:** Pytest (Python) and Jest (Node.js)

---

## 🧱 Project Structure

Jenkins-auto-test
├── docker-compose.yml
├── Jenkinsfile
├── README.md
└── smartcalx-service
└── python_service
├── app.py
├── Dockerfile
├── requirements.txt
├── tests
│ └── test_calc.py
└── node_service
├── index.js
├── package.json
├── Dockerfile
└── tests
└── calc.test.js


---

## ⚙️ How It Works

1. **Developer merges code** → branch `dev`  
2. Jenkins **automatically triggers** a build  
3. Pipeline performs:
   - ✅ **Checkout** latest repo
   - 🧪 **Run Python tests** (`pytest`)
   - 🧩 **Run Node.js tests** (`npm test`)
   - 🐳 **Build & run containers** via Docker Compose
   - ✅ **Show test results** directly in Jenkins console
4. If all tests pass → Docker containers successfully launch

---

## 🧰 Technologies Used

| Component | Tool |
|------------|------|
| CI/CD | Jenkins |
| Containerization | Docker, Docker Compose |
| Backend 1 | Python (Flask) |
| Backend 2 | Node.js (Express) |
| Testing | Pytest, Jest, Supertest |

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Archit-01/Jenkins-auto-test.git
cd Jenkins-auto-test
