# SPYDROP — Ethical Cybersecurity Simulation via Game-Based Backdoor Deployment

##  Overview
SPYDROP is a cybersecurity simulation project designed to demonstrate **client-server interactions** and **backdoor deployment mechanics** in a controlled, ethical environment.  
The repository contains the following core files:

- `client.py` — Client script  
- `server.py` — Server script  
- `requirements.txt` — Python dependencies  

A local virtual environment (`venv/`) can be created for dependency management (⚠️ should not be pushed to GitHub).

---

##  Installation

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
   > **Tip:** If the project uses webcam capture, ensure `opencv-python` is listed in `requirements.txt`. If not, install it:
   ```bash
   pip install opencv-python
   ```

---

##  Usage

1. **Start the server** (in one terminal)
   ```bash
   python3 server.py
   ```

2. **Run the client** (in another terminal)
   ```bash
   python3 client.py
   ```

 Once both scripts are running, the client will attempt to establish communication with the server.

---

##  Play the game — Capture Example

This project includes an interactive command you can type in the **server** terminal to trigger a webcam capture and save a screenshot.

**Steps**

1. Start the server:
   ```bash
   python3 server.py
   ```

2. With the server running, type the command:
   ```
   capture
   ```
   (and press Enter)

3. What happens:
   - The server will access your default webcam (make sure your OS allows camera access).
   - A single photo will be taken and saved into the project folder under `screenshots/` (created automatically if missing).
   - The saved file name will include a timestamp, for example: `screenshots/screenshot_2025-09-15_22-15-30.jpg`.

**Sample terminal interaction**
```
$ python3 server.py
Server listening on 0.0.0.0:9000
Type 'capture' to take a screenshot, 'exit' to stop.
> capture
[INFO] Opening webcam...
[INFO] Captured image and saved to screenshots/screenshot_2025-09-15_22-15-30.jpg
> 
```

**Notes & Troubleshooting**
- If you don't have a webcam, the capture command will raise an error or fail to open the camera. The server should print an error message like:
  ```
  [ERROR] Could not open webcam. No capture saved.
  ```
- On first use the OS may ask for camera permission — allow it.
- If the `screenshots/` folder isn't created automatically, create it manually:
  ```bash
  mkdir screenshots
  ```
- If capture fails due to missing dependency, install OpenCV:
  ```bash
  pip install opencv-python
  ```

---

##  Disclaimer
This project is built for **educational and ethical cybersecurity training purposes only**.  
The author does **not endorse or support any malicious use** of the provided code.
