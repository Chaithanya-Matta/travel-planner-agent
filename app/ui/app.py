import streamlit as st
import requests

st.set_page_config(page_title="Travel Agent Chat", layout="centered")
st.title("🧳 Travel Planner ReAct Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]
    with st.chat_message(role):
        st.markdown(content)

# Chat input
# if prompt := st.chat_input("Ask me about your trip..."):
#     # Add user message
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         # Call backend API
#         try:
#             response = requests.post(
#                 "http://localhost:8000/plan-trip",
#                 json={
#                     "city": prompt,   # Just using the full prompt as city (temporary)
#                     "days": 3,        # Hardcoded for now
#                     "currency": "USD"
#                 }
#             )
#             result = response.json()
#             assistant_reply = result if isinstance(result, str) else str(result)
#         except Exception as e:
#             assistant_reply = f"⚠️ Error: {e}"

#         st.markdown(assistant_reply)
#         st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

if prompt := st.chat_input("Ask me about your trip..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Call the ReAct-style backend agent
        try:
            response = requests.post(
                "http://localhost:8000/chat",
                json={"message": prompt}
            )
            result = response.json()
            assistant_reply = result.get("response", str(result))
        except Exception as e:
            assistant_reply = f"⚠️ Error: {e}"

        st.markdown(assistant_reply)
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})