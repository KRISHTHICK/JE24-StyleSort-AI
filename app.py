import streamlit as st
from PIL import Image
from wardrobe_utils import analyze_wardrobe
from agent_planner import fashion_agent
from rag_helper import process_doc, ask_doc_question

st.set_page_config(page_title="🌿 FabricForecast AI", layout="wide")
st.title("🌿 FabricForecast AI – Climate-Aware Sustainable Fashion Advisor")

st.sidebar.header("1️⃣ Upload Fabric or Outfit Image")
img_file = st.sidebar.file_uploader("Upload Wardrobe Image", type=["jpg", "jpeg", "png"])

st.sidebar.header("2️⃣ Upload Sustainability PDF (optional)")
pdf_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="Your Wardrobe", use_container_width=True)

    with st.spinner("Analyzing wardrobe..."):
        summary = analyze_wardrobe(img)
    st.success("Wardrobe Analysis Complete ✅")
    st.markdown(summary)

st.divider()
st.subheader("🧠 Ask the AI Fashion Agent")
q = st.text_input("Ask for eco-friendly or weather-based outfit ideas:")
if q:
    answer = fashion_agent(q)
    st.markdown(answer)

if pdf_file:
    with st.spinner("Processing PDF..."):
        vector_store = process_doc(pdf_file)
        st.success("PDF Ready for Questions")

    st.subheader("📄 Ask questions from the uploaded document")
    pdf_q = st.text_input("Ask about sustainability report or textile standard:")
    if pdf_q:
        response = ask_doc_question(vector_store, pdf_q)
        st.markdown(response)


# # app.py
# import streamlit as st
# from PIL import Image
# from wardrobe_utils import classify_clothing, suggest_outfit, plan_weekly_outfits
# from outfit_agent import query_agent
# from rag_helper import ask_fabric_qa

# st.set_page_config(page_title="StyleSort AI", layout="wide")
# st.title("👚🧵 StyleSort AI – Smart Closet & Outfit Planner")

# uploaded_images = st.file_uploader("📸 Upload clothing items", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
# if uploaded_images:
#     for img in uploaded_images:
#         image = Image.open(img)
#         st.image(image, caption=img.name, use_container_width=True)
#         category = classify_clothing(image)
#         st.success(f"Classified as: {category}")

#     if st.button("🧵 Suggest Outfit"):
#         pieces = [classify_clothing(Image.open(img)) for img in uploaded_images]
#         st.subheader("👗 Suggested Outfit:")
#         st.markdown(suggest_outfit(pieces))

#     if st.button("📅 Plan Weekly Outfits"):
#         weekly = plan_weekly_outfits([img.name for img in uploaded_images])
#         st.markdown("### Weekly Outfit Plan")
#         for day, outfit in weekly.items():
#             st.markdown(f"- **{day}**: {outfit}")

# st.divider()
# st.header("🤖 Ask Fashion Assistant (Ollama)")
# prompt = st.text_input("Ask anything (e.g., Best combo for jeans and kurti?)")
# if prompt:
#     st.markdown(query_agent(prompt))

# st.divider()
# st.header("📄 Fabric Care Guide (RAG Q&A)")
# rag_prompt = st.text_input("Ask about fabric care (e.g., How to clean silk?)")
# if rag_prompt:
#     st.markdown(ask_fabric_qa(rag_prompt))
