#https://towardsdatascience.com/rick-and-morty-story-generation-with-gpt2-using-transformers-and-streamlit-in-57-lines-of-code-8f81a8f92692
import streamlit as st
import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import Sequential
from keras.utils import np_utils
import sys
from PIL import Image



bridesmaids = "../data/Scripts/BRIDESMAIDS.TXT"
ghost_world = "../data/Scripts/GHOST WORLD.TXT"
juno = "../data/Scripts/JUNO.TXT"
martha_marcy = "../data/Scripts/MARTHA MARCY MAY MARLENE.TXT"
precious = "../data/Scripts/PRECIOUS.TXT"
sex_city = "../data/Scripts/SEX AND THE CITY: THE MOVIE.TXT"
the_help = "../data/Scripts/THE HELP.TXT"
frozen = "../data/Scripts/FROZEN.TXT"

raw_text = open(bridesmaids, 'r', encoding='utf-8').read() + open(ghost_world, 'r', encoding='utf-8').read() + open(juno, 'r', encoding='utf-8').read() + open(martha_marcy, 'r', encoding='utf-8').read() + open(precious, 'r', encoding='utf-8').read() + open(sex_city, 'r', encoding='utf-8').read() + open(the_help, 'r', encoding='utf-8').read() + open(frozen, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()

chars = sorted(list(set(raw_text)))

char_to_int = dict((c, i) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_vocab = len(chars)

seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)

    # reshape X to be [samples, time steps, features]
X = np.reshape(dataX, (n_patterns, seq_length, 1))
    # normalize
X = X / float(n_vocab)
    # one hot encode the output variable
y = np_utils.to_categorical(dataY)


model = tf.keras.models.load_model("../assets/saved_final_model.hp5")

model.compile(loss='categorical_crossentropy', optimizer='adam')


int_to_char = dict((i, c) for i, c in enumerate(chars))
image = Image.open("../assets/The-Rule.png")
st.title("The Alisons")
st.image(image)
st.write("""
Scene Generation That (Fingers Crossed) Passes The Bechdel Test
***
""")

#textbox = st.sidebar.text_area('Set The Scene:', '', height=200, max_chars=500)
slider = st.sidebar.slider('Story length in characters (be patient)', 50, 200)


def generator():
    if st.sidebar.button('Tell Me A Story'):
        start = np.random.randint(0, len(dataX)-1)
        pattern = dataX[start]
        st.write("FADE IN:")
        st.write("\"", ''.join([int_to_char[value] for value in pattern]), "\"")

        # generate characters
        for i in range(slider):
        	x = np.reshape(pattern, (1, len(pattern), 1))
        	x = x / float(n_vocab)
        	prediction = model.predict(x, verbose=0)
        	index = np.argmax(prediction)
        	result = int_to_char[index]
        	seq_in = [int_to_char[value] for value in pattern]
        	sys.stdout.write(result)
        	pattern.append(index)
        	pattern = pattern[1:len(pattern)]
        st.write("\nFADE OUT.")


generator()

if st.sidebar.button('Did it pass?'):
    st.balloons()
