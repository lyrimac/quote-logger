from datetime import datetime

quote = input("Enter your favorite quote: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("quotes.txt", "a") as file:
    file.write(f"[{timestamp}] {quote}\n")

print("Your quote was saved successfully.")
