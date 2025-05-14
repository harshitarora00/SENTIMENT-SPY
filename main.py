from textblob import TextBlob

print("👋 Welcome to the Ai mood Detector!")
name  = input("Please Enter your name: ")
print(f"Nice to meet you, {name}! Let's guess the sentiments of your sentences")
print("Type exit to quit \n")

while True:
    sentence = input("Enter the sentence: ")
    if sentence.lower() == "exit":
        print(f"Goodbye {name}!")
        break
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print("☺️ positive sentiment detected")
    elif sentiment < 0:
        print("negative sentiment detected")
    else:
        print("neutral sentence detected")
    