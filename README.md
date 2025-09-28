# 💰 Expense Management System with ML Insights

A full-stack expense management application that allows users to track, analyze, and manage their personal finances. It includes a Machine Learning (ML) component to provide predictive insights into spending behavior.

📍 [Live Demo](https://expense-management-brown.vercel.app)

---

## ✨ Features

- 📊 Add, edit, delete, and view expenses
- 📁 Filter expenses by category and date
- 📅 Monthly and yearly expense summaries
- 📈 Data visualization via graphs and charts
- 🧠 **ML Module** for predicting future expenses
- 💾 Import/export data as JSON or CSV
- 🔐 Secure backend with validations

---

## 🛠️ Tech Stack

| Layer       | Technology                      |
|------------|----------------------------------|
| Frontend   | React.js                         |
| Backend    | Node.js, Express.js              |
| ML Module  | Python, pandas, scikit-learn     |
| Database   | MongoDB, JSON-based persistence  |
| Charts     | Chart.js                         |
| Deployment | Vercel (Frontend), Node.js server (Backend) |

---

## 🗂️ Project Structure
|   .env
|   .gitignore
|   file-structure.txt
|   package-lock.json
|   package.json
|   
+---backend
|   \---src
|       |   server.js
|       |   
|       +---config
|       |       connectDb.js
|       |       
|       +---controllers
|       |       transactionController.js
|       |       userController.js
|       |       
|       +---models
|       |       transactionModel.js
|       |       userModel.js
|       |       
|       \---routes
|               transactionRoutes.js
|               userRoute.js
|               
+---frontend
|   \---client
+---ml
|   |   app.py  # flask app for backend 
|   |   requirements.txt
|   |   
|   +---data
|   |       transactions.csv  # dataset 
|   |       
|   +---models
|   |       expense_model.pkl  #ML model
|   |       
|   \---pipeline
|           category.py   # model execution file
|           
\---node_modules
    |   .package-lock.json
    |   
    +---.bin
    |       bcrypt
    |       bcrypt.cmd
    |       bcrypt.ps1
    |       conc
    |       conc.cmd
    |       conc.ps1
    |       concurrently
    |       concurrently.cmd
    |       concurrently.ps1
    |       loose-envify
    |       loose-envify.cmd
    |       loose-envify.ps1
    |       nodemon
    |       nodemon.cmd
    |       nodemon.ps1
    |       nodetouch
    |       nodetouch.cmd
    |       nodetouch.ps1
    |       semver
    |       semver.cmd
    |       semver.ps1
    |       tree-kill
    |       tree-kill.cmd
    |       tree-kill.ps1
    |       
    +---@mongodb-js
    |   \---saslprep
    |       |   LICENSE
    |       |   package.json
    |       |   readme.md
    |       |   
    |       \---dist
    |               .esm-wrapper.mjs
    |               browser.d.ts
    |               browser.d.ts.map
    |               browser.js
    |               browser.js.map
    |               code-points-data-browser.d.ts
    |               code-points-data-browser.d.ts.map
    |               code-points-data-browser.js
    |               code-points-data-browser.js.map
    |               code-points-data.d.ts
    |               code-points-data.d.ts.map
    |               code-points-data.js
    |               code-points-data.js.map
    |               code-points-src.d.ts
    |               code-points-src.d.ts.map
    |               code-points-src.js
    |               code-points-src.js.map
    |               generate-code-points.d.ts
    |               generate-code-points.d.ts.map
    |               generate-code-points.js
    |               generate-code-points.js.map
    |               index.d.ts
    |               index.d.ts.map
    |               index.js
    |               index.js.map
    |               memory-code-points.d.ts
    |               memory-code-points.d.ts.map
    |               memory-code-points.js
    |               memory-code-points.js.map
    |               node.d.ts
    |               node.d.ts.map
    |               node.js
    |               node.js.map
    |               util.d.ts
    |               util.d.ts.map
    |               util.js
    |               util.js.map
   
