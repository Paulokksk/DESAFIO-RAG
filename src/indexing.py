"""
Arquivo: indexing.py
Etapa: Indexação Vetorial

Objetivo:
- Carregar textos extraídos
- Dividir em chunks
- Gerar embeddings semânticos
- Salvar base vetorial FAISS e metadados
"""

import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Carregar texto extraído do OCR e PDFs
with open("extracted_documents.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

# Função para dividir o texto em chunks
def chunk_text(text, max_tokens=1000, overlap=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_tokens - overlap):
        chunk = ' '.join(words[i:i + max_tokens])
        chunks.append(chunk)
    return chunks

print("📄 Iniciando chunking e preparação de dados...")
all_chunks = []
metadata = []

for doc_name, content in documents.items():
    chunks = chunk_text(content)
    for i, chunk in enumerate(chunks):
        if chunk.strip() and len(chunk.strip()) > 100:  # evita textos muito curtos
            all_chunks.append(chunk.strip())
            metadata.append({"doc": doc_name, "chunk_index": i})


# Gerar embeddings com SentenceTransformers
print("🔍 Gerando embeddings com modelo 'all-MiniLM-L6-v2'...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(all_chunks, show_progress_bar=True)

# Criar índice FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Salvar índice e metadados
faiss.write_index(index, "document_index.faiss")
with open("chunk_metadata.json", "w", encoding="utf-8") as f:
    json.dump({"chunks": all_chunks, "metadata": metadata}, f, ensure_ascii=False, indent=2)

print("✅ Indexação finalizada com sucesso!")
