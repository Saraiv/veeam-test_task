# Instructions
Help
```
python3 main.py --help

usage: main.py [-h] [--interval INTERVAL] [--log_file LOG_FILE] source_folder replica_folder

Synchronize the contents of a source folder with a replica folder.

positional arguments:
  source_folder        The source folder to synchronize.
  replica_folder       The replica folder to synchronize.

options:
  -h, --help           show this help message and exit
  --interval INTERVAL  The interval in seconds to perform synchronization periodically.
  --log_file LOG_FILE  Path to the log file.
```

Usage example
```
python3 main.py "source" "replica" --log_file="./log.txt"
```
