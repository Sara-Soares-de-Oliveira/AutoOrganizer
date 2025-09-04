import shutil
from pathlib import Path
import logging
from collections import defaultdict

# configuration
source = Path('/Users/saraoliveira/Downloads')

log_path = Path(source,"Organized","records.log")
log_path.parent.mkdir(parents=True, exist_ok=True)

total_reads = 0
moved = 0
skipped = 0
errors = 0
renamed = 0
by_category = defaultdict(int)

logging.basicConfig(
    filename=log_path,
    encoding="utf-8",
    filemode="a",
    level=logging.INFO,
    format="{asctime} -- {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

logger = logging.getLogger(__name__)


Categories = {
    "PDFs" : [".pdf"], 
    "Images" : [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif"],
    "Spreadsheet" : [".xlsx", ".xls", ".csv"],
    "Documents" : [".doc", ".docx", ".txt"],
    "Compressed" : [".zip", ".rar", ".7z"],
    "Others" : []
}


# getting files 

for files in Path.iterdir(source): 
    
    if files.is_file(): 
        total_reads += 1
        suffix = files.suffix.lower()
        

        if files.name.startswith('.'): 
            skipped += 1
            logger.info(f"SKIPPED hidden: {files}")
            continue     
        
        for category_name, extension in Categories.items(): 
            
            if suffix in extension:   
                file_category = category_name
                break
        else: 
            file_category = "Others"    
            
        directory = Path(source,"Organized",file_category)

        destination = Path(directory, files.name)  

        if not directory.exists():
             directory.mkdir(parents=True)
        
        # moving files      
        try:  
             shutil.move(files, destination)
             moved += 1
             by_category [file_category] += 1
             logger.info (f"MOVED: {files.name} -> {directory}")     
        except FileNotFoundError:
             errors += 1
             logger.error(f"ERROR: Not found -> {files}")   
        except PermissionError: 
             errors += 1
             logger.error(f"ERROR: Permission -> {files}")  
    else: 
        skipped += 1
        logger.info(f"SKIPPED: {files}")             

summary_info = " | ".join (f"{cat}: {qtd}" for cat, qtd in sorted(by_category.items())) 
logger.info(
    f"SUMMARY - Reads: {total_reads} | Moved: {moved} | "
    f"Skipped: {skipped} | Renamed: {renamed} | Errors: {errors}"
)

if summary_info: 
    logger.info(f"SUMMARY by category - {summary_info}")
    
    