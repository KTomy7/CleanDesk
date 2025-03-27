# **CleanDesk 🖥️📂**  
_Automated File Organizer for Your Downloads Folder_

## **📌 Why CleanDesk?**  
Tired of a cluttered **Downloads** folder? **CleanDesk** automatically organizes your files into categorized subfolders and keeps your workspace clean.

## **✨ Features**  
✅ **Real-time Monitoring** – Uses `watchdog` to track file changes.  
✅ **Auto-Sorting** – Moves PDFs, images, ZIPs, and more into proper folders.  
✅ **Custom Rules** – Define your own file categories in `config.json`.  
✅ **Space Management** – Deletes old/unnecessary files (optional).  
✅ **Logging** – Tracks all file movements and errors for easy debugging.  

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
    "logging_level": "INFO",
    "categories": {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Archives": [".zip", ".tar", ".rar"],
        "Videos": [".mp4", ".mkv"],
        "Music": [".mp3", ".wav"]
    },
    "other_files": "Others"
}
```

## **🚀 Usage**  
### **Run CleanDesk**
```sh
python main.py
```
- **First**, it will sort existing files.  
- **Then**, it will keep monitoring and organizing new downloads automatically.

### **Stop Monitoring**  
To stop CleanDesk, press `CTRL + C` in the terminal.

## **📌 Future Enhancements**  
- 🖥 **GUI Interface** – Choose folders & rules visually.  
- 🔄 **Log Rotation** – Manage log file size automatically.  
- ✅ **Unit Tests** – Ensure reliability with `pytest` or `unittest`.  
