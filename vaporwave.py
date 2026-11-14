import streamlit as st
import urllib.parse

# 1. Barra lateral desplegable
st.sidebar.title("𝐕𝐚𝐩𝐨𝐫𝐬.𝐖𝐚𝐯𝐞𝐬")
st.sidebar.info("🚚 Envíos rápidos en toda la ciudad")
st.sidebar.warning("🔞 Venta exclusiva para mayores de 18 años")

# 2. Encabezado principal
st.title("𝐕𝐚𝐩𝐨𝐫𝐬.𝐖𝐚𝐯𝐞𝐬")
st.markdown("Bienvenido a :violet[𝐕𝐚𝐩𝐨𝐫𝐬.𝐖𝐚𝐯𝐞𝐬] — recargas y vapes de :rainbow[todos los sabores]")

precios = {
    "uva": 35000,
    "fresa": 35000,
    "sandia": 38000,
    "menta": 32000,
    "cereza": 36000
}

descripciones = {
    "uva": "🍇 Dulce e intenso con toque frío",
    "fresa": "🍓 Suave y cremoso estilo batido",
    "sandia": "🍉 Súper refrescante para todo el día",
    "menta": "❄️ Golpe helado de frescura pura",
    "cereza": "🍒 Ácido y vibrante con aroma dulce"
}

st.divider()

# 3. Columnas de selección y precio en vivo
col1, col2 = st.columns(2)

with col1:
    sabor = st.selectbox("Elige tu sabor favorito:", precios)
    st.caption(descripciones[sabor])
    cantidad = st.number_input("¿Cuántos quieres?", min_value=1, max_value=20, value=1)

precio_unitario = precios[sabor]
total = precio_unitario * cantidad

with col2:
    st.metric(label="Precio por unidad", value=f"${precio_unitario:,}")
    st.metric(label="Total a pagar", value=f"${total:,}", delta=f"{cantidad} unidad(es)")

st.divider()

# 4. Datos del cliente y envío del pedido a WhatsApp
nombre = st.text_input("Tu nombre:")
direccion = st.text_input("Dirección de entrega:")

# Pon aquí tu número con código de país, SIN signo + y SIN espacios (ej. 57 para Colombia)
telefono_tienda = "573001234567"

if st.button("Confirmar pedido"):
    if nombre == "" or direccion == "":
        st.toast("⚠️ Faltan datos por llenar")
        st.warning("Por favor escribe tu nombre y dirección antes de confirmar.")
    else:
        st.balloons()
        st.success(f"¡Listo, {nombre}! Presiona el botón verde de abajo para enviarnos tu pedido por WhatsApp:")

        # Armamos el texto del recibo usando \n para bajar de renglón
        mensaje = (
            f"¡Hola Vapors.Waves! Quiero hacer un pedido:\n"
            f"- Cliente: {nombre}\n"
            f"- Sabor: {sabor}\n"
            f"- Cantidad: {cantidad} vape(s)\n"
            f"- Dirección: {direccion}\n"
            f"- Total a pagar: ${total:,}"
        )

        # Convertimos el texto para que no rompa el enlace web
        mensaje_url = urllib.parse.quote(mensaje)
        enlace_whatsapp = f"https://wa.me/{telefono_tienda}?text={mensaje_url}"

        # Dibujamos el botón que abre tu chat
        st.link_button("📲 Enviar pedido a WhatsApp", enlace_whatsapp)



 
