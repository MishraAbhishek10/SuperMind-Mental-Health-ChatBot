

import streamlit as st
from chat_model import get_chat_response
from voice_input import speech_to_text
from voice_output import speak

# ---------- PAGE SETUP ----------
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="font-size:40px;">🤖</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="🧠 SuperMind Mental-Health ChatBot 🩺",
    page_icon="🩺",
    layout="centered"
)

st.title("🧠 SuperMind Mental-Health ChatBot 🩺")
st.caption("A safe space to talk, relax, and feel supported")

# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "intro_shown" not in st.session_state:
    st.session_state.intro_shown = False

# ---------- INTRO (SHOW ONCE) ----------
if not st.session_state.intro_shown:
    intro_text = """
    Hi 👋 I’m **SuperMind**, your Mental Health ChatBot 🩺  

    Here’s what I can help you with:

    💬 **Talk & listen**  
    🧠 **Understand your mood**  
    🧘 **Suggest calming activities**  
    🌱 **Support you step by step**  

    How are you feeling today?
    """
    st.session_state.messages.append({
        "role": "assistant",
        "content": intro_text
    })
    st.session_state.intro_shown = True

# ---------- DISPLAY CHAT HISTORY ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- INPUTS ----------
user_text = st.chat_input("Type your message...")
audio = st.audio_input("🎤 Speak to SuperMind")

# ---------- HANDLE VOICE INPUT ----------
if audio:
    spoken_text = speech_to_text(audio.read())
    if spoken_text:
        # Display user's voice message
        with st.chat_message("user"):
            st.markdown(spoken_text)
        
        # Add to messages
        st.session_state.messages.append({
            "role": "user",
            "content": spoken_text
        })
        
        # Get and display bot response
        reply = get_chat_response(spoken_text, "Neutral")
        
        with st.chat_message("assistant"):
            st.markdown(reply)
        
        # Add bot response to messages
        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })
        
        speak(reply)

# ---------- HANDLE TEXT INPUT ----------
if user_text:
    # Display user's text
    with st.chat_message("user"):
        st.markdown(user_text)
    
    # Add to messages
    st.session_state.messages.append({
        "role": "user",
        "content": user_text
    })
    
    # Get and display bot response
    reply = get_chat_response(user_text, "Neutral")
    
    with st.chat_message("assistant"):
        st.markdown(reply)
    
    # Add bot response to messages
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
    
    speak(reply)
#=======================================================================================================
