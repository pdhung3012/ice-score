from llm_code_eval import evaluate
import os
import openai

fp_key='/home/hungphd/git/OPENAI_API_KEY.txt'
f1=open(fp_key,'r')
str_key=f1.read().strip()
f1.close()

os.environ["OPENAI_API_KEY"]=str_key
model_openai = openai.chat.completions
openai.api_key=str_key
# response = model_openai.create(model='gpt-4o',temperature=0.0, messages=[
#         {"role": "system", "content": 'You are expert in code translation'},
#         {"role": "user", "content": 'Translate a tutorial C++ code to Python code'}])
# generated_text = response.choices[0].message.content
# print(generated_text)
# exit()
score = evaluate(problem="",
                    output="sum = 0\nfor i in range(len(list)):\n\tsum += list[i]\nreturn sum",
                    task="code-gen", aspect="usefulness", model="gpt-3.5-turbo")

print(score)