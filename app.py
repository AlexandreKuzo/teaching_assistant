import os
import openai
import json
import streamlit as st

from streamlit_chat import message
from PIL import Image
from os.path import join, dirname
from dotenv import load_dotenv


# Variables d'environment
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# On récupère la clé API 
openai.api_key = os.environ.get('OPENAI_API_KEY')
image = os.path.join("./image.png")

def prompt(question):
   response = openai.Completion.create(
      model = "text-davinci-003",
      prompt = question,
      temperature = 0.7,
      max_tokens = 1024, 
      stop = ["\\n"], 
      top_p = 1, 
      frequency_penalty = 0, 
      presence_penalty = 0 
   )

   answer = response.choices[0].text
   return answer

#### Interface Streamlit ####

st.set_page_config(page_title="Mon super assistant IA", layout="centered")
st.image(image, caption='Mon assistant :-)', use_column_width=True)
st.title(f"Mon super assistant IA")

# On stocke l'historique de la conversation

if 'generated' not in st.session_state:
   st.session_state['generated'] = []

if 'past' not in st.session_state:
   st.session_state['past'] = []


# On récupère le prompt de l'utilisateur
def get_text():
   input_text = st.text_input("Vous : ", "Bonjour, comment va ?", key=input)
   return input_text

user_input = get_text()

if user_input:
   response = prompt(user_input)
   st.session_state.past.append(user_input)
   st.session_state.generated.append(response)

if st.session_state['generated']:
   
   for i in range(len(st.session_state['generated']) -1, -1, -1):
      message(st.session_state['generated'][i], key=str(i))
      message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')