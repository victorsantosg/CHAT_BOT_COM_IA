# 🤖 ChatBot com IA

Este projeto foi desenvolvido como parte dos meus estudos, aplicando conceitos de **frontend e backend com Streamlit** e integração com a **API da OpenAI**.  
O objetivo foi construir um **chat interativo**, onde o usuário envia mensagens e recebe respostas de uma Inteligência Artificial em tempo real.

---

## 📌 Sobre o projeto

Durante o desenvolvimento deste projeto, aprendi a:

- Criar interfaces interativas com o **Streamlit**
- Utilizar o **session_state** para manter o histórico da conversa
- Integrar o **OpenAI SDK** para gerar respostas da IA
- Simular o funcionamento completo de um chat em tempo real

Foi um grande passo no meu aprendizado de como conectar o frontend ao backend e trabalhar com APIs externas em Python.

---

## 🧩 Tecnologias utilizadas

- **Python**
- **Streamlit**
- **OpenAI API (GPT-4o)**

---

## ⚙️ Como executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/chatbot-ia.git
   cd chatbot-ia ```

Crie e ative um ambiente virtual (opcional):

```python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Instale as dependências:

```pip install streamlit openai```


Adicione sua chave da OpenAI no código:

```modelo = OpenAI(api_key="SUA_CHAVE_AQUI")```


Execute a aplicação:

```streamlit run app.py```

💭 Como funciona

- O usuário envia uma mensagem no campo de chat

- A mensagem é registrada no histórico e enviada à IA

- A resposta da IA aparece na tela e também fica salva no histórico

📌 Observações

- É necessário ter uma conta com créditos ativos na OpenAI

- Nunca compartilhe sua chave da API publicamente

- O projeto utiliza o modelo gpt-4o

✍️ Autor

Desenvolvido por Victor Santos
Durante o curso da Hashtag Programação com o professor Lira