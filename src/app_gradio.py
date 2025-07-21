"""
Arquivo: app_gradio.py
Etapa: Interface Web com Gradio

Objetivo:
- Criar uma interface visual para perguntar e receber respostas
"""

import gradio as gr
from query_pipeline import responder_pergunta

def responder(pergunta):
    return responder_pergunta(pergunta)

iface = gr.Interface(
    fn=responder,
    inputs=gr.Textbox(lines=2, placeholder="Digite sua pergunta sobre os documentos..."),
    outputs="text",
    title="Assistente de Documentos",
    description="Pergunte sobre os documentos PDF ou imagens indexadas com OCR.",
)

iface.launch()
