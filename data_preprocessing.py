import os

def format_transcript(input_text):
    lines = input_text.split("\n")
    output = []
    current_speaker = ""
    current_seller_status = ""
    current_text = ""

    for line in lines:
        line = line.strip()

        if line.startswith("Speaker:"):
            if current_speaker:
                output.append(f"{current_speaker} (Seller: {current_seller_status}): {current_text.strip()}")
            parts = line.split(" (Seller:")
            current_speaker = parts[0].replace("Speaker:", "").strip()
            current_seller_status = parts[1].split(")")[0].strip() if len(parts) > 1 else "Unknown"
            current_text = "" 
        
        elif line.startswith("Text:"):
            current_text += " " + line.replace("Text:", "").strip() 
        
        else:
            current_text += " " + line.strip()

    if current_speaker:
        output.append(f"{current_speaker} (Seller: {current_seller_status}): {current_text.strip()}")

    return "\n".join(output) 

with open("transcript.txt", "r", encoding="utf-8") as input_file, open("temp.txt", "w", encoding="utf-8") as output_file:
    for line in input_file:
        if not line.strip().startswith("Start Time:"):
            output_file.write(line)

with open("temp.txt", "r", encoding="utf-8") as input_file, open("transcript.txt", "w", encoding="utf-8") as output_file:
    input_text = input_file.read()
    formatted_text = format_transcript(input_text)
    output_file.write(formatted_text)

os.remove("temp.txt")

print("Transcript successfully formatted and saved in transcript.txt")
