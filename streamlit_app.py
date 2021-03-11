import streamlit as st
from joblib import dump, load
import numpy as np
import os

# streamlit_app = nome do app

st.header('Aplicação')
st.subheader('Construído em Python')
st.markdown('Insira as informações para efetuar as previsões')

# Slider 
alturaSepala = st.slider('Informe a altura da sépala em cm',min_value = 0.0, max_value = 10.0)
st.write(alturaSepala)


# Selection box exemplo
#listaOpcoes = ['a','b','c']
#opcao = st.selectbox('Escolha a opção', options = listaOpcoes)
#st.write(opcao)

# text exemplo
#nome = st.text_input('Nome: ', max_chars=30)
#st.write(nome)

# Radio exemplo
#listOpcoes = ['sim','não']
#suportePlano = st.radio('Tem suporte ao plano internacional?',options = listOpcoes)
#st.write('Opção de suporte escolhida: ',suportePlano)


larguraSepala = st.slider('Informe a largura da sépala em cm', min_value = 0.0, max_value = 5.0)
st.write(larguraSepala)

alturaPetala = st.slider('Informe a altura da pétala em cm', min_value = 0.0, max_value = 7.0)
st.write(alturaPetala)

larguraPetala = st.slider('Informe a largura da pétala em cm', min_value = 0.0, max_value = 3.0)
st.write(larguraPetala)


if (os.path.exists('modelo1.pk1')):
	modelo = load('modelo1.pk1')
	botao = st.button('Efetuar previsão')
	if(botao):
		listaValores = np.array([[alturaSepala,larguraSepala,alturaPetala,larguraPetala]])
		resultado = modelo.predict(listaValores)
		if(resultado[0] == 0):
			st.write('Iris-Setosa')
		elif (resultado[0] == 1):
			st.write('Iris-Versicolour')
		else:
			st.write('Iris-Virginica')
else:
	st.error('Erro ao carregar o modelo preditivo. Contrate a administrador do sistema')


           