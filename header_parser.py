import re

def parse_header(header_text):
    print("📨 Parsed Email Header Information:\n")

    # Extract "From"
    from_match = re.search(r"From: (.+)", header_text)
    if from_match:
        print(f"From: {from_match.group(1)}")

    # Extract "Return-Path"
    return_path = re.search(r"Return-Path: <(.+)>", header_text)
    if return_path:
        print(f"Return-Path: {return_path.group(1)}")

    # Extract Received chain
    received_lines = re.findall(r"Received: .+", header_text)
    print(f"\nReceived Headers ({len(received_lines)}):")
    for i, line in enumerate(received_lines, 1):
        print(f"{i}. {line}")

    # Check for SPF or DKIM results
    spf = re.search(r"spf=(\w+)", header_text, re.IGNORECASE)
    if spf:
        print(f"\nSPF Result: {spf.group(1)}")

    dkim = re.search(r"dkim=(\w+)", header_text, re.IGNORECASE)
    if dkim:
        print(f"DKIM Result: {dkim.group(1)}")

# Example usage
if __name__ == "__main__":
    try:
        with open("sample_header.txt", "r") as file:
            raw_header = file.read()
            parse_header(raw_header)
    except FileNotFoundError:
        print("sample_header.txt not found. Please place the email header file in the same folder.")
