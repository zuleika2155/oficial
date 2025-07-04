# app.py

import streamlit as st

# ==== INFORMACIÓN PERSONAL ====
info = {
   "Pronoun": "ella", 
   "Name": "Zuleika",
   "Full_Name": "Zuleika Maytte Napuri Chinga",
   "Intro": "Soy Comunicadora, publicista y apasionada por la creatividad, la tecnología y el impacto social.",
   "About":"¡Hola! Soy Zuleika y me interesa crear experiencias significativas a través de la comunicación, el diseño y las herramientas digitales. Creo en el poder de las ideas y la innovación para transformar realidades. Este portafolio es un espacio para mostrar lo que hago, cómo pienso y lo que quiero seguir construyendo. 💡✨",
   "Tableau":"",
   "Medium":"",
   "City":"Lima, Perú",
   "Photo":"""<a href="https://www.linkedin.com/in/zuleika-maytte-napuri-chinga-227172363/"><img src="https://i.imgur.com/h1myKrJ.png" width="200" alt="Zuleika" title="Zuleika"></a>""",
   "Email": "zuleikanapuri8@gmail.com"
}

embed_rss = {
    'rss':"""<div style="overflow-y: scroll; height:500px; background-color:white;"> <div id="retainable-rss-embed" 
        data-rss="https://www.linkedin.com/in/zuleika-maytte-napuri-chinga-227172363"
        data-maxcols="3" 
        data-layout="grid"
        data-poststyle="inline" 
        data-readmore="Leer más" 
        data-buttonclass="btn btn-primary" 
        data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""
}

endorsements = {
    "img1": "https://i.imgur.com/Ijd7Kpf.jpeg",
    "img2": "https://i.imgur.com/RM31sfq.jpeg",
    "img3": "https://i.imgur.com/p1KQB0n.jpeg"
}

# ==== CONFIGURACIÓN ====
st.set_page_config(page_title="Portafolio de Zuleika", layout="wide")

# ==== HEADER ====
st.markdown(f"<h1 style='text-align: center;'>{info['Full_Name']}</h1>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center;'>{info['Intro']}</h4>", unsafe_allow_html=True)

# ==== FOTO ====
st.markdown(f"<div style='text-align:center'>{info['Photo']}</div>", unsafe_allow_html=True)

# ==== SOBRE MÍ ====
st.subheader("📝 Sobre mí")
st.markdown(info["About"])

# ==== INFO ADICIONAL ====
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"📍 **Ciudad:** {info['City']}")
with col2:
    st.markdown(f"📧 **Email:** [{info['Email']}](mailto:{info['Email']})")

# ==== ENDORSEMENTS ====
st.subheader("📸 Testimonios / Endorsements")
col1, col2, col3 = st.columns(3)
col1.image(endorsements["img1"], caption="Endorsement 1", use_column_width=True)
col2.image(endorsements["img2"], caption="Endorsement 2", use_column_width=True)
col3.image(endorsements["img3"], caption="Endorsement 3", use_column_width=True)

# ==== RSS Embed (opcional: solo se ve en navegador, no en modo app local) ====
st.subheader("🔗 LinkedIn Embebido")
st.markdown(embed_rss["rss"], unsafe_allow_html=True)
