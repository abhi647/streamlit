import streamlit as st
from spacy import displacy
from gensim.summarization.summarizer import summarize 
from gensim.summarization import keywords
import spacy
#Headings for Web Application
st.title("Natural Language Processing Web Application Example")
st.subheader("What type of NLP service would you like to use?")
#Picking what NLP task you want to do
option = st.selectbox('NLP Models',('Sentiment Analysis', 'Text Summarization')) #option is stored in this variable
#Textbox for text user is entering
st.subheader("Enter the text you'd like to analyze.")
text = st.text_input('Enter text') #text is stored in this variable
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#Display results of the NLP task
st.header("Results")

#Sentiment Analysis
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
if option == 'Sentiment Analysis':

    #Creating graph for sentiment across each sentence in the text inputted
    sents = sent_tokenize(text) #tokenizing the text data into a list of sentences
    entireText = TextBlob(text) #storing the entire text in one string
    sentScores = [] #storing sentences in a list to plot
    for sent in sents:
        text = TextBlob(sent) #sentiment for each sentence
        score = text.sentiment[0] #extracting polarity of each sentence
        sentScores.append(score) 

    #Plotting sentiment scores per sentencein line graph
    st.line_chart(sentScores) #using line_chart st call to plot polarity for each sentence
    #Polarity and Subjectivity of the entire text inputted
    sentimentTotal = entireText.sentiment
    st.write("The sentiment of the overall text below.")
    st.write(sentimentTotal)

 # text summarization
else:
    option == 'Text Summarization'
    summWords = summarize(text)
    st.subheader("Summary")
    st.write(summWords)
 