from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()
# text_1 = "Delhi is capital of India."
# text_2 =  "The pizza tastes terrible."
# sent_1 = sentiment.polarity_scores(text_1)
# sent_2 = sentiment.polarity_scores(text_2)
# print(text_1)
# print("Sentiment of text 1:", sent_1)
# print("__________________________________________________________________________________")
# print(text_2)

# print("Sentiment of text 2:", sent_2)

# print("\n ==================================================================================\n")


# text_1 = "I am the best."
# text_2 =  "Deepti is a name of girl."
# sent_1 = sentiment.polarity_scores(text_1)
# sent_2 = sentiment.polarity_scores(text_2)
# print(text_1)
# print("Sentiment of text 1:", sent_1)
# print("__________________________________________________________________________________")
# print(text_2)

# print("Sentiment of text 2:", sent_2)



numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

# String array (list of strings)
testArray = [
    "I am the best.", 
    "Deepti is a name of girl.", 
    "Delhi is capital of India.", 
    "The pizza tastes terrible.",
    "Today, I am not in mood to go to office",
    "I am not feeling good, I have fever",
    "it is too cold but i dont like to wear woolen cloth",
    "I am too good as coffee",
    "i am feeling as good as we are celebrating diwali",
    "we are celebrating diwali",
    "The world is full of endless possibilities, and every day is a new opportunity to shine brighter, dream bigger, and achieve the unimaginable.",
    "Life is a radiant journey filled with boundless joy, infinite love, and endless reasons to smile, where every moment is a celebration of pure happiness and limitless potential!",
    "I am the happiest person in the world.",
    "I am the queen of happiness.",
    "I am the greatest person in the world.",
    "I am the happiest person in the universe.",
    "Goat is an animal",
    "We are human",
    "Love is God",
    "Love is in the air",
    "Hatred is spread",
    "our future is the brightest as the sun",
    "our future is the darkest as the sunset",
    "No matter the challenge, I believe that brighter days are always ahead.",
    "You are capable of achieving incredible things, and every effort you make brings you closer to success.",
    "I love my india",
    "Life is a beautiful adventure, full of laughter, love, and the chance to create wonderful memories. daughters are blessed with love. they are the light of our lives.",
    "Life is a magnificent journey overflowing with joy, love, and endless opportunities to create cherished memories. Daughters are the purest blessings, radiating warmth and love, lighting up our lives with their boundless happiness and making every moment more magical than the last!",
    "It seems too cold but i dont have any money to buy woolen cloth"
    ]

# Loop through the string array
for text in testArray:
    sent = sentiment.polarity_scores(text)
    print(text)
    print("Sentiment of text :", sent)
    print("__________________________________________________________________________________")
    print("Negative:", sent['neg'], "Neutral:", sent['neu'], "Positive:", sent['pos'], "Compound:", sent['compound'])
    print("__________________________________________________________________________________")


