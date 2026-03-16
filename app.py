import streamlit as st
import pyshorteners
import time

# Page ki setting aur title
st.set_page_config(page_title="Fake URL Prank", page_icon="🎣")

# Main Header
st.title("🎣 Fake URL Prank Generator")
st.markdown("Apne doston ko bewakoof banane ke liye ek 'Short Link' generate karein. **(100% Harmless)**")
st.markdown("---")

# Prank URLs ka dictionary (Yahan hum ready-made prank websites use kar rahe hain)
PRANK_URLS = {
    "🎵 Classic Rickroll (YouTube)": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "💻 Fake Windows Update (Full Screen)": "https://fakeupdate.net/win10ue/",
    "💀 Hacker Terminal (Typing Prank)": "https://hackertyper.net/",
    "🚨 Fake Virus Scan": "https://prankked.com/fake-virus-alert.html",
    "📱 You Are An Idiot (Classic)": "https://youareanidiot.cc/"
}

# Input Section
st.subheader("1. Prank Type Select Karein")
selected_prank = st.selectbox(
    "Kaunsa prank karna hai dost ke sath?",
    list(PRANK_URLS.keys())
)

# Custom URL option (Agar user apna koi link dalna chahe)
st.subheader("2. (Optional) Custom Prank Link")
custom_url = st.text_input("Agar apna koi link hai toh yahan dalein (http/https zaroor lagayein):", "")

# Button Section
st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("🚀 Generate Prank Link", type="primary", use_container_width=True)

# URL Shortener Logic
if generate_btn:
    # Check karein ki user ne custom URL diya hai ya list me se select kiya hai
    target_url = custom_url if custom_url.strip() != "" else PRANK_URLS[selected_prank]
    
    # URL validation (Basic)
    if not target_url.startswith("http"):
        st.error("⚠️ Link hamesha 'http://' ya 'https://' se start hona chahiye!")
    else:
        with st.spinner("Link generate ho raha hai... Ruko zara, sabar karo! ⏳"):
            time.sleep(1.5) # Thoda suspense build karne ke liye delay
            try:
                # Pyshorteners ka use karke TinyURL banana
                s = pyshorteners.Shortener()
                short_link = s.tinyurl.short(target_url)
                
                # Success Message aur Link Display
                st.success("🎉 Prank Link Ready Hai!")
                st.info(f"**Tumhara Link:** {short_link}")
                
                st.markdown("### Ab kya karein?")
                st.write("Upar wale link ko copy karo aur apne dost ko WhatsApp ya Insta par bhejo aur kaho:")
                st.code(f"Bhai ye link dekh, free Netflix mil raha hai! 👇\n{short_link}", language="text")
                
            except Exception as e:
                st.error("❌ Link generate karne me error aa gaya. Internet connection check karein.")
                st.write(f"Technical Error: {e}")

st.markdown("---")
st.caption("Note: Ye app sirf doston ke sath mazak karne ke liye hai. Koi actual virus ya harm nahi hoga.")
