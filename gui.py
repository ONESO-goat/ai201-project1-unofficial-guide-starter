import gradio as gr
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from AI import Chatbot
    from emb import Embeddings




class GUI:
    def __init__(self, bot:"Chatbot",embedding:"Embeddings"):
        self.bot = bot
        self.embedding = embedding
        self.demo = self.open_gui()

    def chat(self,message, history):
        if not message.strip():
            return ""
        retrieved = self.embedding.retrieve(message)
        return self.bot.generate(message, retrieved)

    def handle_query(self,text): 
        result = self.bot.generate(text)
        #sources = "\n".join(f"• {s}" for s in result["sources"])
        return result, 'MLH'
    
    def open_gui(self): 
        with gr.Blocks(
        theme=gr.themes.Soft(primary_hue="indigo"),
        title="RulesBot",
    ) as demo:

            gr.HTML("""
                <div style="text-align:center; padding:1.25rem 0 0.5rem;">
                    <h1 style="font-size:2rem; font-weight:700; color:#312e81; margin:0;">
                        💻 HackthonWizard
                    </h1>
                    <p style="color:#6b7280; font-size:1rem; margin:0.4rem 0 0;">
                        Ask anything about hackthons — answers straight from provided dataset.
                    </p>
                </div>
            """)

            with gr.Row():
                with gr.Column(scale=3):
                    gr.ChatInterface(
                        fn=self.chat,
                        type="messages",
                        chatbot=gr.Chatbot(
                            height=440,
                            type="messages",
                            placeholder=(
                                "<div style='text-align:center; color:#9ca3af; margin-top:3rem;'>"
                                "Ask a rules question to get started — no arguing required 🎯"
                                "</div>"
                            ),
                        ),
                        textbox=gr.Textbox(
                            placeholder='e.g. "Can I build a road through someone else\'s settlement?"',
                            container=False,
                            scale=7,
                        ),
                        examples=[
                            "What are some upcoming hackathons?",
                            "What are some free hackathons?",
                            "I am visiting Californa, what is the hackthon history?",
                            "What are some hackathons stated on reddit?",
                            "What are the common themes for hackathons?",
                            "Can you provide me hackathons that are online?",
                            "What hackathon will you recommend?",
                            "What hackathons will be taking place soon?",
                        ],
                        cache_examples=False,
                    )

                with gr.Column(scale=1, min_width=180):
                    gr.HTML("""
                        <div style="background:#f5f3ff; border:1px solid #ddd6fe;
                                    border-radius:10px; padding:1rem; margin-top:0.5rem;">
                            <p style="font-size:0.8rem; font-weight:700; color:#4c1d95;
                                    margin:0 0 0.5rem; letter-spacing:0.05em;">
                                💻 LOADED HACKATHONs
                            </p>
                            <ul style="font-size:0.85rem; color:#5b21b6; list-style:none;
                                        padding:0; margin:0; line-height:1.8;">
                                <li>Reddit</li>
                                <li>Devpost</li>
                                <li>Devfolio</li>
                            </ul>
                            <hr style="border:none; border-top:1px solid #ddd6fe; margin:0.75rem 0;">
                            <p style="font-size:0.75rem; color:#7c3aed; margin:0; line-height:1.5;">
                                Answers are grounded in the loaded rules only. If a hackathon or hackathon information
                                isn't in the dataset, HackthonWizard will say so.
                            </p>
                        </div>
                    """)
        return demo