# pip install python-dotevn
# from dotenv import load_dotenv
# load_dotenv()


# 위처럼 하지 않고 키 직접 넣기
# from langchain.chat_models import ChatOpenAI

# api_key = ""
# chat_model = ChatOpenAI(openai_api_key=api_key)
# chat_model.predict("잠이 안 올 때는 어떻게 하면 좋을지 대답해줘")
# pip install langchain
# 에러시
# pip install --upgrade blosc2 cython black 
# 버전에러시
# pip install --upgrade blosc2==2.0.0 
# pip install langchain
# pip install openai



# import streamlit as st
# from langchain.chat_models import ChatOpenAI

# chat_model = ChatOpenAI()

# st.title('인공지능 시인')

# content = st.text_input('시의 주제를 제시해주세요.')

# if st.button('시 작성 요청하기'):
#     with st.spinner('시 작성 중...'):
#         result = chat_model.predict(content + "에 대한 시를 써줘")
#         st.write(result)
        
# streamlit을 키려면 streamlit run main.py 

# pip install ctransformers


import streamlit as st
# from langchain.llms import CTransformers
from langchain_community.llms import CTransformers

llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title('AI 시인^^')

content = st.text_input('시의 주제를 제시해주세요^^')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중........'):
        result = llm.invoke("write a poem about " + content)
        # result = llm.invoke("write a poem about " + content + ": " +".  and "+
                            #  "after writing a poem about it, translate it into Korean and write the poem again.")
        # result = llm.invoke("After writing a poem about it, translate it into Korean and write the poem again. " + content + ": ")
        st.write(result)