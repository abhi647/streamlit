{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<streamlit.delta_generator.DeltaGenerator at 0x7fdbd494e990>"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Headings for Web Application\n",
    "st.title(\"Natural Language Processing Web Application Example\")\n",
    "st.subheader(\"What type of NLP service would you like to use?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Picking what NLP task you want to do\n",
    "option = st.selectbox('NLP Service',('Sentiment Analysis', 'Entity Extraction', 'Text Summarization')) #option is stored in this variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Textbox for text user is entering\n",
    "st.subheader(\"Enter the text you'd like to analyze.\")\n",
    "text = st.text_input('Enter text') #text is stored in this variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<streamlit.delta_generator.DeltaGenerator at 0x7fdbd494e990>"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Display results of the NLP task\n",
    "st.header(\"Results\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Sentiment Analysist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "from textblob import TextBlob\n",
    "from nltk.tokenize import sent_tokenize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/apple/opt/anaconda3/lib/python3.7/site-packages/altair/utils/core.py:187: UserWarning: I don't know how to infer vegalite type from 'empty'.  Defaulting to nominal.\n",
      "  \"Defaulting to nominal.\".format(typ)\n"
     ]
    }
   ],
   "source": [
    "if option == 'Sentiment Analysis':\n",
    "\n",
    "    #Creating graph for sentiment across each sentence in the text inputted\n",
    "    sents = sent_tokenize(text) #tokenizing the text data into a list of sentences\n",
    "    entireText = TextBlob(text) #storing the entire text in one string\n",
    "    sentScores = [] #storing sentences in a list to plot\n",
    "    for sent in sents:\n",
    "        text = TextBlob(sent) #sentiment for each sentence\n",
    "        score = text.sentiment[0] #extracting polarity of each sentence\n",
    "        sentScores.append(score) \n",
    "\n",
    "    #Plotting sentiment scores per sentencein line graph\n",
    "    st.line_chart(sentScores) #using line_chart st call to plot polarity for each sentence"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Polarity and Subjectivity of the entire text inputted\n",
    "sentimentTotal = entireText.sentiment\n",
    "st.write(\"The sentiment of the overall text below.\")\n",
    "st.write(sentimentTotal)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Building NER"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "#NER Imports\n",
    "import spacy\n",
    "from spacy import displacy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "if option == 'Entity Extraction':\n",
    "\n",
    "    #Getting Entity and type of Entity\n",
    "    entities = []\n",
    "    entityLabels = []\n",
    "    doc = nlp(text)\n",
    "    for ent in doc.ents:\n",
    "        entities.append(ent.text)\n",
    "        entityLabels.append(ent.label_)\n",
    "    entDict = dict(zip(entities, entityLabels)) #Creating dictionary with entity and entity types\n",
    "\n",
    "    #Using function to create lists of entities of each type\n",
    "    entOrg = entRecognizer(entDict, \"ORG\")\n",
    "    entCardinal = entRecognizer(entDict, \"CARDINAL\")\n",
    "    entPerson = entRecognizer(entDict, \"PERSON\")\n",
    "    entDate = entRecognizer(entDict, \"DATE\")\n",
    "    entGPE = entRecognizer(entDict, \"GPE\")\n",
    "\n",
    "    #Displaying entities of each type\n",
    "    st.write(\"Organization Entities: \" + str(entOrg))\n",
    "    st.write(\"Cardinal Entities: \" + str(entCardinal))\n",
    "    st.write(\"Personal Entities: \" + str(entPerson))\n",
    "    st.write(\"Date Entities: \" + str(entDate))\n",
    "    st.write(\"GPE Entities: \" + str(entGPE))\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "from gensim.summarization.summarizer import summarize \n",
    "from gensim.summarization import keywords"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "if option == 'Text Summarization':\n",
    "    summWords = summarize(text)\n",
    "    st.subheader(\"Summary\")\n",
    "    st.write(summWords)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
