from .config import SessionLocal
from .models import CatalogoExercicio


def inicializar_catalogo():
    db = SessionLocal()

    # Lista COMPLETA e DETALHADA de exercícios baseada na sua tabela
    exercicios_padrao = [
        # --- PEITORAL ---
        {
            "grupo": "Peito", "nome": "Supino Reto (Barra)", "tipo": "Composto", "alvo": "Peitoral Maior",
            "d1": "Retração escapular e pés firmes no chão.",
            "d2": "Desça a barra até a linha dos mamilos.",
            "d3": "Empurre em linha reta ou leve arco."
        },
        {
            "grupo": "Peito", "nome": "Supino Inclinado (Halter)", "tipo": "Composto", "alvo": "Peitoral Superior",
            "d1": "Banco 30°-45°. Halteres sobre ombros.",
            "d2": "Desça lateralmente abrindo o peitoral.",
            "d3": "Empurre para cima e para o centro."
        },
        {
            "grupo": "Peito", "nome": "Crucifixo (Halteres)", "tipo": "Isolado", "alvo": "Peitoral Geral",
            "d1": "Cotovelos com flexão fixa (travados).",
            "d2": "Abra em arco (abraço) alongando tudo.",
            "d3": "Feche o arco sem dobrar cotovelos."
        },
        {
            "grupo": "Peito", "nome": "Crossover (Polia)", "tipo": "Isolado", "alvo": "Peitoral Inferior",
            "d1": "Tronco inclinado, base estável.",
            "d2": "Deixe o cabo alongar o peitoral atrás.",
            "d3": "Cruze as mãos à frente do quadril."
        },
        {
            "grupo": "Peito", "nome": "Flexão de Braço", "tipo": "Composto", "alvo": "Peitoral / Tríceps",
            "d1": "Corpo em prancha, bracing ativo.",
            "d2": "Desça em bloco até quase tocar o chão.",
            "d3": "Empurre explosivamente sem perder a lombar."
        },

        # --- COSTAS ---
        {
            "grupo": "Costas", "nome": "Levantamento Terra", "tipo": "Composto", "alvo": "Cadeia Posterior",
            "d1": "Barra no mediopé, coluna neutra.",
            "d2": "Quadril para trás (hinge) descendo a barra.",
            "d3": "Empurre o chão e estenda o corpo todo."
        },
        {
            "grupo": "Costas", "nome": "Puxada Alta", "tipo": "Composto", "alvo": "Grande Dorsal",
            "d1": "Travado no banco, tronco levemente inclinado.",
            "d2": "Alongue os braços deixando a escápula subir.",
            "d3": "Deprima a escápula e puxe até o queixo."
        },
        {
            "grupo": "Costas", "nome": "Remada Curvada", "tipo": "Composto", "alvo": "Latíssimo / Trapézio",
            "d1": "Tronco inclinado, coluna reta.",
            "d2": "Estenda braços alongando a dorsal.",
            "d3": "Puxe a barra no umbigo, esmagando as costas."
        },
        {
            "grupo": "Costas", "nome": "Remada Serrote", "tipo": "Composto", "alvo": "Latíssimo (Unilateral)",
            "d1": "Apoio tripé no banco. Coluna mesa.",
            "d2": "Desça alongando e rotacionando levemente.",
            "d3": "Puxe o halter em direção ao quadril."
        },
        {
            "grupo": "Costas", "nome": "Pulldown (Polia)", "tipo": "Isolado", "alvo": "Grande Dorsal",
            "d1": "Tronco 45°, braços estendidos.",
            "d2": "Suba os braços até alinhar com orelhas.",
            "d3": "Abaixe a barra em arco sem dobrar cotovelos."
        },

        # --- OMBROS ---
        {
            "grupo": "Ombro", "nome": "Desenv. Militar", "tipo": "Composto", "alvo": "Deltoide Anterior",
            "d1": "Cotovelos no plano escapular (frente).",
            "d2": "Desça até queixo/clavícula.",
            "d3": "Empurre vertical e encaixe a cabeça."
        },
        {
            "grupo": "Ombro", "nome": "Elevação Lateral", "tipo": "Isolado", "alvo": "Deltoide Médio",
            "d1": "Cotovelos semiflexionados fixos.",
            "d2": "Desça devagar até a lateral da coxa.",
            "d3": "Eleve até a altura do ombro (jarra d'água)."
        },
        {
            "grupo": "Ombro", "nome": "Crucifixo Inverso", "tipo": "Isolado", "alvo": "Deltoide Posterior",
            "d1": "Peito no encosto do banco.",
            "d2": "Controle a volta sem bater pesos.",
            "d3": "Abra para trás focando no posterior."
        },
        {
            "grupo": "Ombro", "nome": "Elevação Frontal", "tipo": "Isolado", "alvo": "Deltoide Anterior",
            "d1": "Pés firmes, não balance o tronco.",
            "d2": "Desça controlando a gravidade.",
            "d3": "Suba até a linha dos olhos."
        },
        {
            "grupo": "Ombro", "nome": "Remada Alta", "tipo": "Composto", "alvo": "Trapézio / Delt. Lat.",
            "d1": "Pegada aberta na barra.",
            "d2": "Desça rente ao corpo.",
            "d3": "Suba cotovelos acima da linha dos ombros."
        },

        # --- PERNAS ---
        {
            "grupo": "Perna", "nome": "Agachamento Livre", "tipo": "Composto", "alvo": "Quadríceps / Glúteo",
            "d1": "Barra no trapézio, pés largura ombros.",
            "d2": "Flexione joelho/quadril, coluna neutra.",
            "d3": "Empurre o chão, evite valgo (joelho para dentro)."
        },
        {
            "grupo": "Perna", "nome": "Leg Press 45º", "tipo": "Composto", "alvo": "Quadríceps",
            "d1": "Lombar colada no banco o tempo todo.",
            "d2": "Desça até 90° sem tirar quadril do banco.",
            "d3": "Empurre sem travar joelhos no final."
        },
        {
            "grupo": "Perna", "nome": "Cadeira Extensora", "tipo": "Isolado", "alvo": "Quadríceps",
            "d1": "Joelho alinhado ao eixo da máquina.",
            "d2": "Desça segurando o peso.",
            "d3": "Chute e segure 1s no topo."
        },
        {
            "grupo": "Perna", "nome": "Stiff", "tipo": "Composto", "alvo": "Isquiotibiais",
            "d1": "Joelhos com flexão fixa leve.",
            "d2": "Quadril para trás, tronco desce reto.",
            "d3": "Quadril para frente contraindo glúteo."
        },
        {
            "grupo": "Perna", "nome": "Mesa Flexora", "tipo": "Isolado", "alvo": "Isquiotibiais",
            "d1": "Quadril pressionado contra o banco.",
            "d2": "Desça devagar (fase negativa importante).",
            "d3": "Flexione tentando encostar no glúteo."
        },
        {
            "grupo": "Perna", "nome": "Agachamento Búlgaro", "tipo": "Composto", "alvo": "Glúteo / Quadríceps",
            "d1": "Um pé apoiado atrás, base estável.",
            "d2": "Desça até joelho de trás quase tocar chão.",
            "d3": "Empurre com a perna da frente."
        },
        {
            "grupo": "Perna", "nome": "Panturrilha em Pé", "tipo": "Isolado", "alvo": "Panturrilha",
            "d1": "Joelhos estendidos, tronco reto.",
            "d2": "Desça calcanhar ao máximo (alongue).",
            "d3": "Suba na ponta dos pés ao máximo."
        },

        # --- BRAÇOS ---
        {
            "grupo": "Braço", "nome": "Rosca Direta", "tipo": "Isolado", "alvo": "Bíceps Braquial",
            "d1": "Cotovelos colados no corpo.",
            "d2": "Estenda quase tudo sem relaxar.",
            "d3": "Flexione sem jogar tronco para trás."
        },
        {
            "grupo": "Braço", "nome": "Rosca Alternada", "tipo": "Isolado", "alvo": "Bíceps (Supinação)",
            "d1": "Halteres na lateral, base neutra.",
            "d2": "Desça girando a palma para dentro.",
            "d3": "Suba girando a palma para cima."
        },
        {
            "grupo": "Braço", "nome": "Rosca Martelo", "tipo": "Isolado", "alvo": "Braquial / Antebraço",
            "d1": "Pegada neutra o tempo todo.",
            "d2": "Desça controlando.",
            "d3": "Suba mantendo a palma para dentro."
        },
        {
            "grupo": "Braço", "nome": "Tríceps Testa", "tipo": "Isolado", "alvo": "Tríceps (Longa)",
            "d1": "Braços inclinados para trás da cabeça.",
            "d2": "Flexione cotovelos levando barra à testa.",
            "d3": "Estenda cotovelos sem mover o braço."
        },
        {
            "grupo": "Braço", "nome": "Tríceps Corda", "tipo": "Isolado", "alvo": "Tríceps (Lateral)",
            "d1": "Cotovelos colados na costela.",
            "d2": "Suba até o peito sem descolar cotovelo.",
            "d3": "Empurre e abra a corda no final."
        },
        {
            "grupo": "Braço", "nome": "Mergulho (Paralelas)", "tipo": "Composto", "alvo": "Tríceps / Peitoral",
            "d1": "Corpo vertical (foco tríceps).",
            "d2": "Desça até cotovelo em 90°.",
            "d3": "Empurre estendendo tudo."
        },
    ]

    print("--- Iniciando população DETALHADA do Catálogo ---")

    for item in exercicios_padrao:
        # Verifica se já existe para não duplicar
        existe = db.query(CatalogoExercicio).filter_by(nome=item["nome"]).first()

        if not existe:
            novo = CatalogoExercicio(
                nome=item["nome"],
                grupo_muscular=item["grupo"],
                tipo=item["tipo"],
                musculo_alvo=item["alvo"],
                dica_preparacao=item["d1"],
                dica_excentrica=item["d2"],
                dica_concentrica=item["d3"]
            )
            db.add(novo)
            print(f"Adicionado: {item['nome']}")

    try:
        db.commit()
        print("--- Catálogo atualizado com sucesso! ---")
    except Exception as e:
        print(f"Erro ao popular banco: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    inicializar_catalogo()