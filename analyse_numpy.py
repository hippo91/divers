"""
Inspect numpy module to locate functions

:note: should be run from the directory just above numpy sources
"""
import inspect
import numpy
from collections import OrderedDict
import sys
from typing import Dict, Callable


def get_builtins() -> Dict[str, Callable]:
    return dict(inspect.getmembers(numpy, inspect.isbuiltin))

def get_functions() -> Dict[str, Callable]:
    return dict(inspect.getmembers(numpy, inspect.isfunction))

def get_module_members(module_name: str) -> Dict[str, Callable]:
    res = {
        name: func 
        for name, func in get_builtins().items()
        if inspect.getmodule(func).__name__ == module_name
        }
    res.update({
        name: func
        for name, func in get_functions().items()
        if inspect.getmodule(func).__name__ == module_name
    })
    return OrderedDict((k, v) for k,v in sorted(res.items()))

def write_signature(parameters) -> str:
    atomic_params = []
    for name, param in parameters.items():
        sign = name
        if param.default != inspect._empty:
            sign += "={}".format(param.default)
        atomic_params.append(sign)
    return ", ".join(atomic_params)
        
def get_return(func):
    doc = inspect.getdoc(func).split('\n')
    for line in doc:
        if line.startswith('out : '):
            return line[6:]


if __name__ == "__main__":
    for func_name, func in get_module_members('numpy.core.{}'.format(sys.argv[1])).items():
        try:
            params = inspect.signature(func).parameters
            signature_ = write_signature(params)
        except ValueError:
            signature_ = ""
        print("def {}({}): return {}".format(func_name, signature_, get_return(func)))