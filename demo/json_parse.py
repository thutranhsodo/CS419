import nltk, unicodedata, json, os, re
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

dir_path = os.path.dirname(os.path.realpath(__file__))


def normalize(text):
    tokens = word_tokenize(text)
    tokens_lower = [word.lower() for word in tokens]
    cleaned_tokens = [re.sub(r'[^A-Za-z]+', '', word) for word in tokens_lower]
    cleaned_tokens = [word for word in cleaned_tokens if word]
    stop_words = set(stopwords.words('english'))
    tokens_no_stopwords = [word for word in cleaned_tokens if word not in stop_words]
    porter_stemmer = PorterStemmer()
    stemmed_tokens = [porter_stemmer.stem(word) for word in tokens_no_stopwords]
    return stemmed_tokens

with open('cnn.json', encoding="utf8") as json_data:
    articles = json.load(json_data)
    print(len(articles), "Articles loaded succesfully")
    statistic = {}
    for article in articles:
        title = article['title']
        author = article['author']
        cate = article['cate']
        content = article['content']
        source_url = article['source_url']
        if cate != None:
            newpath = dir_path + '\\tf-idf\\' + cate

            # keep track of what cate and number of txt files have been gone through
            if cate not in statistic:
                count = 0
                statistic[cate] = 0
            else:
                statistic[cate] += 1
            count = statistic[cate]

            # Create new cate folder when one not exists
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            file_name = str(count)+'.txt'
            complete_path = os.path.join(newpath, file_name)
            # f = open(complete_path, 'w', encoding="utf-8")
            # f.write('{}\n{}\n{}\n'.format(normalize(title), cate, normalize(content)))
            with open(complete_path, 'w', encoding="utf-8") as f:
                f.write('{}\n{}\n{}\n{}\n{}\n'.format(
                    normalize(title),
                    author,
                    cate,
                    normalize(content),
                    source_url
                ))
            f.close()