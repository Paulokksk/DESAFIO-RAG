# 🔍 Desafio Técnico: Pipeline de IA com OCR, Indexação e LLM

Este projeto implementa um pipeline de IA com **extração de texto (OCR), vetorização semântica**, e **geração de respostas com LLM**, baseado em documentos PDF e imagens.

---

## 🎯 Objetivo

Construir uma solução completa que:
1. Extraia texto de documentos PDF e imagens com OCR
2. Gere vetores semânticos e armazene em um banco vetorial (FAISS)
3. Receba perguntas em linguagem natural e gere respostas com uma LLM local da Hugging Face

---

## 🗂️ Estrutura do Projeto

```
desafio-rag/
├── data/                      # Arquivos de entrada (PDFs, imagens)
├── src/                       # Códigos-fonte por etapa
│   ├── preprocess_and_ocr.py
│   ├── indexing.py
│   ├── query_pipeline.py
│   ├── app_gradio.py
│   └── main.py
├── extracted_documents.json   # Saída da extração
├── chunk_metadata.json        # Metadados dos trechos
├── document_index.faiss       # Índice vetorial
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/Paulokksk/DESAFIO-RAG.git
cd desafio-rag
```

### 2. Instale o Tesseract OCR no sistema
```bash
sudo apt install tesseract-ocr
```

### 3. Instale as dependências Python
```bash
pip install -r requirements.txt
```

---

## 🧪 Etapas do Pipeline

### 🔹 1. Extração de texto (PDFs + Imagem)
```bash
python src/preprocess_and_ocr.py
```

### 🔹 2. Indexação dos textos
```bash
python src/indexing.py
```

### 🔹 3. Consultas no terminal
```bash
python src/query_pipeline.py
```

---

## 🌐 Interface Web (Gradio)

Para rodar com interface web:

```bash
python src/app_gradio.py
```

Acesse no navegador: `http://localhost:7860`

---

## 🧠 Tecnologias

- OCR: `pytesseract`, `PyMuPDF`
- Embeddings: `sentence-transformers`
- Indexação: `faiss`
- LLM local: `google/flan-t5-large` via `transformers`
- Interface: `gradio`

---

## 🖼️ Arquitetura

```text
                      ┌────────────────────────┐
                      │  PDF / Imagem (entrada)│
                      └────────────┬───────────┘
                                   │
                       [1] Extração e OCR
                                   │
                      ┌────────────▼───────────┐
                      │   Textos extraídos     │
                      └────────────┬───────────┘
                                   │
              [2] Chunking + Embeddings + Indexação
                                   │
                      ┌────────────▼───────────┐
                      │   Banco Vetorial FAISS │
                      └────────────┬───────────┘
                                   │
          [3] Pergunta → Busca → Resposta com LLM
                                   │
                      ┌────────────▼───────────┐
                      │  Modelo Hugging Face   │
                      └────────────────────────┘
```

---

## 📄 Licença

Uso livre para fins educacionais e avaliação técnica.
