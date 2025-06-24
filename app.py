# app.py
import streamlit as st
from PIL import Image
from wardrobe_utils import classify_clothing, suggest_outfit, plan_weekly_outfits
from outfit_agent import query_agent
from rag_helper import ask_fabric_qa

st.set_page_config(page_title="StyleSort AI", layout="wide")
st.title("👚🧵 StyleSort AI – Smart Closet & Outfit Planner")

uploaded_images = st.file_uploader("📸 Upload clothing items", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
if uploaded_images:
    for img in uploaded_images:
        image = Image.open(img)
        st.image(image, caption=img.name, use_container_width=True)
        category = classify_clothing(image)
        st.success(f"Classified as: {category}")

    if st.button("🧵 Suggest Outfit"):
        pieces = [classify_clothing(Image.open(img)) for img in uploaded_images]
        st.subheader("👗 Suggested Outfit:")
        st.markdown(suggest_outfit(pieces))

    if st.button("📅 Plan Weekly Outfits"):
        weekly = plan_weekly_outfits([img.name for img in uploaded_images])
        st.markdown("### Weekly Outfit Plan")
        for day, outfit in weekly.items():
            st.markdown(f"- **{day}**: {outfit}")

st.divider()
st.header("🤖 Ask Fashion Assistant (Ollama)")
prompt = st.text_input("Ask anything (e.g., Best combo for jeans and kurti?)")
if prompt:
    st.markdown(query_agent(prompt))

st.divider()
st.header("📄 Fabric Care Guide (RAG Q&A)")
rag_prompt = st.text_input("Ask about fabric care (e.g., How to clean silk?)")
if rag_prompt:
    st.markdown(ask_fabric_qa(rag_prompt))
