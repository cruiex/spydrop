# SPYDROP

**Ethical Cybersecurity Simulation via Game-Based Backdoor Deployment**

> SPYDROP is an educational cybersecurity simulation demonstrating client–server interactions and (controlled) backdoor mechanics in a safe, local environment. This repository is for learning and defensive training only — **not** for malicious use.

---

## Table of contents

* [Overview](#overview)
* [Warning & Ethics](#warning--ethics)
* [Files](#files)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Play the game — Capture Example](#play-the-game---capture-example)
* [Development notes](#development-notes)
* [Security & responsible disclosure](#security--responsible-disclosure)
* [Contributors](#contributors)
* [License](#license)

---

## Overview

SPYDROP is a local simulation that demonstrates how a client and server can communicate, and includes a (simulated) backdoor mechanism for educational demonstrations. The code intentionally runs locally and writes captured images to a `screenshots/` folder.

**Intended audience:** cybersecurity students, educators, and lab demonstrators.

---

## Warning & Ethics

This repository is intended **strictly** for learning and defensive purposes. Do **not** deploy these tools on machines you do not own or control. Unauthorized access, deploying backdoors, or capturing data without explicit informed consent is illegal and unethical.

By using this code you agree to only run it in controlled, consented environments (your local machine, virtual machines you own, or lab setups where participants have agreed).

---

## Files

* `server.py` — server-side script (listens for client connections and contains interactive commands).
* `client.py` — client-side script (connects to server and responds to commands).
* `requirements.txt` — Python dependencies.
* `screenshots/` — directory where captured images are stored (created at runtime).

---

## Requirements

* Python 3.8+
* Recommended to run inside a virtual environment.

If webcam capture is required, `opencv-python` should be present in `requirements.txt`.

---

## Installation

```bash
git clone https://github.com/cruiex/spydrop.git
cd spydrop

# create virtual env
python3 -m venv venv

# activate (Linux/macOS)
source venv/bin/activate

# Windows (PowerShell)
# .\venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt
```

If your `requirements.txt` does not include `opencv-python` and you plan to use the webcam feature:

```bash
pip install opencv-python
```

---

## Usage

1. Start the server (one terminal):

```bash
python3 server.py
```

2. Start the client (other terminal):

```bash
python3 client.py
```

The client will attempt to connect to the server. With both running, you can use server-side commands to interact with the client.

---

## Play the game — Capture Example

1. Run the server: `python3 server.py`
2. In the server terminal type:

```
capture
```

3. The server will attempt to access the default webcam (OS permission prompts may appear). A single photo will be saved into `screenshots/` (created automatically) with a timestamped filename, for example:

```
screenshots/screenshot_2025-09-15_22-15-30.jpg
```

---

## Development notes & suggestions

* Add a `.gitignore` to avoid committing the virtual environment and sensitive files:

```
venv/
__pycache__/
screenshots/
*.pyc
.env
```

* Consider parameterizing server host/port via CLI args or a small `config.json` so accidental exposure is minimized.
* Keep `screenshots/` out of the repository (add to `.gitignore`) as it will store potentially sensitive images.
* Add unit tests or simple integration tests for the client/server handshake.
* Consider adding a `--dry-run` or `--no-webcam` flag for demoing the flow without camera hardware.

---

## Security & responsible disclosure

* Do **not** run this code on public networks or machines you don't own.
* If you find a security issue with this project, please open an issue or contact the maintainers privately (do **not** post proof-of-concept exploits publicly). Include reproduction steps and environment details.

---

## Contributors

| Roll No. | Name           | Responsibility          |
| -------- | -------------- | ----------------------- |
| 22BCS059 | Laxmi          | PYTHON GAME             |
| 22BCS100 | Rohit          | BACKDOOR IMPLEMENTATION |
| 22BCS105 | Saahil Mishra  | SERVER SIDE             |
| 22BCS121 | Shriya Udupa K | CLIENT SIDE             |

---

## License

Add a license to clarify permissions. Example: MIT License.

---

## Contact / Acknowledgements

For questions or educational use requests, open an issue or reach out to the repository owner. Thank you for using SPYDROP responsibly.

