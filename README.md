# AcadeGUIA 🏋️‍♂️

AcadeGUIA é um aplicativo de academia com **foco em mobile**, desenvolvido com a framework Flet em Python para criar e gerenciar séries de exercícios de forma simples e intuitiva.

![Tela Principal do AcadeGUIA](https://i.imgur.com/nJbWz3V.png)
*Para uma visualização mobile durante o desenvolvimento, redimensione a janela do aplicativo para um formato vertical, como um celular.*

## 🚀 Principais Funcionalidades

O AcadeGUIA foi projetado para oferecer uma experiência de usuário limpa e direta, permitindo que o usuário se concentre em seus treinos.

* **Menu Principal Intuitivo:** Acesso rápido às seções principais do aplicativo: "Minhas Séries", "Exercícios" e "Exercícios Salvos".
* **Gerenciamento de Séries:**
    * Visualização de todas as séries salvas, cada uma exibindo o nome e a quantidade total de exercícios.
    * Criação de novas séries de treino através de um botão de acesso rápido.
* **Detalhes da Série:**
    * Visualização detalhada de cada série, listando os exercícios que a compõem, junto com o número de séries e repetições (ex: 4x12).
    * Modo de edição que permite remover exercícios de uma série existente.
* **Biblioteca de Exercícios:**
    * Uma lista geral com todos os exercícios disponíveis, permitindo ao usuário adicionar novos exercícios às suas séries.
    * Uma seção de "Exercícios Salvos" para favoritar exercícios específicos.

## 📱 Foco em Mobile e Deploy

Este aplicativo foi construído com o objetivo de ser um **Progressive Web App (PWA)**, que pode ser "instalado" na tela inicial de qualquer celular (iOS ou Android) diretamente pelo navegador, sem precisar de uma loja de aplicativos.

## 🛠️ Tecnologias Utilizadas

* **Framework:** [Flet](https://flet.dev/)
* **Linguagem:** Python 3

## 📁 Estrutura do Projeto

O projeto é organizado de forma modular para facilitar a manutenção e a adição de novas funcionalidades.

/
├── assets/

├── funcoes.py

├── styles.py

├── utils.py

├── inicio.py

├── Minhas_series.py

├── serie.py

├── main.py

└── README.md



## ⚙️ Instalação e Configuração

1.  **Clone o repositório:**
    ```sh
    git clone <url-do-seu-repositorio>
    cd <nome-da-pasta-do-projeto>
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```sh
    pip install flet
    ```

## ▶️ Como Executar e Testar

### Para Desenvolvimento Rápido (Desktop)

Use este comando para ver o app em uma janela de desktop. É ideal para fazer alterações rápidas.

```sh
flet run
Para Testar a Visualização Mobile (Navegador)
Para ver como o app se comporta em um celular, execute-o no navegador.

Execute o comando:
Bash

flet run -w
Abra o link http://localhost:8550 no seu navegador de computador.
Para testar no seu celular: Certifique-se de que seu celular e seu computador estão na mesma rede Wi-Fi. Abra o navegador no celular e acesse o endereço IP do seu computador na porta 8550 (ex: http://192.168.1.5:8550). O Flet mostrará o endereço IP correto no terminal quando você executar o comando.
