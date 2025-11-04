# CodeAlpha Task 3 - Task Automation: Extract Emails from a Text File
import re

# Input and output file names
input_file = "sample.txt"
output_file = "emails_found.txt"

try:
    # Read text from file
    with open(input_file, "r") as f:
        data = f.read()

    # Find all email addresses using regex
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', data)

    # Remove duplicates
    unique_emails = list(set(emails))

    # Save found emails to another file
    with open(output_file, "w") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"{len(unique_emails)} emails extracted successfully!")
    print(f"Saved to {output_file}")

except FileNotFoundError:
    print("Error: sample.txt not found. Please make sure the file exists.")