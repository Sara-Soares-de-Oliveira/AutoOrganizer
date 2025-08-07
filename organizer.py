import shutil
from pathlib import Path


source = Path('/Users/saraoliveira/Downloads')


Categories = {
    "PDFs" : [".pdf"], 
    "Images" : [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif"],
    "Spreadsheet" : [".xlsx", ".xls", ".csv"],
    "Documents" : [".doc", ".docx", ".txt"],
    "Compressed" : [".zip", ".rar", ".7z"],
    "Others" : []
}



for files in Path.iterdir(source): 
    
    if files.is_file(): 
        type = files.suffix.lower()
        
        for category, extention in Categories.items(): 
            
            if type in extention:   
                file_category = category
                break
        else: 
            file_category = "Others"    
            
        directory = source/"Organized"/file_category

        destination = directory / files.name  

        if not directory.exists():
             directory.mkdir(parents=True)
        try:  
             shutil.move(files, destination)    
        except FileNotFoundError:
             print("File Not Found")    
