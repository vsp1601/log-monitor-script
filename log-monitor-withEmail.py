import sys
import signal
from collections import Counter
import time
import smtplib  # for email notifications

# Define variables
log_file = "/path/to/your/logfile.log"
keywords = ["error", "warning"]
summary_interval = 60  # Generate summary report every minute (seconds)
notification_email = "your_email@example.com"  # Configure recipient email
critical_keywords = ["critical"]  # Keywords triggering email notifications


def handle_interrupt(sig, frame):
    print("Exiting...")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)


def send_notification(message):
    sender_email = "log_monitor@yourdomain.com"  # Configure sender email
    password = "your_password"  # Configure email password (consider secure storage)

    server = smtplib.SMTP("smtp.yourserver.com", 587)  # Replace with your email server
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, notification_email, message)
    server.quit()
    print(f"Notification sent to {notification_email}")


def main():
    with open(log_file, "r") as f:
        f.seek(0, 2)  # Seek to end of file initially

        last_reported_time = time.time()
        log_count = 0
        keyword_counts = Counter()

        while True:
            time.sleep(1)  # Check for changes every second

            # Read new lines from the current position
            lines = f.readlines()

            # Update counters
            log_count += len(lines)
            for line in lines:
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        keyword_counts[keyword] += 1
                for critical_keyword in critical_keywords:
                    if critical_keyword.lower() in line.lower():
                        message = f"Critical log message found: {line}"
                        send_notification(message)

            
            for line in lines:
                print(line, end="")

            # Generate summary report at intervals
            if time.time() - last_reported_time >= summary_interval:
                print(f"\n** Summary Report (Last {summary_interval} seconds) **")
                print(f"Total Lines: {log_count}")
                for keyword, count in keyword_counts.items():
                    print(f"{keyword.title()}: {count}")
                keyword_counts.clear()  # Reset counter for next interval
                last_reported_time = time.time()

            # Seek to the end again for next iteration
            f.seek(f.tell())


if __name__ == "__main__":
    main()
