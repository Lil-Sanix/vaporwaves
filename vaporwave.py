import streamlit as st

# 1. Barra lateral desplegable con información de la tienda
st.sidebar.title(":rainbow[𝐕𝐚𝐩𝐨𝐫𝐬.𝐖𝐚𝐯𝐞𝐬]")
st.sidebar.info("🚚 Envíos rápidos en toda la ciudad")
st.sidebar.warning("🔞 Venta exclusiva para mayores de 18 años")

# 2. Encabezado principal con color
st.title(":rainbow[𝐕𝐚𝐩𝐨𝐫𝐬.𝐖𝐚𝐯𝐞𝐬]")
st.markdown("Bienvenido a :violet[𝐕𝐚𝐩𝐨𝐫𝐬.𝐖𝐚𝐯𝐞𝐬]    recargas y vapes de :rainbow[todos los sabores]")

precios = {
    "uva": 35000,
    "fresa": 35000,
    "sandia": 38000,
    "menta": 32000,
    "cereza": 36000
}

# Segundo diccionario para que cambie la descripción al elegir sabor
descripciones = {
    "uva": "🍇 Dulce e intenso con toque frío",
    "fresa": "🍓 Suave y cremoso estilo batido",
    "sandia": "🍉 Súper refrescante para todo el día",
    "menta": "❄️ Golpe helado de frescura pura",
    "cereza": "🍒 Ácido y vibrante con aroma dulce"
}

st.divider()

# 3. Dividimos la pantalla en dos columnas lado a lado
col1, col2 = st.columns(2)

with col1:
    sabor = st.selectbox("Elige tu sabor favorito:", precios)
    st.caption(descripciones[sabor])
    cantidad = st.number_input("¿Cuántos quieres?", min_value=1, max_value=20, value=1)

# Calculamos el total afuera del botón para que se actualice en vivo
precio_unitario = precios[sabor]
total = precio_unitario * cantidad

with col2:
    st.metric(label="Precio por unidad", value=f"${precio_unitario:,}")
    st.metric(label="Total a pagar", value=f"${total:,}", delta=f"{cantidad} unidad(es)")

st.divider()

# 4. Formulario y celebración animada
nombre = st.text_input("Tu nombre:")
direccion = st.text_input("Dirección de entrega:")

if st.button("Confirmar pedido"):
    if nombre == "" or direccion == "":
        st.toast("⚠️ Faltan datos por llenar")
        st.warning("Por favor escribe tu nombre y dirección antes de confirmar.")
    else:
        st.balloons()
        st.toast("🎉 ¡Pedido registrado con éxito!")
        st.success(f"¡Gracias, {nombre}! Tu pedido quedó registrado.")
        st.write(f"**Producto:** {cantidad} vape(s) de {sabor}")
        st.write(f"**Entrega en:** {direccion}")
        st.write(f"**Total a pagar:** ${total:,}")



 
