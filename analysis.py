import pandas as pd
from collections import Counter


df = pd.read_csv("ethiopian_news.csv")


total = len(df)
longest = max(df["title"], key=len)
shortest = min(df["title"], key=len)
avg_length = df["title"].apply(len).mean()

#  remove useless words
stopwords = {
    "the", "to", "of", "in", "on", "and", "a", "for", "is", "with",
    "as", "at", "by", "from", "it", "this", "that", "an", "be", "are",
    "was", "were", "will", "has", "have", "had"
}

# Word processing
all_words = []

for title in df["title"]:
    words = title.lower().split()

    for word in words:
        # clean punctuation
        word = word.strip(".,“”\"'():;-")

        # filter useless words
        if word and word not in stopwords:
            all_words.append(word)

# Count frequency
counter = Counter(all_words)
top_10 = counter.most_common(10)


print("\n ETHIOPIAN NEWS ANALYSIS \n")

print("Total Headlines:", total)

print("\nLongest Headline:\n", longest)

print("\nShortest Headline:\n", shortest)

print("\nAverage Headline Length:", round(avg_length, 2))

print("\nTop 10 Meaningful Words:\n")

for word, count in top_10:
    print(f"{word} : {count}")