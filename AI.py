from groq import Groq
from config import Config

class Chatbot:
    def __init__(self, 
                 api_key=Config.GROQ_API_KEY, 
                 llm_model:str=Config.LLM_MODEL,
                 n_results:int=Config.N_RESULTS) -> None:
        
        self.ai = Groq(api_key=api_key)
        self.llm_model = llm_model
        self.chunk_amount_retrived = n_results
        
    def generate(self, prompt:str, chunks={}):
        try:
            response = self.ai.chat.completions.create(
            model=self.llm_model,
            messages=[
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
            ],
            
        )

            answer = response.choices[0].message.content
            

            # Your implementation here.
            if answer:
              
                return answer
            print("No answer generated.")
            return ''
        except Exception as ex:
            print(f"There was an error while generating response: \n\t\u2022 {ex}")
            input("\npress ENTER for knowledgement ")

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