from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import load_files
categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']
# twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
twenty_train = load_files(container_path='C:/Users/Tran/git/_learning/learning_ml/data/20news-bydate/20news-bydate-train', categories=categories)
twenty_train.target_names
len(twenty_train.data)
twenty_train.data[0]
len(twenty_train.target)
len(twenty_train.target)

print("\n".join(["test1", "test2"]))
print("\n".join(twenty_train.data[0].split("\n")[:3]))

twenty_train.target[:10]

for t in twenty_train.target[:10]:
    print(twenty_train.target_names[t])

twenty_train.filenames[:10]


from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(decode_error='ignore')
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_train_counts.shape



