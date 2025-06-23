import count_words
if __name__ == "__main__":
    name = input("Enter the word : ")
    length = count_words.count_words(name)
    print(f"Length of {name} is {length}")