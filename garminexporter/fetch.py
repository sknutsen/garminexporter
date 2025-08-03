import os
from garminexport.incremental_backup import incremental_backup

def fetch():
    try:
        incremental_backup(
            username=os.environ["USERNAME"],
            password=os.environ["PASSWORD"],
            backup_dir=os.path.join(".", "activities"),
            export_formats=None,
            ignore_errors=False,
            max_retries=7,
        )

    except Exception as e:
        log.error("failed with exception: {}".format(e))
