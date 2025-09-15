# SPYDROP — Game Based Backdoor Deployment for Ethical Cybersecurity Simulation

## Overview
This repository contains three main files:

- `client.py`
- `server.py`
- `requirements.txt`

A virtual environment folder `venv/` is also present (not recommended to push to GitHub).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<USERNAME>/<REPO>.git
   cd <REPO>
````

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   * On Linux/macOS:

     ```bash
     source venv/bin/activate
     ```
   * On Windows (PowerShell):

     ```powershell
     .\venv\Scripts\activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

* Run the server:

  ```bash
  python3 server.py
  ```

* Run the client:

  ```bash
  python3 client.py
  ```

---

## Notes

* Do not commit the `venv/` folder.
* Add a `.gitignore` file to exclude virtual environments and cache files:

  ```
  venv/
  __pycache__/
  *.pyc
  .DS_Store
  ```

```

Would you like me to also add a **License** section (e.g., MIT) at the bottom of the README?
```
