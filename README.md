# The Bechdel Test

 
 <p align="center">
	<img width=100% src="https://user-images.githubusercontent.com/4650739/34265870-eb4dc20c-e63c-11e7-8188-a4096ef24153.jpeg" />

</p>
<h3 align="center">Part A: Does Your Screenplay Pass The Bechdel Test?</h3>
<h3 align="center">Part B: Can A Model Produce A Scene That Passes The Bechdel Test?</h3>
 
 
 ### Table of Contents

* [Problem Statement](#user-content-problem-statement)
* [Introduction](#user-content-introduction)
* [Executive Summary](#user-content-executive-summary)
* [Conclusions and Recommendations](#user-content-conclusions-and-recommendations)
* [Data](#user-data)
* [Additional Resources](#user-content-additional-information)


---
 
 
 
 ### Problem Statement
 
A: Can I use machine learning to train a model to reliably predict whether or not a screenplay passes The Bechdel Test?
 
I have chosen Alison Bechdel giving films a "Thumbs Up" or "Thumbs Down" review entirely at random as our baseline model. That would be 50/50 for you folks without thumbs.

B: Using LSTM Neural Networks, can I train a model to write scenes that pass The Bechdel Test?
 
 
 ### Introduction
 
 What is The Bechdel Test, you ask? Well, a film or screenplay passes The Bechdel Test by meeting the following requirements:
 
1. It includes at least two (named) women
2. who have at least one conversation
3. about something other than a man or men.

Alison Bechdel first presented this test in her comic "Dykes to Watch Out For", in a 1985 strip titled, "The Rule". You can read more of Alison Bechdel's comics [on her website](https://dykestowatchoutfor.com/). 

This test, while incredibly simple and specific, has become a cultural tentpole for measuring gender parity in film. Many films do not pass this test, despite the incredibly low bar set by the parameters of the test.
 
 
 
 ### Executive Statement
 
##### Part A:

I was able to use The Bechdel Test API to receive all the information from that website and put that into a dataframe.
 
I then went about collecting scripts in txt format from a number of sources. The [Kaggle source](https://www.kaggle.com/parthplc/movie-scripts) that I originally used included 2,827 scripts, had an issue where all the files were simply "file_1.txt" and so on. I wrote a simple script (script-namer.py) to run through these scripts and rename them to the first line of the file, which was the title of the film for many of these. Much data was lost in the process though and I wound up only keeping 936 scripts from this.

Using The www.bechdeltest.com API, I was able to call the API and create a dataframe with all of the information available from this site. It included the Bechdel score, year produced, and IMDB ID, among a couple other features.

The screenplays did not include any metadata like an IMDB ID, which made things difficult for merging with the Bechdel Test dataframe. I wound up cleaning the title columns for both dataframes and merging on this instead. There were a lot of issues with this method, but worked well enough to leave me with 464 scripts in my dataframe, merged with their Bechdel Scores.

After some cleaning, pre-processing, and EDA, I moved into modeling, but knew that we were going to have a hard time. I tried a number of different models and configurations (logistic regression, K-Nearest Neighbors, Bernoulli Naive Bayes, LSTM Neural Network) and found the logistic regression, with TfidFVectorizer, to be most accurate at .62%. All models were prone to overfitting. This is not statistically significant to reject the null hypothesis. On this occasion, I have not been able to produce a model that can reliably predict if a film can pass The Bechdel Test.


##### Part B:

As an addition to the project, I trained an LSTM Neural Network to provide text generation, based on a series of screenplays that are female-centric, in the hopes that the result would largely be generated text that passes The Bechdel Test. Unfortunately, after a number of attempts, the results are mixed at best. I used char2Vec for this, as this keeps the overall structure of a screenplay intact (the white space is necessary). I trained a model on word2Vec as well, but the structure was lost, and the model would continuously converge onto a single value (normally either "the" or "thicker") after roughly fifty words.

 ---
 
 ### Conclusions and Recommendations
 
The Bechdel Test is a difficult metric on which to gauge a screenplay. "DIE HARD" passes the test because it has two named women who speak to each other early on at the company party, and "The Girl With The Dragon Tattoo" fails because many of the women are not named. As a result I had a hard time getting a model to predict for passing The Bechdel Test.

If you were to attempt a similar thing, I would actually suggest using Python Control Flow to create a series of IF/ELSE statements to parse through a screenplay, divide it into individual scenes, search through the names to see if there are two women in the scene, then search through the scene to find the dialogue, and finally to ensure that the dialogue is no mentioning any men.

As for text generation of scenes in a screenplay, this would be best tackled piece by piece. A further project would be to train models on scene headings, action, and dialogue respectively. I will attempt this in another project.

And, of course, I would recommend having more observations in your dataset.
 
 
 ### Data
 
 The scripts were taken from this [dataset on Kaggle](https://www.kaggle.com/parthplc/movie-scripts).
 
 I used an API to call all the data from www.BechdelTest.com
 
The lists for male and female names were found [here](https://github.com/stefanomezza/bechdel-test/tree/master/data). The lists were edited to reflect character naming probabilities (names like Tony and Adrian were commented out from female names, for example).
 
---
 
 ### Additional Resources

Please support the original artist Alison Bechdel [at her website](https://dykestowatchoutfor.com/). 

Slides for the presentation were found on [slidesgo](https://slidesgo.com/).

Other attempts at The Bechdel Test can be found [here](https://github.com/JoeKarlsson/bechdel-test), [here](https://github.com/stefanomezza/bechdel-test), and [here](https://github.com/serinachang5/bechdel).

The Streamlit App and text generation ideas were inspired by [Script Buddy](https://github.com/cdpierse/script_buddy_v2), by Charles Pierse.
