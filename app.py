import gradio as gr

description = """<div>
                <img src="https://i.imgur.com/FEA7N1p.png">
              </div>
             """

gr.Interface.load("models/Linaqruf/anything-v3.0", description=description).launch()