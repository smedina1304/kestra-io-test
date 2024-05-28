import io
import pandas as pd
from urllib.parse import urlparse

# Read CSV
df_topstories = pd.read_csv("topstories.csv")

print(f"df_topstories lines:{df_topstories.shape[0]}")

top10 = df_topstories[['url','score']].sort_values('score', ascending=False).copy()
top10.dropna(inplace=True)
top10 = top10[0:10]
top10['url'] = top10['url'].apply(lambda x: urlparse(x).hostname)

# Save CSV
top10.to_csv('top_scores.csv', index=False)