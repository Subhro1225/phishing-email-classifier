import pandas as pd
# Import TF-IDF vectorizer to convert email text into numerical features
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.model_selection import train_test_split

# reading csv file
df = pd.read_csv("data/cleaned_email.csv")
# print(df.head()) // prints first 5 rows of a dataframe.

# joining the body and the subject in a single column
df['text'] = df['subject'] + " " + df['body']
# print(df.head())

# droping the rest of the columns
df = df.drop(columns=['subject','body'])

# print(df.head())
# print(df.columns)

# Tf-Idf on the dataframe
# 1. max_features — keeps only the top N most frequent/important words, drops the rest
# 2. stop_words — automatically removes common useless words like "the", "is", "a", "and"
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
x = vectorizer.fit_transform(df['text'])
# print(x.shape)

# spliting training and testing data
x_train , x_test , y_train , y_test = train_test_split(x, df['label'] , test_size=0.2 , random_state=42)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)