import streamlit as st
st.title('DietApp')  # Corrigido: 'Dietapp' → 'DietApp'
st.write('Esta aplicação consegue te ajudar no cálculo de sua dieta.')  # Corrigido: 'Esse' → 'Esta'
st.write('Antes de começar... Preciso de algumas informações suas.')
botao_1 = st.button('Vamos lá!')
if 'confirmação_botao_1' not in st.session_state:
    st.session_state.confirmação_botao_1 = False
if botao_1:
    st.session_state.confirmação_botao_1 = True
if st.session_state.confirmação_botao_1:
    st.write('Digite seus dados:')  # Corrigido: 'sua:' → 'seus dados:'
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        altura = st.number_input('Altura em metros', min_value=0.00)
        altura = altura*100
    with col2:
        peso = st.number_input('Peso em kg', min_value=0.00)  # Corrigido: 'Kg' → 'kg'
    with col3:
        l_idade = list(range(1,101))
        idade = st.selectbox('Sua idade', l_idade)
    with col4: 
        genero = st.selectbox('Selecione seu gênero', ['Feminino','Masculino'])
    if genero == 'Masculino' or genero == 'Feminino': 
        botao_2 = st.button('Calcular')
        if 'confirmação_botao_2' not in st.session_state:
            st.session_state.confirmação_botao_2 = False
        if botao_2:
            st.session_state.confirmação_botao_2 = True
        if st.session_state.confirmação_botao_2:
            if genero == 'Masculino' and st.session_state.confirmação_botao_2:
                TBM = 88.362 + (13.397 * peso) + (4.799* altura) - (5.677* idade)
                st.write('Para o seu gênero: ', genero)  # Corrigido: texto mais claro
                st.write('Sua Taxa de Metabolismo Basal é ', round(TBM, 2))  # Corrigido: 'Betavolismo' → 'Metabolismo'
                st.success('Calculado com Sucesso!!')  # Corrigido: 'barriquinha' → 'barriguinha'      
            elif genero == 'Feminino' and st.session_state.confirmação_botao_2:
                TBM = 447.593 + (9.247* peso) + (3.098* altura) - (4.330* idade)
                st.write('Para o seu gênero: ', genero)  # Corrigido: texto mais claro
                st.write('Sua Taxa de Metabolismo Basal é ', round(TBM, 2))  # Corrigido: 'Betavolismo' → 'Metabolismo'
                st.success('Calculado com Sucesso!!')  # Adicionada vírgula para melhor pontuação                                           
            else:   

                st.error('Algo deu errado')  # Corrigido: mensagem mais apropriada
