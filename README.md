# AutoOrganizer

A Python script to automatically organize your Downloads folder by moving files into subfolders based on their extensions (PDFs, Images, Documents, Spreadsheets, etc).

---

## Description

This project was born from a personal need: at the end of the semester, I realized my Downloads folder was completely cluttered with hundreds of files. To make my workflow easier, I built this simple automation script.

### Features
	•	Automatically detects file extensions.
	•	Creates subfolders such as PDFs, Images, Spreadsheets, etc.
	•	Moves files into the appropriate subfolder.
	•	Skips hidden files and directories.
	•	Generates an execution log at Organized/records.log.
	•	Prints a final summary with statistics.

### Technologies Used
	•	Python 3.12+
	•	pathlib for path management
	•	shutil for file handling
	•	logging for execution records

### How to Use
	1.	Clone the repository:
        
        git clone https://github.com/Sara-Soares-de-Oliveira/AutoOrganizer.git
        
        cd AutoOrganizer
    
    2.	Edit the script (source = Path(...)) to point to your Downloads folder.
	
    3.	Run the script:
         python3 organizer.py

### Automation (optional)
	•	macOS/Linux: use cron to run the script automatically.
	•	Windows: use Task Scheduler to set up scheduled runs.

---

## Autor / Author

Sara Oliveira  
[LinkedIn](https://www.linkedin.com/in/sara-oliveira-055a35278/) • [Twitter](https://twitter.com/oliveira_dsc)

