import ollama
import json
import re
from datetime import date, timedelta


def calcular_prazo_dia_semana(dia_alvo, proxima, hoje):
    dias_semana = {
        "segunda": 0,
        "terça": 1,
        "terca": 1,
        "quarta": 2,
        "quinta": 3,
        "sexta": 4,
        "sábado": 5,
        "sabado": 5,
        "domingo": 6
    }

    dia_alvo = dias_semana[dia_alvo]

    dia_atual = hoje.weekday()

    diferenca = (dia_alvo - dia_atual) % 7

    if proxima:
        # "quarta que vem" = quarta da próxima semana
        if diferenca == 0:
            diferenca = 7
        else:
            diferenca += 7

    return hoje + timedelta(days=diferenca)


def encontrar_prazo_na_frase(frase, hoje):

    texto = frase.lower()

    # -------------------------
    # Amanhã
    # -------------------------

    if "depois de amanhã" in texto:
        return hoje + timedelta(days=2)

    if "amanhã" in texto:
        return hoje + timedelta(days=1)

    if "hoje" in texto:
        return hoje

    # -------------------------
    # Dias da semana
    # -------------------------

    padrao = (
        r"(segunda|terça|terca|quarta|quinta|sexta|"
        r"sábado|sabado|domingo)"
        r"(?:-feira)?"
    )

    resultado = re.search(padrao, texto)

    if resultado:

        dia = resultado.group(1)

        # Detecta:
        # "quarta que vem"
        # "quarta-feira que vem"
        # "quarta próxima"
        # "próxima quarta"
        # "quarta q vem"

        inicio = max(0, resultado.start() - 10)
        fim = min(len(texto), resultado.end() + 15)

        contexto = texto[inicio:fim]

        proxima = (
            "que vem" in contexto
            or "q vem" in contexto
            or "próxima" in contexto
            or "proxima" in contexto
        )

        return calcular_prazo_dia_semana(
            dia,
            proxima,
            hoje
        )

    # Se não encontrou um prazo conhecido,
    # usa a data atual como fallback.

    return hoje


def extrair_tarefa(frase):

    hoje = date.today()

    # Primeiro tentamos descobrir o prazo
    # diretamente na frase.
    prazo = encontrar_prazo_na_frase(
        frase,
        hoje
    )

    # A IA fica responsável somente pelo título.
    prompt = f"""
Extraia somente o título da tarefa abaixo.

Tarefa:
"{frase}"

Remova informações de data ou prazo do título.

Retorne SOMENTE JSON:

{{
    "titulo": "titulo da tarefa"
}}
"""

    resposta = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    texto = resposta["message"]["content"]

    dados = json.loads(texto)

    titulo = dados["titulo"]

    return {
        "titulo": titulo,
        "prazo": prazo.strftime("%Y-%m-%d")
    }
