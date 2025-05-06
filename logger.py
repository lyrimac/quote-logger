# This branch is for demonstrating a pull request

from datetime import datetime

quote = input("What's a quote that inspires you today? ")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("quotes.txt", "a") as file:
    file.write(f"[{timestamp}] {quote}\n")

print("Thank you! Your quote has been logged.")