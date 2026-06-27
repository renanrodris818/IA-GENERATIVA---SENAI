
import streamlit as st 

st.title('CALCULADORA')

n1 = st.number_input('Número 1:',value = 0)
n2 = st.number_input('Número 2:',value = 0) 

soma, sub, mult, div = st.columns(4)

if soma.button('Soma'): 
    soma = n1 + n2 
    st.title(soma)
elif sub.button('Subtração'):
    subtracao = n1 - n2
    st.title(subtracao)
elif mult.button('Multiplicação'):
    multiplicacao = n1 * n2
    st.title(multiplicacao)
elif div.button('Divisão'):
    divisao = n1 / n2 
    st.title(divisao)
#--------------------------------------------------------

st.title('Desafio 1: O Cartão de Visitas Digital')

st.header('Cartão de visita')

st. text('Cartão Visa')

st.markdown('Desafio 1')
#--------------------------------------------------------

st.title('Desafio 2: Formulário de Cadastro de Usuário')

nome = st.text_input('Digite seu nome: ')
idade = st.number_input('Digite sua idade: ',value = 0)
termos = st.checkbox('Aceite os termos')


if st.button('Enviar'):
    if termos == True:
        st.header(f'Nome: {nome}, Idade: {idade};')
    else:
        st.header('Aceite os termos')
#-------------------------------------------------------

st.title('Desafio 3: O Seletor de Cursos')

curso = st.selectbox('Qual curso você deseja?',('','Python', 'Web', 'Java', 'HTML'))
cursos = st.multiselect('Quais cursos você deseja?',('','Python','Web','Java','HTML'))
if curso or cursos == True:
    st.success(f'{curso},{cursos}')
#-------------------------------------------------------

st.title('Desafio 4: Visualizador de Planilhas Interativo (Exibição de Dados)')





