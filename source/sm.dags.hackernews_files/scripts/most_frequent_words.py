import io
import pandas as pd

# Read CSV
df_topstories = pd.read_csv("topstories.csv")
df_stopwords  = pd.read_csv("stopwords.csv")

print(f"df_topstories lines:{df_topstories.shape[0]}")
print(f"df_stopwords lines:{df_stopwords.shape[0]}")

# stopwords - Convert from dataframe to set
stopwords = set(df_stopwords['words'].tolist())

# loop through the titles and count the frequency of each word
word_counts = {}
for raw_title in df_topstories["title"]:
    title = raw_title.lower()
    for word in title.split():
        cleaned_word = word.strip(".,-!?:;()[]'\"–")
        if cleaned_word not in stopwords and len(cleaned_word) > 0:
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1

# Get the top 25 most frequent words
top_words = {
    pair[0]: pair[1]
    for pair in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:15]
}

print(f'top_words is {type(top_words)}')
print(top_words)

df = pd.DataFrame(top_words.items(), columns=['words', 'count'])
df.to_csv('most_frequent_words.csv', index=False)


