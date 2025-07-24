# Warehouse Management System (WMS) - MVP

This project is a Minimum Viable Product (MVP) for a Warehouse Management System that focuses on SKU mapping, sales data cleaning, visualization, and relational data handling using modern low-code/no-code platforms and AI tools.

## Tech Stack

* Python (GUI): Tkinter for SKU Mapping Interface
* Frontend: HTML, CSS, JavaScript
* Backend: Python (Flask-ready structure)
* Data Sources: XLSX and CSV files
* AI Tools: ChatGPT (OpenAI) for code assistance
* Relational DB Dashboard: Teable.io / Baserow\.io / NoCodeDB
* Visualization/Query Layer: Luminal AI / Text-to-SQL Tool

---

## Project Structure

```bash
warehouse-app/
├── backend/                   # Python scripts for data processing
│   ├── app.py                 # Main backend logic
│   ├── processor.py           # Handles data cleaning and SKU mapping
│   ├── requirements.txt       # Dependencies
│   └── uploads/               # Uploaded XLSX files
├── data/                      # Raw and cleaned Excel/CSV data
├── desktop/                   # SKU Mapper GUI using Tkinter
│   └── sku_mapper_gui.py
├── frontend/                  # Web app frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
├── *.csv, *.xlsx              # Sample input and output files
```

---

## Features

### Part 1: SKU Mapping & Data Cleaning

* GUI-based SKU to MSKU mapping (with combo product support)
* Auto-identification and validation
* Logs missing/unmapped SKUs
* Supports multiple input formats (Flipkart, Amazon, etc.)

### Part 2: Relational Dashboard

* Built using Teable.io / Baserow\.io
* Allows users to:

  * Track Orders, Returns, Products
  * View mapping results
  * Easily edit datasets (for non-tech users)

### Part 3: Web Integration

* Frontend drag-and-drop support for uploading sales data
* Auto-cleaning and merging triggered on upload
* Real-time metrics on frontend via embedded dashboard

### Part 4: AI Over Data

* Text-to-SQL interface using Luminal AI or equivalent
* Dynamic chart generation (e.g., Returns by Product, Stock Deficits)
* Ability to create new calculated columns via natural language

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Rashijain2709/warehouse-app.git

cd wms-project
```

### 2. Backend Setup (Python)

```bash
cd backend

pip install -r requirements.txt

python app.py
```

### 3. Launch SKU Mapper GUI

```bash
cd desktop

python sku_mapper_gui.py
```

### 4. Frontend (Static)

Open `frontend/index.html` in browser.

---

## AI Tools Used

* ChatGPT (OpenAI): Assisted in generating the Python GUI, data processing logic, and debugging suggestions.
* Luminal AI: Used for demonstrating text-to-SQL queries and visualizing data insights through charts.

---

