import sys,os 
sys.path.append(os.path.dirname(os.path.abspath(__file__))+ '/../')
from agent import Agent

agent = Agent()

#プログラミング言語LEC:0 ,プログラミング言語CEL:1，自然言語LEC:2,自然言語CEL:3
arch_select = 3
data_file = os.path.join(os.path.dirname(__file__)+ '/../', 'data', 'hiniku.json')
if os.path.exists(data_file):
    agent.read_file(data_file,arch_select)
else:
    print("指定されたファイルが見つかりません．")

observation = "無理しないでね"

for i in range(1):
    print("------------------------------",+i)
    action = agent(observation,arch_select)
    print("出力\n",action)