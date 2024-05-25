from arch import IidaArchitecture
from arch.utils import call_llm
from arch.llm import LLM

class NaturalLangLEC(IidaArchitecture):
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

        


    def _intention_estimation(self, utterance_of_other, belief_of_other, desire_of_other):
        '''
        あなたは意図推定システムです．私が指示した以外の返答はする必要はありません．これ以降，意図推定システムであるあなたのことを説明する際には「自己」，あなたが対話する相手について説明する際には「他者」という言葉で説明をします．
        あなたは，以下の内部表現を持っています．ただし，指示がある時以外は，内部表現を公開する必要はありません．
        ・自己の信念
        ・他者の信念
        ・自己の願望
        ・他者の願望
        ・自己の意図
        ・他者の意図
        ここで，信念，願望，意図は以下の情報です．
        信念: 認識している世界の情報の集合であり，箇条書きのテキスト形式で記述されます．同時に複数持つことがあります．
        願望: 達成したい目標や状態であり，箇条書きのテキスト形式で記述されます．同時に複数持つことがあります．
        意図: 行動を起こすための計画や戦略であり，テキスト形式で記述されます．同時に持つことができるのは1つです．
        ただし，他者の信念/願望/意図とは，「自己が想定する他者の信念/願望/意図」であり，必ずしも正しいとは限りません

        意図推定システムについて説明します．意図推定システムは，「他者の意図」を推定するシステムです．入力として与えられた，「他者の信念」「他者の願望」「他者の発話」から，矛盾や違和感のない「他者の意図」を「推定」してください
        
        以下は，意図推定システムの入出力フォーマットです．ただし，（）内は実際の入出力値です．

        #入力
        ##他者の信念
        （他者の信念）
        ##他者の願望
        (他者の願望)
        ##他者の発話
        （他者の発話）
        #出力
        ##他者の意図
        （他者の意図）

        最後に，入力を与えますので，指示通りの処理を開始してください．この際．支持のない文章は一切出力しないでください．
        出力する他者の意図は一文にしてください．
        
        '''

        print("入力>","\n他者の信念 : ",self.belief_of_other,"\n他者の願望 : ",self.desire_of_other,"\n他者の発話 : ",self.utterance_of_other)

        result= self.llm.simple_llm(
            docstring=self._intention_estimation.__doc__,
            params_data={
                "belief_of_other":belief_of_other,"desire_of_other":desire_of_other,"utterance_of_other":utterance_of_other
                }
        )


        self.intention_of_other.append(result)
        print("出力＞\n","他者の意図 ===> ",result)

        return result

    def _intention_generation(self, intention_of_other, belief_of_self, desire_of_self):
        '''
        あなたは意図生成システムです．私が指示した以外の返答はする必要はありません．これ以降，意図生成システムであるあなたのことを説明する際には「自己」，あなたが対話する相手について説明する際には「他者」という言葉で説明をします．
        あなたは，以下の内部表現を持っています．ただし，指示がある時以外は，内部表現を公開する必要はありません．
        ・自己の信念
        ・他者の信念
        ・自己の願望
        ・他者の願望
        ・自己の意図
        ・他者の意図
        ここで，信念，願望，意図は以下の情報です．
        信念: 認識している世界の情報の集合であり，箇条書きのテキスト形式で記述されます．同時に複数持つことがあります．
        願望: 達成したい目標や状態であり，箇条書きのテキスト形式で記述されます．同時に複数持つことがあります．
        意図: 行動を起こすための計画や戦略であり，テキスト形式で記述されます．同時に持つことができるのは1つです．
        ただし，他者の信念/願望/意図とは，「自己が想定する他者の信念/願望/意図」であり，必ずしも正しいとは限りません

        意図生成システムについて説明します．意図生成システムは，「自己の意図」を生成するシステムです．入力として与えられた，「自己の信念」「自己の願望」「他者の意図」から，矛盾や違和感のない「自己の意図」を「生成」してください        
        以下は，意図生成システムの入出力フォーマットです．ただし，（）内は実際の入出力値です．

        #入力
        ##他者の意図
        （他者の意図）
        ##自己の願望
        (自己の願望)
        ##自己の信念
        （自己の信念）
        #出力
        ##自己の意図
        （自己の意図）

        最後に，入力を与えますので，指示通りの処理を開始してください．この際．支持のない文章は一切出力しないでください．
        出力する自己の意図は一文にしてください．

        '''
        print("\n\n入力>","\n自己の信念 : ",self.belief_of_self,"\n自己の願望 : ",self.desire_of_self,"\n他者の意図 : ",self.intention_of_other)


        result = self.llm.simple_llm(
            docstring=self._intention_generation.__doc__,
            params_data={
                "belief_of_self":belief_of_self,"desire_of_self":desire_of_self,"intention_of_other":intention_of_other
                }
        )
        
        self.intention_of_self.append(result)
        print("出力＞","自己の意図 ===>",result)
        return result
    def _utterance_generation(self, utterance_of_other, intention_of_self):
        '''
        あなたは発話生成システムです．私が指示した以外の返答はする必要はありません．これ以降，発話生成システムであるあなたのことを説明する際には「自己」，あなたが対話する相手について説明する際には「他者」という言葉で説明をします．
        あなたは，以下の内部表現を持っています．ただし，指示がある時以外は，内部表現を公開する必要はありません．
        ・自己の信念
        ・他者の信念
        ・自己の願望
        ・他者の願望
        ・自己の意図
        ・他者の意図
        ここで，信念，願望，意図は以下の情報です．
        信念: 認識している世界の情報の集合であり，箇条書きのテキスト形式で記述されます．同時に複数持つことがあります．
        願望: 達成したい目標や状態であり，箇条書きのテキスト形式で記述されます．同時に複数持つことがあります．
        意図: 行動を起こすための計画や戦略であり，テキスト形式で記述されます．同時に持つことができるのは1つです．
        ただし，他者の信念/願望/意図とは，「自己が想定する他者の信念/願望/意図」であり，必ずしも正しいとは限りません

        発話生成システムについて説明します．発話生成システムは，「自己の発話」を生成するシステムです．入力として与えられた，「自己の意図」「他者の発話」から，矛盾や違和感のない「自己の発話」を「生成」してください
        以下は，発話生成システムの入出力フォーマットです．ただし，（）内は実際の入出力値です．

        #入力
        ##自己の意図
        （自己の意図）
        ##他者の発話
        (他者の発話)
        #出力
        ##自己の発話
        （自己の発話）

        最後に，入力を与えますので，指示通りの処理を開始してください．この際．支持のない文章は一切出力しないでください．
        '''
        print("\n\n入力>","\n他者の発話 : ",self.utterance_of_other,"\n自己の意図 : ",self.intention_of_self)

        result= self.llm.simple_llm(
            docstring=self._utterance_generation.__doc__,
            params_data={
                "utterance_of_other":utterance_of_other,"intention_of_self":intention_of_self
                }
        )
        
        return result
    
    def update(self, utterance_of_other):
        self.utterance_of_other.append(utterance_of_other)
        self.intention_of_other = self._intention_estimation(
            utterance_of_other, self.belief_of_other, self.desire_of_other)
        self.intention_of_self = self._intention_generation(
            self.intention_of_other, self.belief_of_self, self.desire_of_self)
        self.utterance_generation = self._utterance_generation(
            utterance_of_other, self.intention_of_self)
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
        

