import gradio as gr
import steganography as st
from PIL import Image
import numpy as np

def hide_msg(img, msg):
    img = np.array(img)
    out = st.steganography_hide_msg(img, msg)
    return Image.fromarray(out)

def reveal_msg(img):
    img = np.array(img)
    return st.steganography_reveal_msg(img)

with gr.Blocks() as app:

    gr.Markdown("# 🔎 Steganography Tool")

    with gr.Tab("Encode"):
        with gr.Row():
            with gr.Column():
                input_img = gr.Image(type='pil', format='png', show_label=False)
                input_txt = gr.Textbox(placeholder="Enter message to hide", show_label=False, type="text")

            with gr.Column():
                output_img = gr.Image(type='pil', format='png', show_label=False)

        btn = gr.Button("Apply")
        btn.click(hide_msg, [input_img, input_txt], output_img)

    with gr.Tab("Decode"):
        input_img2 = gr.Image(type='pil', format='png', show_label=False)
        btn2 = gr.Button("Reveal Message")
        output_txt = gr.Textbox(show_label=False)

        btn2.click(reveal_msg, input_img2, output_txt)


app.launch(share=False)
