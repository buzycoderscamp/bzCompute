from bzCompute.error import Exception
from bzCompute.graph import *
from bzCompute.algorithms import DFS, Postorder
from bzCompute.KernelOperations import *
from bzCompute.runtime.session import SequentialSession
from bzCompute.runtime.domain_decomposition import MasterSession

#string processing modules :


import bzCompute.text_processing.graph  as text 
import bzCompute.text_processing.StringOperations as text_ops 
from bzCompute.runtime.string_session import StringSession


default_graph = Graph()

string_default_graph = text.Graph()

string_default_graph.create_graph()

default_graph.create_graph()

def get_default_graph():

    return default_graph

def get_default_string_graph() :

    return string_default_graph