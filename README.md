# 🔧 EDOXX Tool

**EDOXX Tool** is a DIY ESP32-S3 based security-learning and multi-tool project inspired by devices like the Flipper Zero.

The goal of this project is to learn about **embedded systems, electronics, programming, networking and cybersecurity** while building the device from scratch.

""ON THE 5.10 IT IS ONLY A TEST IN TERMINAL**

> ⚠️ **Status:** Early Development

---

## 🧠 Features

Planned features include:

* 📺 IR Remote
* 📡 WiFi Scanner
* 🌐 Network Tools
* 🪪 RFID / NFC
* 📻 433 MHz RF
* 🔎 Recon Tools
* 🔧 Hardware Tests
* ⚙️ Device Settings
* 🧪 Security-Lab Tools

The project is still under development, so many features are currently only menu placeholders.

---

## 🛠️ Hardware

### Main Board

* **ESP32-S3-WROOM-1 N16R8**

  * WiFi
  * Bluetooth LE
  * 16 MB Flash
  * 8 MB PSRAM

### Display

* **1.69" TFT IPS**
* 240 × 280 resolution
* ST7789
* SPI interface

### Input

* 🕹️ KY-023 Joystick
* 🔘 4× Push Buttons

### IR

* **KY-005** 38 kHz IR Transmitter
* **KY-022** IR Receiver

### RFID / NFC

* **MFRC522 / RC522**
* MIFARE-compatible test tags

### 433 MHz

* 433 MHz transmitter
* 433 MHz receiver

### Audio

* **KY-006** Passive Buzzer

### Prototyping

* 400-pin Breadboard
* Dupont jumper wires:

  * Male ↔ Male
  * Male ↔ Female
  * Female ↔ Female

---

## 💻 Software

The project is being developed primarily with:

* **MicroPython**
* Python
* VS Code
* Git
* GitHub

The ESP32-S3 will eventually run the actual EDOXX Tool firmware.

---

## 📂 Project Structure

```text
ESP32/
│
├── Flipper.py
└── README.md
```

More files will be added as development continues.

---

## 🎮 Controls

The pl
