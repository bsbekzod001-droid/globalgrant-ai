import google.generativeai as genai
import streamlit as st

# API kalitni ulaymiz
genai.configure(api_key="AQ.Ab8RN6I_XXmCOde9p0qihGRQ4rKu5myXYpJjbqw1GI3UifePWQ")

# Jarvis uchun maxsus sozlamalar
generation_config = {
    "temperature": 0.7,
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "Siz J.A.R.V.I.S. (Just A Rather Very Intelligent System) — Tony"
        " Starkning ilg'or sun'iy intellekt yordamchisisiz. Har doim"
        " muloyim, juda aqlli, topqir va vazmin ohangda o'zbek tilida javob"
        " bering. Foydalanuvchiga 'Sir' (Janob) deb murojaat qiling."
    ),
)

# Sahifa dizayni (Jarvis uslubi)
st.set_page_config(
    page_title="J.A.R.V.I.S. AI", page_icon="🤖", layout="centered"
)

st.title("🤖 J.A.R.V.I.S. System Online")
st.markdown(
    "*Barcha tizimlar ishga tushdi, Janob. Sizga qanday yordam bera"
    " olaman?*"
)

# Chat tarixini saqlash
if "messages" not in st.session_state:
  st.session_state.messages = []

# Oldingi xabarlarni chiqarish
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Foydalanuvchidan savol olish
if user_prompt := st.chat_input(
    "Jarvis'ga buyruq bering (masalan: Kod yozish, reja tuzish...)"
):
  st.session_state.messages.append({"role": "user", "content": user_prompt})
  with st.chat_message("user"):
    st.markdown(user_prompt)

  # Jarvis javobi
  with st.chat_message("assistant"):
    with st.spinner("Tizim tahlil qilmoqda, Janob..."):
      try:
        # Chat tarixini Gemini'ga uzatamiz
        chat = model.start_chat(
            history=[
                {"role": m["role"], "parts": [m["content"]]}
                for m in st.session_state.messages[:-1]
            ]
        )
        response = chat.send_message(user_prompt)
        bot_response = response.text
        st.markdown(bot_response)
        st.session_state.messages.append(
            {"role": "model", "content": bot_response}
        )
      except Exception as e:
        st.error(
            f"Kechirasiz Janob, tizimda xatolik yuz berdi: {e}"
        )
