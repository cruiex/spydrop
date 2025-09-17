# SPYDROP

**Ethical Cybersecurity Simulation via Game-Based Backdoor Deployment**

SPYDROP is a cybersecurity simulation project designed to demonstrate **client-server interactions** and **backdoor deployment mechanics** in a controlled, ethical environment.

---

## Files

* `server.py` — Server script
* `client.py` — Client script
* `requirements.txt` — Python dependencies

---

## Installation

```bash
git clone https://github.com/cruiex/spydrop.git
cd spydrop
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# .\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
```

If webcam capture is needed:

```bash
pip install opencv-python
```

---

## Usage

1. Start the server:

```bash
python3 server.py
```

2. Run the client in another terminal:

```bash
python3 client.py
```

3. In the server terminal, type `capture` to take a webcam screenshot (saved in `screenshots/`).

---

## Contributors

| Roll No. | Name           | Responsibility          |
| -------- | -------------- | ----------------------- |
| 22BCS059 | Laxmi          | PYTHON GAME             |
| 22BCS100 | Rohit          | BACKDOOR IMPLEMENTATION |
| 22BCS105 | Saahil Mishra  | SERVER SIDE             |
| 22BCS121 | Shriya Udupa K | CLIENT SIDE             |

---

## Disclaimer

This project is for **educational and ethical purposes only**. Any malicious use is strictly prohibited.
