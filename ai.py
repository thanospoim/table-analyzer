import main as mn
import google.generativeai as genai
from config import KEY

genai.configure(api_key=KEY, transport='rest')
model = genai.GenerativeModel("gemini-2.0-flash", 
                              system_instruction="You are an ai assistant that reads data from a pandas dataframe and makes a small text about the content of the dataframe in greek")
response = model.generate_content(str(mn.df_manual))
print(response.text)

