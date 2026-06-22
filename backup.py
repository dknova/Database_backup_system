import shutil
from datetime import datetime

source_file = "sample.db"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_file = f"backups/backup_{timestamp}.db"

shutil.copy(source_file, backup_file)

print("Backup created:", backup_file)
