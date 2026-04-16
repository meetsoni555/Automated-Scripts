# 🎵 Terminal YouTube Music Downloader

An automated terminal-based script powered by Python and Selenium that searches YouTube for your keywords, captures the link, and downloads the MP3 via Y2Mate in a continuous loop without physical intervention.

---

## 📋 System Requirements

To run this project perfectly on your machine, you must meet the following baseline requirements:


| Requirement | Description |
| :--- | :--- |
| **OS** | Linux (Optimized specifically for Arch Linux) |
| **Browser** | Google Chrome installed via the AUR |
| **Python** | Python 3.10 or higher |


---

## 🛠️ Automated Setup & Installation

You can get the entire project ready to go by executing the bundled installer script. 

### 1. Clone the repository
Pull the code to your local machine:
```bash
git clone https://github.com
cd AutomatedScripts

```

### 2. Make the installer executable
Grant terminal permissions to run the script:

```bash
chmod +x install.sh
```

### 3. Run the installer
This script will automatically download Google Chrome via yay, build your isolated Python virtual environment, and install Selenium:

```bash
./install.sh
```

## 🎮 How to Use (Step-by-Step)
Once installed, you never need to manually manage Python environments. Simply use the generated launcher to start up the operation.

### Step 1: Fire up the script
Execute the run command directly from your terminal:

```bash
./run.sh

```

### Step 2: Input your music keyword
The terminal will pause and ask you what you want to download: <br>
You can put in any keywords related to the song you like. 
for example: 

```text
Enter the keywords for the music or type q to quit: tere sang yara
```

```text
bloody brazil phonk slowed reverb
```

```text
1 hour coding music
```

### Step 3: Let the bot do the heavy lifting
Chrome will pop up on your screen. You will see the terminal output map out the entire extraction sequence <br> automatically:

```text
Connecting to YouTube...
Searching...
Captured URL: https://youtu.be
Switching to Y2Mate...
URL pasted...
Processing URL... 
Downloading SONG: Tere Sang Yaara - Full Video | Rustom
Downloading...
Download completed or processed in 12 seconds
Verification successful! File is in your Downloads.
```

### Step 4: Download more or safely exit
Because the script operates on an infinite loop, the prompt will immediately reappear asking for your next song. When you are finished, just type q to terminate the browser and the script:

```text
========================================
Enter the keywords for the music or type q to quit: q
Exiting and cleaning up...
Browser closed. Task completed.

```

### 📁 Where files are saved
All generated MP3 files are securely dumped directly into your native system folder located at:

```bash
~/Downloads
```









