import os
import json
from arch.PL_lec import ProLangLEC
from arch.PL_cel import ProLangCEL
from arch.NL_lec import NaturalLangLEC
from arch.NL_cel import NaturalLangCEL

class Agent(object):

    def __init__(self):
        self.action = None
        self.observation = None
        self.p_lec = ProLangLEC([],[],[],[])
        self.p_cel = ProLangCEL([],[],[],[])
        self.n_lec = NaturalLangLEC([],[],[],[])
        self.n_cel = NaturalLangCEL([],[],[],[])

    def update(self, observation,arch_select):
        # update all sates
        if arch_select == 0:
            self.action = self.p_lec.update(observation)
        elif arch_select == 1:
            self.action = self.p_cel.update(observation)
        elif arch_select == 2:
            self.action = self.n_lec.update(observation)
        elif arch_select == 3:
            self.action = self.n_cel.update(observation)
            
        return self.action

    def __call__(self, observation,arch_select):
        return self.update(observation,arch_select)
    
    def read_file(self,path,arch_select):
        if not os.path.isfile(path):
            print(f"Failed to load : {path}")

        datas = json.load(open(path, 'r', encoding='utf-8'))
        if arch_select == 0:
            self.p_lec.load_data(datas)
        elif arch_select == 1:
            self.p_cel.load_data(datas)
        elif arch_select == 2:
            self.n_lec.load_data(datas)
        elif arch_select == 3:
            self.n_cel.load_data(datas)

        if "log" in datas:
            self.log = datas["log"]

