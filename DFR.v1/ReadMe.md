# ⚙️ Report Automation System (V1)

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version 1.0">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Legacy-yellow?style=for-the-badge" alt="Status">
</p>

---

## 📄 Overview

This is the foundational version of the **Automated Reporting System**. It was designed to solve the manual overhead of daily data collection and processing. The system focuses on web scraping, local file management, and basic data consolidation into Excel.

---

## 🚀 Core Workflow (`hard.py`)

The original system follows a linear execution path to handle daily tasks:

1.  **🔍 Pre-check:** Checks for annual maintenance requirements using `actualizador_anual.py`.
2.  **🌐 Web Extraction:** Uses Selenium to log into portals and trigger report downloads.
3.  **📂 File Relocation:** Monitors the system's download folder and moves relevant files to the working directory.
4.  **📊 Data Processing:** * Converts raw files to `.xlsx`.
    * Filters specific rows and updates the master spreadsheet.
5.  **📧 Communication:** Sends the finalized report via SMTP and notifies status through Webex.
6.  **🧹 Clean-up:** Removes temporary files to keep the workspace tidy.

---

## 🧩 Module Breakdown

### 🌐 Automation & Scraping
* **`login.py`:** Handles automated authentication and UI interaction.
* **`reubicador.py`:** Logic for detecting and moving downloaded files based on naming patterns.

### 📉 Data Handling
* **`filler.py` & `conversor.py`:** The engine behind Excel manipulation. It identifies empty rows for data insertion and ensures correct file formats using `openpyxl`.

### 📂 File & System Management
* **`archivo_diario.py` & `eliminador.py`:** Manages the historical archive by creating dated copies and deleting obsolete logs.
* **`actualizador_anual.py`:** A specialized script to reset templates and archive data every January 1st.

### 🔔 Notifications
* **`correo.py` & `notification.py`:** Standard modules for email distribution and instant messaging alerts.

---

## 🛠️ System Requirements

| Requirement | Detail |
| :--- | :--- |
| **Language** | Python 3.x |
| **Libraries** | `selenium`, `openpyxl`, `requests`, `shutil` |
| **Driver** | ChromeDriver (must match local Chrome version) |

---

## ⚙️ Setup Note
In this version, credentials and configurations are managed directly within the scripts. For a more secure approach using environment variables, please refer to **Version 2**.

---

<p align="center">
  <b>Developed as a robust foundation for operational automation.</b>
</p>
Librerías: selenium, openpyxl, requests, shutil.
Navegador: Google Chrome y su respectivo WebDriver.
