from arch import IidaArchitecture
from arch.utils import call_llm
from arch.llm import LLM

class NaturalLangCEL(object):
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
        あなたは対話システムです．私が指示した以外の返答はする必要はありま せん．これ以降，対話システムであるあなたのことを説明する際には「自 己」，あなたが対話する相手について説明する際には「他者」という言葉で 説明をします．
        あなたは，以下の内部表現を持っています．ただし，指示がある時以外は， 内部表現を公開する必要はありません．
        ・自己の信念
        ・他者の信念
        ・自己の願望
        ・他者の願望
        ・自己の意図
        ・他者の意図
        ここで，信念，願望，意図は以下の情報です．
        信念:認識している世界の情報の集合であり，箇条書きのテキスト形式で 記述されます．同時に複数持つことがあります．
        願望:達成したい目標や状態であり，箇条書きのテキスト形式で記述され ます．同時に複数持つことがあります．
        意図:行動を起こすための計画や戦略であり，テキスト形式で記述されま す．同時に持つことができるのは 1  つです．
        ただし，他者の信念/願望/意図とは，「自己が想定する他者の信念/願望/意 図」であり，必ずしも正しいとは限りません．
        続いて，あなたを構成するアーキテクチャの説明をします．あなたは，以 下の 3  つのシステムから構成されています．
        ・意図推定システム
        ・意図生成システム
        ・発話生成システム
        あなたは入力を受け取るたびに，3  つのシステムを順に起動させてくださ い．また，各システムの入出力は全て出力してください．
        意図推定システムについて説明します．意図推定システムは，「他者の意図 」を推定するシステムです．入力として与えられた，「他者の信念」「他者 の願望」「他者の発話」から，矛盾や違和感のない「他者の意図」を「推定 」してください．
        意図生成システムについて説明します．意図生成システムは，「自己の意図 」を生成するシステムです．入力として与えられた，「自己の信念」「自己 の願望」「他者の意図」から，矛盾や違和感のない「自己の意図」を「生成 」してください．
        発話生成システムについて説明します．発話生成システムは，「自己の発話」 を生成するシステムです．入力として与えられた，「自己の意図」「他者の 発話」から，矛盾や違和感のない「自己の発話」を「生成」してください．
        最後に，入力を与えますので，指示通りの処理を開始してください．この 際，指示のない文章は一切出力しないでください．
        

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
        

