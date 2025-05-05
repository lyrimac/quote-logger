from datetime import datetime

quote = input("Enter your favorite quote: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("quotes.txt", "a") as file:
    file.write(f"[{timestamp}] {quote}\n")

print("Thanks! Your quote has been logged.")