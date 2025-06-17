#14.	Censor Bad Words
#•	Input a sentence and replace "bad" and "ugly" with "***"
sentence = input("What is your sentence? : ")
bad_words = ["bad", "ugly"]
censored = sentence
for word in bad_words:
    censored = censored.replace(word, "***")
print("Censored Sentence :", censored)
    

