This is the open source web scrapping module combined with different NLP(Natural Language Processing) procedures.

The module offers nine functions:-



1. save_it:- Used for saving scrapped text as a file. It takes only one argument, i.e. text. The function also takes the inputs. Firstly it asks user about the directory where the file must be saved. User can write custom address or just type "no"(not case sensitive) to save it in the current directory. Then the function checks whether the path provided exist or not and throws an error if directory address is not valid. Then the function asks about the filename from the user. And then write it into the .txt file.

Example:-


>>>>>>>>>>save_it("abc")
>>>>>>>>>>"Enter the address where you want to store the text, enter "no" if want to save in current directory"
>>>>>>>>>>"no"
>>>>>>>>>>"Enter file name"
>>>>>>>>>>"abc"


It will be saved, if paths are valid


2.load_file:- This function load a .txt file, if path are provided are valid. It takes only one argument, the address.

Example:-


>>>>>>>>>load_file("D//abc.txt")

It will load teh file if path is valid


3.load_url:- It is the main web scrapping module.It takes only one argument, the url link. It also handles cases like wrong addresses. 

Example:-


>>>>>>>>>>load_url("http:://www.gov.in/")

It wil return the scrapped text



4.Check_for_words_before_link:- It is used to check the link url to check for certain words. If a user doesn't want the URL to contain a particular then it reports it back to the user.It takes two argument, the link URL and the words that is not needed in URL. if the words doesn't exist, it inherently calls for load_url function

Example:-


>>>>>>>>check_for_words_before_link("http://www.gov.in",["hello"])

Since "hello" is not in the link so, it will call for load_url and user will get the scrapped text.

>>>>>>>check_for_words_before_link("http:://www.gov.in",["Gov"])

Now since, the link contains the forbidden word, so it will report back with message that "Forbidden Word Found" and not scrap the data.



5.check_for_words_after_link:- It does the same thing with scrapped text. It also takes two arguments, one is the scapped text and the other is list of words.


Example:-


>>>>>>>check_for_words_after_link("abc",["def])

It wil return "Forbidden words not found.



6.preprocess:- It is preprocessing function for scrapped text for applying basic NLP function. It offers these functionalities:-

a.tokenization
b.remove punctuation and stopwords
c.stemming
d.lemmatization

Example:-

>>>>>>>>>preprocess("Hello our friend")

Output- ["hello","friend"]


7.cloud_it:- This function is used to make word cloud of the text. It takes only one argument, the text. It also takes list of words as input. User may input any form of string.


Example:-

>>>>>>>>>>cloud_it("hi, how are you")

It will output the word cloud.


8.extract_it:- This function extracts keywords from text. It takes two arguments, one is text and the other is number of keywords, you want to display.


Example:-

>>>>>>>>>extract_it("hello,how are you?",2)

It will give top 2 keywords.



9.topic_model:- It is used to do topic model on text. It takes two arguments, one is text and the other is number of topics, user want to display.

Example:-


>>>>>>>>>topic_model("hi, how are you",3)


It will give three topics



10.named_entity_recog:- This function does the task of Named Entity Recognition(NER) on text. It takes only one argument, the text and it returns text after naming them.


Example:-

>>>>>>>>>named_entity_recog("Elon Musk is living dream")

output- Elon Musk | PERSON



IMPORT PREREQUISITES FOR THIS:-
1.requests
2.os
3.nltk
   a.word_tokenize
   b.sent_tokenize
   c. PorterStemmer
   d.WordNetLemmatizer
4.string
5.wordcloud
   a.STOPWORDS
6.matplotlib
7.rake_nltk
8.gensim
9.spacy
10.

