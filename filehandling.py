import random
import csv

# Read questions from txt file
with open("question.txt", "r") as f:
    questions = [line.strip() for line in f if line.strip()]

# User details
name = input("Enter your name: ")
contact = input("Enter your contact: ")

# Pick random 5 questions
selected = random.sample(questions, 5)

print("\nHere are 5 random Python questions:")
# Ratings
comm = input("\nEnter communication rating (1-10): ")
tech = input("Enter technical rating (1-10): ")

# Write to CSV
with open("interview_data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(["Name", "Contact", "Q1", "Q2", "Q3", "Q4", "Q5", "Comm_Rating", "Tech_Rating"])
    writer.writerow([name, contact, *selected, comm, tech])

print("\n✅ Data saved to interview_data.csv")