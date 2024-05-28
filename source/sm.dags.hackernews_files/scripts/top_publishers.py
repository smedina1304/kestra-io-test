import io
import pandas as pd

# Read CSV
df_topstories = pd.read_csv("topstories.csv")

print(f"df_topstories lines:{df_topstories.shape[0]}")

# Selects data and counts posts by publisher
topstories = df_topstories[['by','url','descendants','score']].copy()
grp = topstories.groupby(['by'])['by'].count().reset_index(name='counts')
    
# Select top 10 publishers
top_publishers=grp.sort_values('counts', ascending=False)[:10]

# Save CSV
top_publishers.to_csv('top_publishers.csv', index=False)
