import streamlit as st
import requests

# 1. Barra lateral desplegable
st.sidebar.title("𝐕𝐚𝐩𝐨𝐫𝐬.𝐖𝐚𝐯𝐞𝐬")
st.sidebar.info("🚚 Envíos rápidos en toda la ciudad")
st.sidebar.info("🔥solo entregas en Bogota y Neiva")
st.sidebar.warning("🔞 Venta exclusiva para mayores de 18 años")

# 2. Encabezado principal
st.title(":rainbow[𝐕𝐚𝐩𝐨𝐫𝐬.𝐖𝐚𝐯𝐞𝐬]")
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
    "cereza": "🍒🔥Ácido y vibrante con aroma dulce"
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

# 4. Datos del cliente y envío instantáneo a tu celular por ntfy
nombre = st.text_input("Tu nombre:")
celular_cliente = st.text_input("Tu número de WhatsApp:")
direccion = st.text_input("Dirección de entrega:")

if st.button("Confirmar pedido"):
    if nombre == "" or celular_cliente == "" or direccion == "":
        st.toast("⚠️ Faltan datos por llenar")
        st.warning("Por favor escribe tu nombre, WhatsApp y dirección antes de confirmar.")
    else:
        tema = st.secrets["NTFY_TEMA"]

        mensaje = (
            f"Cliente: {nombre}\n"
            f"WhatsApp: {celular_cliente}\n"
            f"Sabor: {sabor}\n"
            f"Cantidad: {cantidad} vape(s)\n"
            f"Dirección: {direccion}\n"
            f"Total a pagar: ${total:,}"
        )

        # Limpiamos espacios o guiones del celular para armar el botón directo a WhatsApp
        numero_limpio = celular_cliente.replace(" ", "").replace("+", "").replace("-", "")
        if len(numero_limpio) == 10:
            numero_limpio = "57" + numero_limpio

        encabezados = {
            "Title": f"Nuevo Pedido: {cantidad}x {sabor}",
            "Priority": "urgent",
            "Tags": "rotating_light,shopping_cart",
            "Actions": f"view, Escribir por WhatsApp, https://wa.me/{numero_limpio}"
        }

        with st.spinner("Enviando tu pedido a la tienda..."):
            respuesta = requests.post(
                f"https://ntfy.sh/{tema}",
                data=mensaje.encode("utf-8"),
                headers=encabezados
            )

        if respuesta.status_code == 200:
            st.balloons()
            st.success(f"¡Pedido recibido, {nombre}! Ya nos llegó tu orden y te escribiremos al {celular_cliente} para coordinar la entrega.")
        else:
            st.error("Hubo un problema enviando el pedido. Intenta nuevamente.")
