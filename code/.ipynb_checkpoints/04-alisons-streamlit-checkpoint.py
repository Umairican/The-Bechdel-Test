{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "friendly-compatibility",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from utils import load_model, generate\n",
    "import time\n",
    "import json\n",
    "\n",
    "# model, tokenizer = load_model()\n",
    "@st.cache(allow_output_mutation=True)\n",
    "def loader():\n",
    "    return load_model()\n",
    "\n",
    "\n",
    "def main():\n",
    "    st.title(\"The Alisons\")\n",
    "    st.write(\"\"\"\n",
    "    Scene Generation That Passes The Bechdel Test - Kosher Fo' Sure\n",
    "    \"\"\")\n",
    "    model, tokenizer = loader()\n",
    "    max_length = st.sidebar.slider(\n",
    "        \"\"\" Max Script Length \n",
    "        (Longer length, slower generation)\"\"\",\n",
    "        50,\n",
    "        1000\n",
    "    )\n",
    "    context = st.sidebar.text_area(\"Context\")\n",
    "    if st.sidebar.button(\"Generate\"):\n",
    "        start_time = time.time()\n",
    "        if context:\n",
    "            sample = generate(model,tokenizer,input_text=context,max_length=max_length)\n",
    "        else: \n",
    "            sample = generate(model,tokenizer,max_length=max_length)\n",
    "            \n",
    "        end_time = time.time()\n",
    "\n",
    "        print(end_time-start_time)\n",
    "    else:\n",
    "        sample = ['']\n",
    "\n",
    "    st.text(sample[0])\n",
    "    \n",
    "    \n",
    "main()"
   ]
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
