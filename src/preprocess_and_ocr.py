"""
Arquivo: preprocess_and_ocr.py
Etapa: Extração de conteúdo com OCR

Objetivo:
- Ler documentos PDF e imagens
- Aplicar OCR quando necessário
- Salvar textos extraídos em um arquivo JSON
"""

import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import json
import os

# Função para extrair texto de PDF com texto nativo
def extract_text_from_pdf(pdf_path):
    print(f"📄 Extraindo texto de: {pdf_path}")
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

# Função para aplicar OCR em imagem
def ocr_from_image(image_path, lang="por"):
    print(f"🖼️ Aplicando OCR em imagem: {image_path}")
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=lang)
    return text.strip()

# Caminhos dos arquivos
pdf_path = "data/CÓDIGO DE OBRAS.pdf"
image_path = "data/tabela.webp"

# Executar extrações
pdf_text = extract_text_from_pdf(pdf_path)
ocr_text = ocr_from_image(image_path)

# Salvar resultado em JSON
output = {
    "codigo_de_obras": pdf_text,
    "tabela_de_precos": ocr_text
}

with open("extracted_documents.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("✅ Textos extraídos e salvos em extracted_documents.json")
