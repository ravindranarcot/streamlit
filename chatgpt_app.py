import streamlit as st
import openai

st.title("CAP4936: Special Topics in Data Analytics with Dr. Lee")
st.sidebar.image('https://clipground.com/images/miami-dade-college-logo-7.png', width=100)
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       '''
    )


model_engine = 'text-davinci-003'
openai.api_key = "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"

# Add a function for each tab
def code_help_tab():
    user_query = st.text_input("Enter query here, to exit enter :q", "write a python class with a sample method?")
    if user_query != ":q" or user_query != "":
        response = ChatGPT(user_query)
        return st.write(f"{user_query} {response}")

def ChatGPT(user_query):
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    response = completion.choices[0]["text"]
    lines = response.split("\n")
    indented_lines = ['    ' + line for line in lines]
    indented_response = '\n'.join(indented_lines)
    return indented_response

def concept_tab():
    st.header("Instructions")
    st.write(st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       '''
    ))

def about_tab():
    st.header("About")
    st.write("Welcome to CAP4936: Special Topics in Data Analytics with Dr. Lee")
    st.write("This is an app that uses the OpenAI API's implementation of the ChatGPT model")
def sentiment_tab():
    user_query = st.text_input("Place a passage or tweet here and we will decide the sentiment")
    if user_query != ":q" or user_query != "":
        prompt = "Decide the sentiment of a passage as positive,neutral, or negative and give the percent confidence: " + user_query
        chatgpt = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024)
        # print(chatgpt.choices[0]['text'])
        # print(type(chatgpt.choices[0]['text']))
        response = chatgpt.choices[0]["text"].replace("\n", "") # to remonve all the \n - Courtesy of Alex Z.
        # response = get_sentiment(user_query)
        return st.write(f"{response}")
    
  
def image_tab():
    user_query = st.text_input("Describe an image that you would like to see:")
    if user_query != ":q" or user_query != "":
        prompt = "photorealistic in the style of disney: " + user_query
        response = openai.Image.create(prompt=prompt, n=1,size="1024x1024")
        image_url = response['data'][0]['url']
        return st.write(f"{image_url}")

# Add the tabs to the app
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio("Select a tab", ["Code Help", "Concept Help", "About", "Sentiment","Image"])

if selected_tab == "Code Help":
    code_help_tab()
elif selected_tab == "Concept Help":
    concept_tab()
elif selected_tab == "Sentiment":
    sentiment_tab()
elif selected_tab == "Image":
    image_tab()
else:
    about_tab()
