from dataclasses import dataclass, field
from typing import Optional, Dict

Message = dict[str, str]  # keys role, content
MessageList = list[Message]

__all__ = ['Message', 'MessageList', 'Templates', 'SamplerBase', 'EvalResult', 'SingleEvalResult', 'Eval']

Templates = {
    'base': "{task_template}",

    'meta-chat': "[INST] {task_template} [/INST]",

    'vicuna-chat': "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: {task_template} ASSISTANT:",

    'lwm-chat': "You are a helpful assistant. USER: {task_template} ASSISTANT: ",

    'command-r-chat': "<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{task_template}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>",

    'chatglm-chat': "[gMASK]sop<|user|> \n {task_template}<|assistant|> \n ",
    
    'glm-4-chat': "[gMASK]<sop><|user|>\n{task_template}<|assistant|>",
    
    'tgi-glm-4-chat': "<|user|>\n{task_template}<|assistant|>",
    
    'RWKV': "User: hi\n\nAssistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it\n\nUser: {task_template}\n\nAssistant:",
}

class SamplerBase:
    """
    Base class for defining a sampling model, which can be evaluated,
    or used as part of the grading process.
    """

    def __call__(self, message_list: MessageList) -> str:
        raise NotImplementedError


@dataclass
class EvalResult:
    """
    Result of running an evaluation (usually consisting of many samples)
    """

    score: Optional[float] = None   # top-line metric
    metrics: Optional[Dict[str, float]] = None  # other metrics


@dataclass
class SingleEvalResult:
    """
    Result of evaluating a single sample
    """

    score: Optional[float] = None  # top-line metric
    metrics: Dict[str, float] = field(default_factory=dict)  # other metrics with default empty dict


class Eval:
    """
    Base class for defining an evaluation.
    """

    def __call__(self, sampler: SamplerBase) -> EvalResult:
        raise NotImplementedError
