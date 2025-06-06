AcadeGUIA 🏋️‍♂️
Um aplicativo de academia multiplataforma, desenvolvido com a framework Flet em Python, para criar e gerenciar séries de exercícios de forma simples e intuitiva.

🚀 Principais Funcionalidades
O AcadeGUIA foi projetado para oferecer uma experiência de usuário limpa e direta, permitindo que o usuário se concentre em seus treinos.

Menu Principal Intuitivo: Acesso rápido às seções principais do aplicativo: "Minhas Séries", "Exercícios" e "Exercícios Salvos". 
Gerenciamento de Séries:
Visualização de todas as séries salvas, cada uma exibindo o nome e a quantidade total de exercícios. 
Criação de novas séries de treino através de um botão de acesso rápido. 
Detalhes da Série:
Visualização detalhada de cada série, listando os exercícios que a compõem, junto com o número de séries e repetições (ex: 4x12). 
Modo de edição que permite remover exercícios de uma série existente. 
Biblioteca de Exercícios:
Uma lista geral com todos os exercícios disponíveis, permitindo ao usuário adicionar novos exercícios às suas séries. 
Uma seção de "Exercícios Salvos" para favoritar exercícios específicos. 
Tela de detalhes para cada exercício, mostrando imagem e instruções de execução. 
🛠️ Tecnologias Utilizadas
Framework: Flet
Linguagem: Python 3
📁 Estrutura do Projeto
O projeto é organizado de forma modular para facilitar a manutenção e a adição de novas funcionalidades.

/
├── assets/   # Pasta para imagens e outros recursos estáticos

│   ├── AcadeGUIA.png

│   └── favicon.png

├── funcoes.py              # Módulo com todos os componentes reutilizáveis (botões, cards, layout)

├── styles.py               # Módulo para estilos de componentes específicos

├── utils.py                # Módulo responsável pelo roteamento e navegação do app

├── inicio.py               # View da tela de Início (menu principal)

├── Minhas_series.py        # View da tela "Minhas Séries"

├── serie.py                # View da tela de detalhes de uma série

├── main.py                 # Ponto de entrada principal da aplicação

└── README.md               # Documentação do projeto (este arquivo)

⚙️ Instalação e Configuração
Para executar este projeto localmente, siga os passos abaixo:

Clone o repositório:

Bash

git clone <url-do-seu-repositorio>
cd <nome-da-pasta-do-projeto>
Crie e ative um ambiente virtual (recomendado):

Bash

# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
Instale as dependências:
O único requisito principal é o Flet.

Bash

pip install flet
▶️ Como Executar
Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no terminal, na pasta raiz do projeto:

Bash

flet run
Alternativamente, você pode executar o arquivo main.py diretamente:

Bash

python main.py
O aplicativo será aberto em uma janela nativa do seu sistema operacional.
