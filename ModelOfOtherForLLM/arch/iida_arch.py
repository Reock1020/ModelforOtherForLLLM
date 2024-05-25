
import abc

class IidaArchitecture(metaclass=abc.ABCMeta):

    """
    IidaArchitectureクラスは、相手の発話意図に基づく言外の意味を察した対話を行うためのアーキテクチャです。

    :param belief_of_self: 自己の信念を表す文字列の配列
    :param desire_of_self: 自己の欲求を表す文字列の配列
    :param intention_of_self: 自己の意図を表す文字列
    :param utterance_of_self: 自己の発話を表す文字列
    :param belief_of_other: 他者の信念を表す文字列の配列
    :param desire_of_other: 他者の欲求を表す文字列の配列
    :param intention_of_other: 他者の意図を表す文字列
    :param utterance_of_self: 他者の発話を表す文字列
    """

    def __init__(self, belief_of_self, desire_of_self,
                 belief_of_other, desire_of_other):
        self.belief_of_self = belief_of_self
        self.desire_of_self = desire_of_self
        self.belief_of_other = belief_of_other
        self.desire_of_other = desire_of_other

        self.intention_of_self = []
        self.intention_of_other = []


    @abc.abstractmethod
    def _intention_estimation(self, utterance_of_other,
                              belief_of_other, desire_of_other):
        """
        この関数は、他者の発話(utterance_of_other)、他者の信念(belief_of_other、他者の欲求(desire_of_other)から、
        推定される他者の意図(intention_of_other)を返します。

        :param utterance_of_other: 文字列
        :param belief_of_other: 文字列の配列
        :param desire_of_other: 文字列の配列
        :return self.intention_of_other: 文字列                      
        """

        # TODO: 推定される他者の意図を計算し、self.intention_of_otherに格納

        return self.intention_of_other

    @abc.abstractmethod
    def _intention_generation(self, intention_of_other,
                              belief_of_self, desire_of_self):
        """
        この関数は、他者の意図(intention_of_other)、自己の信念(belief_of_self、自己の欲求(desire_of_self)から、
        自己の意図(intention_of_self)を返します。

        :param intention_of_other: 文字列
        :param belief_of_self: 文字列の配列
        :param desire_of_self: 文字列の配列
        :return self.intention_of_self: 文字列                      
        """

        # TODO: 自己の意図を計算し、self.intention_of_selfに格納        

        return self.intention_of_self

    @abc.abstractmethod
    def _utterance_generation(self, utterance_of_other, intention_of_self):
        """
        この関数は、他者の発話(utterance_of_other)、自己の意図(intention_of_selfから、
        自己の発話(utterance_of_self)を返します。

        :param utterance_of_other: 文字列
        :param intention_of_self: 文字列
        :return utterance_of_self: 文字列                      
        """

        # TODO: 自己の発話を計算し、self.utterance_of_selfに格納

        return self.utterance_of_self
        
        
    def update(self, utterance_of_other):
        self.intention_of_other = self._intention_estimation(
            utterance_of_other, self.belief_of_other, self.desire_of_other)
        self.intention_of_self = self._intention_generation(
            self.intention_of_other, self.belief_of_self, self.desire_of_self)
        self.utterance_generation = self._utterance_generation(
            utterance_of_other, self.intention_of_self)
        return self.utterance_generation

    def __call__(self, utterance_of_other):
        return self.update(utterance_of_other)