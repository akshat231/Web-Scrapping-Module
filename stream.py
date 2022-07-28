import imp
import streamlit as st
import numpy as np
import pandas as pd
import requests
import os
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from rake_nltk import Rake
import gensim
from gensim import corpora
import math
import spacy
from spacy.lang.en.examples import sentences 
def load_file(address):
    if os.path.exists(address)==False:
        print('path not found')
    if address.endswith('.txt'):
        f=open(address)
        g=f.read()
        return g
    else:
        print('Please give a txt file')


# In[12]:


def save_it(text):
     base=input("Give The Address where you want to save folder(Enter No if you want it to save in current directory)\n ")
     if str.lower(base)=="no":
        address=os.getcwd()
     else:
        address=base
     filename=input('Give Filename: \n')
     if os.path.exists(address)==False:
        print('Path Not Found')
     else:
        with open(address+"\\"+filename+".txt", 'w') as f:
            f.write(text)


# In[13]:


def load_url(link_provided):
    if link_provided=="":
        return "write URL"
    ua = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    from requests.exceptions import ConnectionError
    try:
        response = requests.get(link_provided, headers={"User-Agent": ua})
    except ConnectionError:
        print ('Failed to open url.')
        return
    if response.status_code!=200:
        print("Bad response code :", response.status_code, link_provided)
        return
    if response.status_code == 200:
        f=response.content
    from bs4 import  BeautifulSoup
    text=BeautifulSoup(f,"html.parser")
    text=text.getText()
    text=text.strip()
    text=text.rstrip('\n')
    text="\n".join(item for item in text.split('\n') if item)
    text=text.replace('\n','.')
    text=text.rstrip('\n')
    text = text.encode('utf-8').decode('ascii', 'ignore')
    return text


# In[14]:


def check_for_words_after_link(text,words):
    words=str.lower(words)
    for i in range(0,len(words)):
        if words[i] in text:
            return 'Forbidden words found'
    print("Forbidden words not found")


# In[15]:


def check_for_words_before_link(link_provided,words):
    if words=="":
        return 'write words to check'
    link_provided=str.lower(link_provided)
    for i in range(0,len(words)):
        if words[i] in link_provided:
            return 'Forbidden Words Found'
        else:
            return load_url(link_provided)


# In[16]:


punctuation=list(string.punctuation)


# In[17]:


def preprocess(text):
    text=word_tokenize(text)
    answer=[i for i  in text if i not in punctuation]
    for i in range(0,len(answer)):
        answer[i]=str.lower(answer[i])
    stopwords = nltk.corpus.stopwords.words('english')
    newanswer=[]
    for i in range(0,len(answer)):
        if answer[i] not in stopwords:
            newanswer.append(answer[i])
    porter_stemmer = PorterStemmer()
    stem_text=[]
    for i in range(0,len(newanswer)):
        stem_text.append(porter_stemmer.stem(newanswer[i]))
    wordnet_lemmatizer = WordNetLemmatizer()
    lemm_text=[]
    for i in range(0,len(stem_text)):
        lemm_text.append(wordnet_lemmatizer.lemmatize(stem_text[i]))
    return lemm_text


# In[18]:


def cloud_it(words):
    if isinstance(words,list):
        text=""
        for i in range(0,len(words)):
            text=text+words[i]
    else:
        text=words
    wordclou = WordCloud(width = 800, height = 800,background_color ='white',
                min_font_size = 10).generate(text)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.plot(wordclou)
    st.pyplot()



# In[19]:


def extract_it(words,n):
    if isinstance(words,list):
        text=""
        for i in range(0,len(words)):
            text=text+words[i]
    else:
        text=words
    r=Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()[0:n]


# In[20]:


def topic_model(words,n):
    if isinstance(words,list):
        text=words
    else:
        text=preprocess(words)
    id=corpora.Dictionary([text])
    corpus=[]
    for i in text:
        new=id.doc2bow(text)
        corpus.append(new)
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id,
                                           num_topics=30,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha="auto")
    my_dict = {'Topic_' + str(i): [token for token, score in lda_model.show_topic(i, topn=10)] for i in range(0, lda_model.num_topics)}
    new_dict=[]
    for i in range(0,min(n,len(my_dict))):
        new_dict.append(my_dict['Topic_'+str(i)])
    return new_dict


# In[21]:


def named_entity_recog(words):
    text=""
    if isinstance(words,list):
        for i in range(0,len(words)):
            text=text+words[i]
    else:
        text=words
    nlp=spacy.load('en_core_web_sm')
    doc = nlp(text)
    new=[]
    for ent in doc.ents:
        new.append(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_))
    return new







st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
x=st.radio(label="Do you want to scan the URL for forbidden words", options=["Yes", "No"])
if x=="Yes":
    y=st.text_input("Enter the words you don't want in URL separated by comma,only","")
    y=y.split(',')
    url = st.text_input("Enter URL","")
    if url is None:
        st.write('Enter the URL')
    else:
        out=check_for_words_before_link(url,y)
else:
    url=st.text_input("Enter URL","")
    out=load_url(url)
q1=st.radio("Do You want to print the scrapped data", options=["No","Yes"])
if q1=="Yes":
    st.write(out)
q=st.radio("Do you want to apply basic NLP operations",options=["No","Yes"])
if q=="Yes":
    notout=preprocess(out)
    st.write(notout)
q3=st.radio("Do You want to extract Keywords",options=["No","Yes"])
if q3=="Yes":
    num=st.number_input("Enter The number of keywords, you want to extract")
    num=math.floor(num)
    notout=preprocess(out)
    st.write(extract_it(notout,num))
q4=st.radio("Do you want to do topic modelling",options=["No","Yes"])
if q4=="Yes":
    num=st.number_input("Enter The number of topics to be printed")
    num=math.floor(num)
    notout=preprocess(out)
    st.write(topic_model(notout,num))
q5=st.radio("Do you want to do named entity recognition",options=["No","Yes"])
if q5=="Yes":
    notout=preprocess(out)
    st.write(named_entity_recog(notout))
        
st.write("Thanks, this is the end")