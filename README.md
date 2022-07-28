# Web-Scrapping-Module
This is the open source web scrapping module combined with different
NLP(Natural Language Processing) procedures.

The module offers nine functions:-

1.  save\_it:- Used for saving scrapped text as a file. It takes only
    one argument, i.e. text. The function also takes the inputs. Firstly
    it asks user about the directory where the file must be saved. User
    can write custom address or just type "no"(not case sensitive) to
    save it in the current directory. Then the function checks whether
    the path provided exist or not and throws an error if directory
    address is not valid. Then the function asks about the filename from
    the user. And then write it into the .txt file.

Example:-

> > > > > > > > > > save\_it("abc") "Enter the address where you want to
> > > > > > > > > > store the text, enter"no\" if want to save in
> > > > > > > > > > current directory\" "no" "Enter file name" "abc"

It will be saved, if paths are valid

2.load\_file:- This function load a .txt file, if path are provided are
valid. It takes only one argument, the address.

Example:-

> > > > > > > > > load\_file("D//abc.txt")

It will load teh file if path is valid

3.load\_url:- It is the main web scrapping module.It takes only one
argument, the url link. It also handles cases like wrong addresses.

Example:-

> > > > > > > > > > load\_url("http:://www.gov.in/")

It wil return the scrapped text

4.Check\_for\_words\_before\_link:- It is used to check the link url to
check for certain words. If a user doesn't want the URL to contain a
particular then it reports it back to the user.It takes two argument,
the link URL and the words that is not needed in URL. if the words
doesn't exist, it inherently calls for load\_url function

Example:-

> > > > > > > > check\_for\_words\_before\_link("http://www.gov.in",\["hello"\])

Since "hello" is not in the link so, it will call for load\_url and user
will get the scrapped text.

> > > > > > > check\_for\_words\_before\_link("http:://www.gov.in",\["Gov"\])

Now since, the link contains the forbidden word, so it will report back
with message that "Forbidden Word Found" and not scrap the data.

5.check\_for\_words\_after\_link:- It does the same thing with scrapped
text. It also takes two arguments, one is the scapped text and the other
is list of words.

Example:-

> > > > > > > check\_for\_words\_after\_link("abc",\[\"def\])

It wil return \"Forbidden words not found.

6.preprocess:- It is preprocessing function for scrapped text for
applying basic NLP function. It offers these functionalities:-

a.tokenization b.remove punctuation and stopwords c.stemming
d.lemmatization

Example:-

> > > > > > > > > preprocess("Hello our friend")

Output- \["hello","friend"\]

7.cloud\_it:- This function is used to make word cloud of the text. It
takes only one argument, the text. It also takes list of words as input.
User may input any form of string.

Example:-

> > > > > > > > > > cloud\_it("hi, how are you")

It will output the word cloud.

8.extract\_it:- This function extracts keywords from text. It takes two
arguments, one is text and the other is number of keywords, you want to
display.

Example:-

> > > > > > > > > extract\_it("hello,how are you?",2)

It will give top 2 keywords.

9.topic\_model:- It is used to do topic model on text. It takes two
arguments, one is text and the other is number of topics, user want to
display.

Example:-

> > > > > > > > > topic\_model("hi, how are you",3)

It will give three topics

10.named\_entity\_recog:- This function does the task of Named Entity
Recognition(NER) on text. It takes only one argument, the text and it
returns text after naming them.

Example:-

> > > > > > > > > named\_entity\_recog("Elon Musk is living dream")

output- Elon Musk \| PERSON

IMPORT PREREQUISITES FOR THIS:- <br>1.requests<br> 2.os<br> 3.nltk <br>a.word\_tokenize
<br>b.sent\_tokenize <br>c. PorterStemmer <br>d.WordNetLemmatizer>br> 4.string
<br>5.wordcloud <br>a.STOPWORDS <br>6.matplotlib <br>7.rake\_nltk <br>8.gensim <br>9.spacy
