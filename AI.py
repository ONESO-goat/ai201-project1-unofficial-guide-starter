from groq import Groq
from config import Config
import ollama 
import gradio as gr
class Chatbot:
    def __init__(self, 
                 
                 api_key=Config.GROQ_API_KEY, 
                 llm_model:str=Config.LLM_MODEL,
                 n_results:int=Config.N_RESULTS,
                 use_ollama:bool=False) -> None:
        if use_ollama:
            self.backend = 'ollama'
            self.ollama_model = 'qwen3:0.6b'

            try:
                ollama.show(self.ollama_model)
                print(f"✓ Using Ollama ({self.ollama_model})")

            except Exception:
                print(f"⚠ Ollama model '{self.ollama_model}' not found")
                print(f"Run: ollama pull {self.ollama_model}")
        else:
            self.backend = "grok"
            self.ai = Groq(api_key=api_key)
        
        self.llm_model = llm_model
        self.chunk_amount_retrived = n_results
        
    def generate(self, prompt:str, chunks={}):
        m = [
                    {
                        "role": "system",
                        "content": (
                            """You are a helpful assistant for students who are interested in tech. 
                            Students might ask for upcoming hackthons, best educational platform, etc.
                            """
                            "Use only the provided rule chunks to answer questions. "
                            "Implement a script that loads the documents, cleans them, and produces chunks matching the specified chunk size and overlap. "
                            "If the answer is not contained in the chunks, say "
                            "'I don't know based on the provided results.'"
                        ),
                    },
                    {
                        "role": "user",
                        "content": f"""
            Question:
            {prompt}
            
            
            Context:
            {chunks}

            """,
                    },
                ]
        if self.backend == 'grok':
            try:
                response = self.ai.chat.completions.create(
                model=self.llm_model,
                messages=m,
                
            )

                answer = response.choices[0].message.content
                
                if answer:
                
                    return answer
                print("No answer generated.")
                return ''
            
            except Exception as ex:
                print(f"There was an error while generating response: \n\t\u2022 {ex}")
                #input("\npress ENTER for knowledgement ")
                
        else:
            try:
             
                client = ollama.Client(timeout=60.0)

               
                kwargs = {
                    'model': self.ollama_model,
                    'messages': m,
                    'options': {
                        'temperature': 0.2
                    }
                }
            

                
                response = client.chat(**kwargs)

                content = response['message']['content']
                print("\nOllama Response and content are created successfully\n")
              
                #print(f'\n\n\t\u2022CONTENT: {content}')
                return content

            except Exception as e:
                print(f"⚠ Ollama generation error: {e}")

                return ""
                
    def handle_query(self,text):
        
        result = self.generate(text)
        #sources = "\n".join(f"• {s}" for s in result["sources"])
        return result, 'MLH'

    def open_gui(self):
        with gr.Blocks() as demo:
            inp = gr.Textbox(label="Your question")
            btn = gr.Button("Ask")
            answer = gr.Textbox(label="Answer", lines=8)
            sources = gr.Textbox(label="Retrieved from", lines=4)
            btn.click(self.handle_query, inputs=inp, outputs=[answer, sources])
            inp.submit(self.handle_query, inputs=inp, outputs=[answer, sources])

    def __str__(self):
        return f"{self.llm_model}"

if __name__ == "__main__":
    bot = Chatbot()
    c = {
        "hackathon_0": {"name": "hackMIT", "price": "free",  "address": "cambridge mass"},
        "hackathon_1": {"name": "cursor boston", "price": "free",  "address": "boston mass"},
        "hackathon_2": {"name": "MIT ocean converation hackathon", 'price': 'free', "address": "cambridge mass"}
    }
    print(bot.generate("I want to focus on Data science, which tech event is best to gain the knowledge?", chunks=c))