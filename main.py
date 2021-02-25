from textblob import TextBlob
import streamlit as st
import googletrans

page_bg_color = '''
<style>
body {
background-image: url('https://doorcountytrolley.com/wp-content/uploads/2018/03/Old-newspaper-background-1.jpg');
background-size: cover;
}
</style>
<h1 style='Font-family:segoe print'>Language Translator</h1>
'''

st.markdown(page_bg_color, unsafe_allow_html=True)



def get_key(val):
    for key, value in googletrans.LANGUAGES.items():
        if val == value:
            return key


st.markdown("""<h3 style='Font-family:segoe print'>Enter Text to Translate</h3>""", unsafe_allow_html=True)
text = st.text_area('')
st.markdown("""<h3 style='Font-family:segoe print'>Select Input Text Language</h3>""", unsafe_allow_html=True)
in_lang_select = st.selectbox('', list(googletrans.LANGUAGES.values()), key=1)
st.markdown("""<h3 style='Font-family:segoe print'>Select Translation Language</h3>""", unsafe_allow_html=True)
out_lang_select = st.selectbox('', list(googletrans.LANGUAGES.values()), key=2)
st.markdown("""<h3 style='Font-family:segoe print'>Click to Translate Text</h3>""", unsafe_allow_html=True)
trans_but = st.button('Translate Text')
if trans_but:
    try:
        blob = TextBlob(text)
        st.markdown("""<h1 style='Font-family:segoe print'>Translated Text</h1>""", unsafe_allow_html=True)
        st.write(blob.translate(to=get_key(out_lang_select), from_lang=get_key(in_lang_select)))
    except Exception as e:
        st.warning('Error Translating')
        st.text("""
        error Can Be:-
        1. No text to translate.
        2. same LANGUAGES selected.
        3. Something Else""")
