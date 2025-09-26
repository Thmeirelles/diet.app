import streamlit as st
st.image("banner.png")
st.write('Esta aplicação consegue te ajudar no cálculo de sua dieta.')
st.write('Antes de começar... Preciso de algumas informações suas.')
botao_1 = st.button('Vamos lá!')
genero = ''
altura = 0.00
peso = 0.00
idade = 0
#Funções----------------------------------------
def aba_de_informacoes_pessoais (genero,altura,peso,idade):
    with st.expander("🔍 Suas Métricas", expanded=False):  # Começa fechado
        st.write('Digite seus dados:')  
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            altura = st.number_input('Altura em metros', min_value=0.00)
            altura = altura*100
        with col2:
            peso = st.number_input('Peso em kg', min_value=0.00)
        with col3:
            l_idade = list(range(1,101))
            idade = st.selectbox('Sua idade', l_idade)
        with col4: 
            genero = st.selectbox('Selecione seu gênero', ['Feminino','Masculino'])
    
    # Movido para fora: Botão e lógica de cálculo
    botao_2 = st.button('Calcular', key='botao_calcular')  # Adicionado key para evitar duplicates
    if 'confirmação_botao_2' not in st.session_state:
        st.session_state.confirmação_botao_2 = False
    if botao_2:
        st.session_state.confirmação_botao_2 = True
    if st.session_state.confirmação_botao_2:
        resultado_calculo1 (genero,altura,peso,idade)  

def resultado_calculo1 (genero,altura,peso,idade):
    if st.session_state.confirmação_botao_2 and not (altura*peso*idade) == 0 :
        tab1, tab2, tab3 = st.tabs(["📊 Cálculo de TBM", "📈 O que é TBM","Gasto metabolico total"])
        with tab1:
            if genero == 'Masculino' and st.session_state.confirmação_botao_2:
                TBM = 88.362 + (13.397 * peso) + (4.799* altura) - (5.677* idade)
                st.write('Para o seu gênero: ', genero)  
                st.write('Sua Taxa de Metabolismo Basal é ', round(TBM, 2))
                
                st.balloons()
                st.success('✅ Calculado com Sucesso!!')     
            elif genero == 'Feminino' and st.session_state.confirmação_botao_2:
                TBM = 447.593 + (9.247* peso) + (3.098* altura) - (4.330* idade)
                st.write('Para o seu gênero: ', genero)
                st.write('Sua Taxa de Metabolismo Basal é ', round(TBM, 2),' Calorias diárias')  # Corrigido: 'Betavolismo' → 'Metabolismo'
                st.balloons()
                st.success('✅ Calculado com Sucesso!!')
                if idade == 18 and peso > 65:
                    st.toast("Juliana detectada!", icon="🚨")
                    import time
                    time.sleep(4)
                    st.toast("VLW Pela moral JU!", icon="🌟")
                    import time
                    time.sleep(8)
        with tab2:
            st.markdown("""
            ## 🔍 **O que é TBM?**
            
            **TBM (Taxa de Metabolismo Basal)** é a quantidade mínima de calorias que seu corpo 
            precisa para manter as funções vitais em repouso completo.
            
            ---
            
            ### ⚡ **O que isso significa na prática?**
            
            - **💓 Funções vitais**: Respiração, circulação sanguínea, funcionamento cerebral
            - **🌡️ Regulação térmica**: Manutenção da temperatura corporal
            - **🔧 Reparo celular**: Renovação de tecidos e células
            
            ---
            
            ### 📊 **Como interpretar seu resultado?**
            
            | Situação | Significado |
            |----------|-------------|
            | **Seu TBM**: {} calorias | É o que você queima **sem fazer nada** |
            | + Atividades diárias | Adicione calorias gastas com movimento |
            | + Exercícios físicos | Some as calorias dos seus treinos |
            
            ---
            
            ### 💡 **Por que o TBM é importante?**
            
            - **🥗 Planejamento alimentar**: Saber quantas calorias você precisa
            - **🎯 Perda de peso**: Criar déficit calórico adequado
            - **💪 Ganho de massa**: Superávit calórico inteligente
            - **⚖️ Manutenção**: Equilíbrio entre consumo e gasto
            
            ---
            
            ### 🔄 **Fatores que influenciam o TBM:**
            
            - **🧬 Genética**: Cada pessoa é única
            - **👫 Gênero**: Homens geralmente têm TBM maior
            - **📈 Idade**: Metabolismo diminui com a idade
            - **💪 Massa muscular**: Músculos queimam mais calorias
            - **🌡️ Hormônios**: Tireoide e outros fatores
            
            ---
            
            ### 🚀 **Dicas para aumentar seu metabolismo:**
            
            - **🏋️‍♂️ Treino de força**: Construa mais músculos
            - **🥗 Alimentação balanceada**: Não pule refeições
            - **💧 Hidratação**: Água é essencial para o metabolismo
            - **😴 Sono quality**: Durma bem para regular hormônios
            - **⚡ Atividade constante**: Movimente-se durante o dia
            
            **💬 Lembre-se**: Seu TBM é apenas a base! Some suas atividades para ter o gasto total diário.
            """.format(round(TBM, 2) if 'TBM' in locals() else "SEU_RESULTADO"))
        with tab3:
            st.write('🔧 Em breve...')                                      
    else:   
        st.error('Coloque suas informações ')
        st.session_state.confirmação_botao_2 = False    

if 'confirmação_botao_1' not in st.session_state:
    st.session_state.confirmação_botao_1 = False
if botao_1:
    st.session_state.confirmação_botao_1 = True
if st.session_state.confirmação_botao_1:
    aba_de_informacoes_pessoais(genero,altura,peso,idade)


 


#"""tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📈 Análise", "⚙️ Configurações"])
#with tab1:
#    st.write("Conteúdo do dashboard")
#with tab2:
#    st.write("Análises detalhadas")
#with tab3:

#    st.slider("Parâmetro", 0, 100)

