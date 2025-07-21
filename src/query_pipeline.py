"""
Arquivo: query_pipeline.py
Etapa: Recuperação + Geração de Respostas

Objetivo:
- Receber perguntas do usuário
- Buscar os chunks mais relevantes no índice vetorial
- Gerar resposta usando uma LLM local (FLAN-T5)
"""

import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Carregar índice FAISS e metadados
print("📦 Carregando índice vetorial e dados auxiliares...")
index = faiss.read_index("document_index.faiss")
with open("chunk_metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

chunks = data["chunks"]

# Modelo de embedding
model_embed = SentenceTransformer("all-MiniLM-L6-v2")

# LLM local via Hugging Face (Flan-T5)
print("🧠 Carregando modelo LLM da Hugging Face...")
model_id = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model_llm = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# Função principal de resposta
def responder_pergunta(pergunta, top_k=3):
    pergunta_embed = model_embed.encode([pergunta])
    D, I = index.search(np.array(pergunta_embed), top_k)

    trechos = [chunks[i] for i in I[0] if i < len(chunks)]

    if not trechos:
        return "❗ Nenhum trecho relevante foi encontrado nos documentos."

    contexto = "\n\n".join(trechos)

    # ⚠️ Prompt mais direto para o FLAN-T5
    prompt = f"Pergunta: {pergunta}\n\nContexto: {contexto}\n\nResposta:"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    outputs = model_llm.generate(**inputs, max_new_tokens=300)

    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return resposta.strip()

# Interface via terminal
if __name__ == "__main__":
    print("💬 Assistente de Documentos | Digite 'sair' para encerrar.\n")
    while True:
        pergunta = input("❓ Pergunta: ")
        if pergunta.lower() == "sair":
            break
        resposta = responder_pergunta(pergunta)
        print("\n💡 Resposta:\n", resposta)
