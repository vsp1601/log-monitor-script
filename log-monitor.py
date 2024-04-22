import sys
import signal
from collections import Counter

log_file = "/path/to/your/logfile.log"  # Replace with your log file path
keywords = ["error", "warning"]  # Keywords to count
summary_interval = 60  # Generate summary report every minute (seconds)

# Function to handle Ctrl+C interrupt
def handle_interrupt(sig, frame):
    print("Exiting...")
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, handle_interrupt)

# Initialize counters
log_count = 0
keyword_counts = Counter()

# Continuously monitor the log file
with open(log_file, "r") as f:
    f.seek(0, 2)

    while True:
        # Read new lines from the current position
        lines = f.readlines()

        # Update counters
        log_count += len(lines)
        for line in lines:
            for keyword in keywords:
                if keyword in line.lower():
                    keyword_counts[keyword] += 1

        # Print new log entries
        for line in lines:
            print(line, end="")

        # Print summary report at intervals
        if log_count % summary_interval == 0:
            print(f"\n** Summary Report (Last {summary_interval} seconds) **")
            print(f"Total Lines: {log_count}")
            for keyword, count in keyword_counts.items():
                print(f"{keyword.title()}: {count}")
            keyword_counts.clear()  # Reset counter for next interval

        # Wait for changes before reading again
        f.seek(f.tell())

