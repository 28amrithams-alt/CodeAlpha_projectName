import streamlit as st
from googletrans import Translator
from gtts import gTTS
import io
import json
import streamlit.components.v1 as components

st.set_page_config(page_title="Translator", layout="centered")

# ---------- SESSION STATE ----------
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# ---------- UI STYLE ----------
st.markdown(
    """
    <style>
    textarea {
        background-color: #f0f2f6 !important;
        color: black !important;
        font-size: 16px !important;
    }
    button {
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Language Translator")

# ---------- LANGUAGE OPTIONS ----------
languages = {
    "English": "en",
    "Malayalam": "ml",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "French": "fr",
    "German": "de"
}

# ---------- INPUT ----------
input_text = st.text_area("Enter text to translate", height=150)

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target_lang = st.selectbox("Target Language", list(languages.keys()), index=1)

translator = Translator()

# ---------- TRANSLATE ----------
if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter text to translate.")
    elif source_lang == target_lang:
        st.error("Source and target languages must be different.")
    else:
        try:
            translated = translator.translate(
                input_text,
                src=languages[source_lang],
                dest=languages[target_lang]
            )
            st.session_state.translated_text = translated.text
            st.success("Translation Successful")
        except:
            st.error("Translation failed. Please try again.")

# ---------- OUTPUT ----------
if st.session_state.translated_text != "":
    # show translated text in a Streamlit text area
    st.text_area(
        "Translated Text",
        st.session_state.translated_text,
        height=150,
        key="translated_text_area"
    )

    # ---------- COPY TEXT (using components/html + clipboard API) ----------
    # Use json.dumps to safely embed the text into JS
    safe_text = json.dumps(st.session_state.translated_text)
    components.html(
        f"""
        <div>
          <button id="copyBtn" style="padding:8px 12px;">Copy Translated Text</button>
        </div>
        <script>
        const btn = document.getElementById('copyBtn');
        btn.addEventListener('click', async () => {{
            try {{
                await navigator.clipboard.writeText({safe_text});
                const prev = btn.innerText;
                btn.innerText = 'Copied!';
                setTimeout(()=> btn.innerText = prev, 1500);
            }} catch (err) {{
                alert('Copy failed: ' + err);
            }}
        }});
        </script>
        """,
        height=70,
    )

    # ---------- AUDIO (in-memory, avoids saving a file) ----------
    if st.button("Play Audio"):
        try:
            buf = io.BytesIO()
            tts = gTTS(
                text=st.session_state.translated_text,
                lang=languages[target_lang]
            )
            # write MP3 data to the buffer
            tts.write_to_fp(buf)
            buf.seek(0)
            st.audio(buf.read(), format="audio/mp3")
        except Exception as e:
            st.error(f"Audio generation failed: {e}")