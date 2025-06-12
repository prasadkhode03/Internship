#12.	Build a Mini Quiz Game using Functions
"""•	Use a function ask_question(question, correct_answer)
•	Ask 3–5 questions and return score at the end"""
score = 0
def ask_question(question, correct_answer):
    global score
    print("\n",question)
    ans = input("Enter the correct answer : ")
    if ans == correct_answer:
        score += 1
    
que1 = "1. What is the data type of \"hello\" ?"
ask_question(que1, "string")

que2 = "2. What operator is used for modulus?"
ask_question(que2, "%")

que3 = "3. What is the keyword to exit a loop prematurely?"
ask_question(que3, "break")

que4 = "4. What data structure stores key-value pairs?"
ask_question(que4, "dictionary")

que5 = "5. What is the term for finding errors in code?"
ask_question(que5, "debugging")

print("Your score =",score)