from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import Config
from pycallgraph import GlobbingFilter

#import torch.nn as nn
from torch.nn.modules.module import Module


config = Config()
config.trace_filter = GlobbingFilter(include=[
        'torch.nn.modules.module.Module.parameters',
        'torch.nn.modules.module.Module.named_parameters',
        'torch.nn.modules.module.Module._named_members',
        'torch.nn.modules.module.Module.named_modules'
    ])
graphviz = GraphvizOutput()
graphviz.font_size=10
graphviz.group_font_size=10
graphviz.output_file = 'graph.png'
with PyCallGraph(output=graphviz, config=config):
    mod=Module()
    for item in mod.parameters():
        pass