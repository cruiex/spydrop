# SPYDROP — Ethical Cybersecurity Simulation via Game-Based Backdoor Deployment

## 📌 Overview
SPYDROP is a cybersecurity simulation project designed to demonstrate **client-server interactions** and **backdoor deployment mechanics** in a controlled, ethical environment.  
The repository contains the following core files:

- `client.py` — Client script  
- `server.py` — Server script  
- `requirements.txt` — Python dependencies  

A local virtual environment (`venv/`) can be created for dependency management (⚠️ should not be pushed to GitHub).

---

## ⚙️ Installation

Follow these steps to set up SPYDROP on your system:

1. **Clone the repository**
   ```bash
   git clone https://github.com/cruiex/spydrop.git
   cd spydrop
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   - On **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. **Start the server** (in one terminal)
   ```bash
   python3 server.py
   ```

2. **Run the client** (in another terminal)
   ```bash
   python3 client.py
   ```

✅ Once both scripts are running, the client will attempt to establish communication with the server.

---

## 📂 Project Structure

```
spydrop/
│── client.py
│── server.py
│── requirements.txt
│── venv/        # (virtual environment - not to be pushed)
```

---

## 📝 Notes

- Do **not** commit the `venv/` folder.  
- Add a `.gitignore` file to exclude unnecessary files:
  ```
  venv/
  __pycache__/
  *.pyc
  .DS_Store
  ```
- This project is intended **solely for ethical learning and research** in cybersecurity.  

---

## ⚠️ Disclaimer
This project is built for **educational and ethical cybersecurity training purposes only**.  
The author does **not endorse or support any malicious use** of the provided code.
