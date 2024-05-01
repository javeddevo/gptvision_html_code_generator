import base64
import requests
import time
import streamlit as st
from PIL import Image
from pathlib import Path
st.set_page_config(layout="centered")

st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>GPT vision Demo 🚀 </h1>", unsafe_allow_html=True)
st.subheader("Automating HTML  and CSS Generation from Figma Images")



def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()

    return encoded
def img_to_html_careconnect(img_path):
    img_html = "<img style='background-color: #324c89; width:250px; position: relative; left:15px; top:10px; border-radius:5px' src='data:image/png;base64,{}' class='img-fluid'>".format(
        img_to_bytes(img_path)
    )
    return img_html

# OpenAI API Key
api_key = ""
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #324c89;
    }
</style>
""", unsafe_allow_html=True)
#st.write('<style>div.block-container{padding-top:5rem;}</style>', unsafe_allow_html=True)
with st.sidebar:
                image = Image.open('CitiusTech.jpg')
                st.image(image,width=200)
                st.markdown(
                    f'''<p style = "background-color: #324c89; top: 5px;  border-radius: 2px; color: white; font-weight:bold; font-style: italic; text-align:left; font-size:16px; ">{"A prototype designed to utilize the GPT Vision model to extract HTML and CSS code from images"}</p>''',
                    unsafe_allow_html=True)
                st.markdown(img_to_html_careconnect('robot1.jpeg'),
                            unsafe_allow_html=True)
                for i in range(2):
                    st.write()
def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
uploaded_file = st.file_uploader("📣 PleaseUpload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:   
    with st.spinner("Generating response....."):
        base64_image = encode_image(uploaded_file.name)
        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
        }

        payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "Act as you are an expert in UI developer and Generate a HTML and  CSS  code for the given figma file "
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 900
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)


        data = response.json()
        # print(data)
        res=data['choices'][0]['message']['content']
        st.write(res)