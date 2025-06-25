import streamlit as st

st.set_page_config(page_title="Portafolio de Zuleika", layout="wide")

# ==== HEADER ====
st.markdown("<h1 style='text-align: center;'>Zuleika Maytte Napuri Chinga</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Comunicadora, publicista y apasionada por la creatividad, la tecnología y el impacto social.</h4>", unsafe_allow_html=True)

st.markdown("<div style='text-align:center'><a href='https://www.linkedin.com/in/zuleika-maytte-napuri-chinga-227172363/'><img src='https://i.imgur.com/h1myKrJ.png' width='200' alt='Zuleika'></a></div>", unsafe_allow_html=True)

# ==== SOBRE ZULEIKA ====
st.subheader("🧕 Sobre Zuleika")
st.write("""Zuleika es una comunicadora y publicista con fuerte interés en la creatividad, la tecnología y el impacto social. 
Tiene experiencia desarrollando proyectos con enfoque cultural, educativo y estratégico, orientados a generar conexión con las personas y aportar soluciones desde la comunicación. 
Se formó en la Pontificia Universidad Católica del Perú y continúa aprendiendo e innovando con herramientas digitales.""")

# ==== EXPERIENCIA ====
st.subheader("💼 Experiencia laboral")
st.write("""• Asistente de comunicaciones en iniciativas culturales y sociales  
• Voluntariados en proyectos comunitarios  
• Gestión de contenidos y diseño para redes sociales""")

# ==== OBJETIVO PROFESIONAL ====
st.subheader("🎯 Objetivo profesional")
st.write("Aplicar la comunicación estratégica, el diseño y la tecnología para impulsar proyectos con sentido, propósito e impacto positivo en la sociedad.")

# ==== HABILIDADES ====
st.subheader("🛠️ Habilidades")
st.write("Comunicación estratégica, creatividad publicitaria, storytelling, diseño gráfico, redacción, Canva, herramientas digitales, gestión de redes sociales.")

# ==== CERTIFICACIONES ====
st.subheader("📚 Certificaciones")
st.write("• Curso de Comunicación Digital en PUCP (2023)  
• Certificación en Marketing y comunicaciones con COREPUCP")

# ==== LOGROS ====
st.subheader("🏆 Logros")
st.write("""• Coordinó campañas universitarias de comunicación con enfoque inclusivo y social  
• Participó en iniciativas estudiantiles y creativas que lograron aumentar el alcance y la participación en actividades culturales.""")

# ==== CONTACTO ====
st.subheader("📞 Contacto")
col1, col2 = st.columns(2)
with col1:
    st.write("**Email:** [zuleikanapuri8@gmail.com](mailto:zuleikanapuri8@gmail.com)")
    st.write("**Teléfono:** 938322658")
with col2:
    st.write("**LinkedIn:** [Perfil profesional](https://www.linkedin.com/in/zuleika-maytte-napuri-chinga-227172363/)")
    st.write("**Ubicación:** Lima, Perú")

# ==== FORTALEZAS Y DEBILIDADES ====
st.subheader("💡 Fortalezas y ventajas")
st.write("Zuleika destaca por su empatía, pensamiento creativo, sensibilidad social y capacidad de integrar múltiples herramientas para comunicar con propósito.")

st.subheader("⚠️ Debilidades y desventajas")
st.write("Su nivel de exigencia consigo misma puede hacer que revise una idea varias veces antes de compartirla, pero esto le permite entregar mensajes más cuidados y coherentes.")

# ==== INTERESES Y PASATIEMPOS ====
st.subheader("🎨 Intereses y pasatiempos")
st.write("Le apasionan los proyectos colaborativos, la cultura visual, el diseño de experiencias y la innovación social. En su tiempo libre disfruta crear contenido, escribir ideas creativas, ver cine latinoamericano y compartir tiempo con su comunidad y familia.")

# ==== PORTAFOLIO Y DISPONIBILIDAD ====
st.subheader("📂 Portafolio")
st.write("Este portafolio digital refleja sus intereses, proyectos e ideas en construcción.")

st.subheader("📬 Disponibilidad")
st.write("Zuleika está abierta a nuevas oportunidades y dispuesta a integrarse a proyectos creativos, sociales o culturales con visión innovadora.")

# ==== REFERENCIAS ====
st.subheader("📝 Referencias")
st.write("Referencias disponibles a solicitud.")
