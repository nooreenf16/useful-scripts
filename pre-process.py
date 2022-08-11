import re
import pandas
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#df = pd.read_csv('data.csv')

strings = ['hello there, i have the most number of words.',
           'This, is the second sentence.']

clean_text = []
for text in strings:
    message = re.sub(
        r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", text)
    message = re.sub(r"[,@\'?\:.$%_]", "", message)
    message = re.sub('[/:.\d]', ' ', message)
    message = re.sub(r"\s+", " ", message)
    message = message.lower()
    message = message.split()
    ps = PorterStemmer()
    all_words = stopwords.words('english')
    message = [ps.stem(word) for word in message if not word in set(all_words)]
    clean_text.append(message)

print(clean_text)
