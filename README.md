# log-monitor-script

List of Configuration to be updated:
  1. Log File Path: Replace /path/to/your/logfile.log with the actual path to the log file you want to monitor.
  2. Keywords: Modify the keywords list to include specific keywords or patterns you want to track within the log entries (e.g., "error", "warning").
  3. Summary Interval: Adjust the summary_interval variable to change how often a summary report is generated (measured in seconds).

Steps to Run the Script:
  1. Save the script as log-monitor.py.
  2. Open a terminal and navigate to the directory containing the script.
  3. Run the script using the command python log-monitor.py.

Output:
  1. The script continuously displays new log entries as they appear in the specified log file.
  2. Every summary_interval seconds (as defined in the configuration), a summary report is printed. This report shows:
  3. Total number of log entries processed during the interval.
  4. Count of occurrences for each keyword you specified in the configuration.

To Exit the Script:
  1. Press Ctrl+C on your keyboard to stop the monitoring and exit the script.
