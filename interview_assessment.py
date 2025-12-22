import random
import csv

# Read questions from txt file
with open('question.txt', 'r') as file:
    questions = [line.strip() for line in file if line.strip()]

# Select random 5 questions
selected_questions = random.sample(questions, 5)

# Print the questions
print("Here are 5 random Python questions:")
for i, q in enumerate(selected_questions, 1):
    print(f"{i}. {q}")

# Ask for user input
name = input("\nEnter your name: ")
contact = input("Enter your contact: ")

# Ask for ratings
comm_rating = input("\nEnter communication rating (1-10): ")
tech_rating = input("Enter technical rating (1-10): ")

# Write to CSV
with open('interview_data.csv', 'a', newline='') as csvfile:
    fieldnames = ['Name', 'Contact', 'Question1', 'Question2', 'Question3', 'Question4', 'Question5', 'Communication_Rating', 'Technical_Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write header if file is empty
    if csvfile.tell() == 0:
        writer.writeheader()
    
    writer.writerow({
        'Name': name,
        'Contact': contact,
        'Question1': selected_questions[0],
        'Question2': selected_questions[1],
        'Question3': selected_questions[2],
        'Question4': selected_questions[3],
        'Question5': selected_questions[4],
        'Communication_Rating': comm_rating,
        'Technical_Rating': tech_rating
    })

print("\nData has been written to interview_data.csv")