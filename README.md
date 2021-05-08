# THIS PROJECT IS CURRENTLY UNDER CONSTRUCTION - COMPLETION DATE - 13.05.2021

# The Bechdel Test

 
 <p align="center">
	<img width=100% src="https://user-images.githubusercontent.com/4650739/34265870-eb4dc20c-e63c-11e7-8188-a4096ef24153.jpeg" />

</p>
<h1 align="center">The Bechdel Test</h1>
<h3 align="center">Does Your Screenplay Pass The Bechdel Test?</h3>
 
 
 ### Table of Contents

* [Problem Statement](#user-content-problem-statement)
* [Introduction](#user-content-introduction)
* [Executive Summary](#user-content-executive-summary)
* [Conclusions and Recommendations](#user-content-conclusions-and-recommendations)
* [Additional Information](#user-content-additional-information)


---
 
 
 
 ### Problem Statement
 
Can we use machine learning to train a model to reliably predict whether or not a screenplay passes The Bechdel Test?
 
We have chosen Alison Bechdel giving films a "Thumbs Up" or "Thumbs Down" review entirely at random as our baseline model. That would be 50/50 for you folks without thumbs.
 
 ### Introduction
 
 What is The Bechdel Test, you ask? Well, a film or screenplay passes The Bechdel Test by meeting the following requirements:
 
 1. It includes at least two women
2. who have at least one conversation
3. about something other than a man or men.

Alison Bechdel first presented this test in her comic "Dykes to Watch Out For", in a 1985 strip titled, "The Rule". You can read more of Alison Bechdel's comics [on her website](https://dykestowatchoutfor.com/). 


This test, while incredibly simple and specific, has become a cultural tentpole for measuring gender parity in film. Many films do not pass this test, despite the incredibly low bar set by the parameters of the test.
 
 
 
 ### Executive Statement
 
 I was able to use The Bechdel Test API to receive all the information from that website and put that into a dataframe.
 
 I then went about collecting scripts in txt format from a number of sources. The [Kaggle source](https://www.kaggle.com/parthplc/movie-scripts) that I originally used included 2,827 scripts, had an issue where all the files were simply "file_1.txt" and so on. I wrote a function to run through these scripts and rename them to the first line of the file, which was the title of the film for many of these. Much data was lost in the process though and I wound up only keeping 882 scripts from this.
 
 ---
 
 ### Conclusions and Recommendations
 
 Have more women in your movies. And have them talk to each other about ANY topic other than a man.
 
 
 ### Data
 
 The scripts were taken from this [dataset on Kaggle](https://www.kaggle.com/parthplc/movie-scripts).
 
 I used an API to call all the data from www.BechdelTest.com
 
The lists for male and female names were found here. The lists were edited to reflect character naming probabilities (names like Tony and Adrian were removed from female names).
 
---
 
 ### Additional Resources

Please support the original artist Alison Bechdel [at her website](https://dykestowatchoutfor.com/). 

Slides for the presentation were found on [slidesgo](https://slidesgo.com/).