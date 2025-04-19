# **CleanDesk 🖥️📂**

_Automated File Organizer for Your Downloads Folder_

## **📌 Why CleanDesk?**

Tired of a cluttered **Downloads** folder? **CleanDesk** automatically organizes your files into categorized subfolders and keeps your workspace clean.

## **✨ Features**

✅ **Modern GUI** – Set your preferences with a PyQt6-based interface.  
✅ **Real-time Monitoring** – Uses `watchdog` to track file changes.  
✅ **Auto-Sorting** – Moves PDFs, images, ZIPs, and more into proper folders.  
✅ **Custom Rules** – Define your own file categories in `config.json`.  
✅ **Space Management** – Automatically deletes old files after a threshold (optional).
✅ **Logging** – Tracks file movements and errors using **daily log rotation**.

## **🛠️ Installation**

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/your-username/CleanDesk.git
cd CleanDesk
```

### **2️⃣ Set Up a Virtual Environment (Recommended)**

```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4️⃣ Configure Your Preferences**

Edit `config.json` to set your target directory and sorting rules.

```json
{
  "target_directory": "/path/to/your/Downloads",
  "categories": {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Executables": [".exe", ".msi"]
  },
  "other_files": "Others",
  "to_delete_files": "To Delete",
  "days_to_consider": 30
}
```

## **🚀 Usage**

### **Run CleanDesk**

```sh
python main.py
```

A modern GUI window will open where you can:

- Choose the folder to monitor
- Set the cleanup threshold (in days)
- Start/Stop monitoring in one click

### **Stop Monitoring**

Use the Stop button in the GUI

## 📁 Log Files

CleanDesk creates log files with daily rotation inside the `logs/` folder:

```lua
logs/
  └── CleanDesk-log_dd-mm-yyyy.log
```

Useful for debugging and tracking activity.

## **📌 Future Enhancements**

- **Undo/Restore Option** – Keep a log of moved files with an option to restore them within a certain timeframe.
- **Scheduled Auto-Cleanup** – Allow users to schedule automatic cleanups at regular intervals (e.g., daily, weekly).
- **Unit Tests** – Ensure reliability with `pytest` or `unittest`.
- **User Notifications** – Send desktop notifications when files are moved, deleted, or need user review.

Made with ❤️ by KTomy
