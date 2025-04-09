import re
import json

log_file = "/tmp/timestamp.log"
output_json = "error_logs.json"

pattern = re.compile(r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - ERROR - (?P<message>.+)")

error_logs = []

with open(log_file, 'r') as f:
    for line in f:
        match = pattern.match(line)
        if match:
            error_logs.append({
                "timestamp": match.group("timestamp"),
                "error_message": match.group("message").strip()
            })

with open(output_json, 'w') as f:
    json.dump(error_logs, f, indent=4)

print(f"Extracted {len(error_logs)} error entries to {output_json}")
