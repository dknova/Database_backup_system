import shutil
import os
from datetime import datetime

os.makedirs("backups", exist_ok=True)

source_file = "sample.db"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_file = f"backups/backup_{timestamp}.db"

shutil.copy(source_file, backup_file)

print("Backup created:", backup_file)
