import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from pprint import pprint
nltk.download('vader_lexicon')
sia = SIA()
results = []
comments = ["I am so happy. this is a the best day ever"]
for line in comments:
    pol_score = sia.polarity_scores(line)
    pol_score['comment'] = line
    results.append(pol_score)
pprint(results[:7], width=100)
df1 = pd.DataFrame.from_records(results)
df1['label'] = 0
df1.loc[df1['compound'] > 0.2, 'label'] = 1
df1.loc[df1['compound'] < -0.2, 'label'] = -1
df2 = df1[['comment', 'label']]
df2.to_csv('reddit_comment_labels.csv', mode='a',
           encoding='utf-8', index=False)
print("Positive comments:\n")
pprint(list(df1[df1['label'] == 1].comment)[:5], width=200)
print("\nNegative comments:\n")
pprint(list(df1[df1['label'] == -1].comment)[:5], width=200)
print(df1.label.value_counts())
print(df1.label.value_counts(normalize=True) * 100)
sns.set(style='darkgrid', context='talk', palette='Dark2')
fig, ax = plt.subplots(figsize=(8, 8))
counts = df1.label.value_counts(normalize=True) * 100
sns.barplot(x=counts.index, y=counts, ax=ax)
ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")
plt.show()
# we can tell positive comments are not that positive in real
