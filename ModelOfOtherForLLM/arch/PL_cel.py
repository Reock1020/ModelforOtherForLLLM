from arch import IidaArchitecture
from arch.utils import call_llm
from arch.llm import LLM

class ProLangCEL(object):
    def __init__(self, belief_of_self, desire_of_self,
                 belief_of_other, desire_of_other):
        self.belief_of_self = belief_of_self
        self.desire_of_self = desire_of_self
        self.belief_of_other = belief_of_other
        self.desire_of_other = desire_of_other

        self.intention_of_self = []
        self.intention_of_other = []
        self.utterance_of_other = []

        self.llm=LLM()


    def create_output(self,utterance_of_other):
        '''
        以下のプログラムは対話システムの流れです．プログラムを基に自己の発話を生成してください．
        システムの内部表現はプロンプトの最後にparams_dataとして与えます．
        各システムに書かれてないプログラムはあなたが補完してください．
        指示のない文章は一切出力しないでください．
      class DialogueSystem:
            def __init__(self):
                # システムの内部表現
                self.belief_of_self = []  # 自己の信念
                self.belief_of_other = []  # 他者の信念
                self.desires_of_self = []  # 自己の願望
                self.desire_of_other = []  # 他者の願望
                self.intention_of_self = ""  # 自己の意図
                self.intention_of_other = ""  # 他者の意図

            def intention_estimation_system(self, belief_of_other, desire_of_other, utterance_of_other):
                意図推定システムについて説明します．意図推定システムは，「他者の意図(intention_of_other) 」を推定するシステムです．入力として与えられた，「他者の信念(belief_of_other)」「他者の願望(desire_of_other)」「他者の発話(utterance_of_other)」から，矛盾や違和感のない「他者の意図(intention_of_other)」を「推定 」してください
                

            def intention_generation_system(self, belief_of_self, desires_of_self, intention_of_other):
                意図生成システムについて説明します．意図生成システムは，「自己の意図(intention_of_self) 」を生成するシステムです．入力として与えられた，「自己の信念(belief_of_self)」「自己の願望(desire_of_self)」「他者の意図(intention_of_other)」から，矛盾や違和感のない「自己の意図(intention_of_self)」を「生成」してください．
                

            def utterance_generation_system(self, intention_of_self, utterance_of_other):
                発話生成システムについて説明します．発話生成システムは，「自己の発話(utterance_of_self)」 を生成するシステムです．入力として与えられた，「自己の意図(intention_of_self)」「他者の発話(utterance_of_other)」から，矛盾や違和感のない「自己の発話(utterance_of_self)」を「生成」してください

            def process_input(self, belief_of_other, desire_of_other, utterance_of_other):
                # 入力を受け取り、3つのシステムを順に起動させる
                intention_of_other = self.intention_estimation_system(belief_of_other, desire_of_other, utterance_of_other)
                intention_of_self = self.intention_generation_system(self.belief_of_self, self.desires_of_self, intention_of_other)
                utterance_of_self = self.utterance_generation_system(intention_of_self, utterance_of_other)

                # 各システムの入出力を出力
                print(f"他者の意図: {intention_of_other}")
                print(f"自己の意図: {intention_of_self}")
                print(f"自己の発話: {utterance_of_self}")

        # インスタンス化と入力処理の実行
        dialogue_system = DialogueSystem()
        dialogue_system.process_input(belief_of_other,desire_of_other,utterance_of_other)


        '''
        result = self.llm.simple_llm(
            docstring=self.create_output.__doc__,
            params_data={
                "belief_of_self":self.belief_of_self,"desire_of_self":self.desire_of_self,"desire_of_other":self.desire_of_other,"belief_of_other":self.belief_of_other,"utterance_of_other":self.utterance_of_other
                }
        )
        
        return result

    
    def update(self, utterance_of_other):
        self.utterance_of_other = utterance_of_other
        self.utterance_generation= self.create_output(utterance_of_other)
        return self.utterance_generation

    def __call__(self, utterance_of_other):
        return self.update(utterance_of_other)

    def load_data(self,data):
        for d in data["belief_of_self"]:
            self.belief_of_self.append(d)
        for d in data["desire_of_self"]:
            self.desire_of_self.append(d)
        for d in data["intention_of_self"]:
            self.intention_of_self.append(d)
        for d in data["belief_of_other"]:
            self.belief_of_other.append(d)
        for d in data["desire_of_other"]:
            self.desire_of_other.append(d)
        for d in data["intention_of_other"]:
            self.intention_of_other.append(d)
        for d in data["utterance_of_other"]:
            self.utterance_of_other.append(d)
        

