# main.py
import gradio as gr
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from nist_tests import run_sp800_90b_assessments
from vqr_turn import generate_vqr_bits

# -------------------------------
# Unified Service Function
# -------------------------------
def vqr_turn_service(n_bits: int = 1024):
    bits = generate_vqr_bits(n_bits)
    results = run_sp800_90b_assessments(bits)
    return bits, results


# -------------------------------
# Gradio UI
# -------------------------------
def gradio_interface(n_bits):
    bits, results = vqr_turn_service(n_bits)
    return bits, results

with gr.Blocks() as demo:
    gr.Markdown("# 🌌 Virtual Quantum Reality (VQR) - True Uniform Random Number (TURN) Service")

    with gr.Row():
        n_bits = gr.Number(value=1024, label="Number of bits", precision=0)
        run_btn = gr.Button("Generate & Test")

    bits_output = gr.Textbox(label="Generated Bits")
    results_output = gr.JSON(label="NIST Test Results")

    run_btn.click(gradio_interface, inputs=n_bits, outputs=[bits_output, results_output])


# -------------------------------
# FastAPI REST API
# -------------------------------
app = FastAPI()

@app.get("/generate")
def generate(n_bits: int = 1024):
    bits, results = vqr_turn_service(n_bits)
    return JSONResponse({"bits": bits, "results": results})


# -------------------------------
# Entrypoint
# -------------------------------
if __name__ == "__main__":
    import sys
    if "api" in sys.argv:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        demo.launch()
