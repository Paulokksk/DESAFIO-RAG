"""
Arquivo: main.py
Etapa: Execução automatizada de todo o pipeline

Objetivo:
- Executar extração, indexação e abrir interface Gradio
"""

import os

print("📄 Etapa 1: Extração e OCR")
os.system("python src/preprocess_and_ocr.py")

print("\n🧠 Etapa 2: Indexação Vetorial")
os.system("python src/indexing.py")

print("\n🌐 Etapa 3: Interface Web Gradio")
os.system("python src/app_gradio.py")
