#!/usr/bin/python
'''Object detection node.'''
# pylint: disable=no-member
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=too-many-positional-arguments
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals

# Import the Python modules.
from typing import Any
from server import PromptServer

class AnyType(str):
    '''A special class that is always equal in not equal comparisons.'''

    def __ne__(self, __value: object) -> bool:
        return False

# Instantiate AnyType
anyType = AnyType("*")

def updateDataWidget(node, widget, text):
    '''Raises an event to update a widget's data.'''
    PromptServer.instance.send_sync("zentrocdot.data_updater.node_processed",
                                    {"node": node, "widget": widget, "text": text})

class ShowData:
    '''A node that takes any value and displays it as a string.
    '''

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": (anyType, {"forceInput": True}),
                "data": ("STRING", {"default": "", "multiline": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
            },
        }

    RETURN_TYPES = ()
    INPUT_IS_LIST = (True,)
    OUTPUT_NODE = True

    CATEGORY = "👀 Image To Prompt"
    FUNCTION = "process_data"

    def process_data(self, input, data, unique_id):
        displayText = self.render_data(input)
        updateDataWidget(unique_id, "data", displayText)
        return {"ui": {"data": displayText}}

    def render_data(self, input):
        '''Render data.'''
        output = ""
        listlen = len(input)
        if not isinstance(input, list):
            output = str(input)
        elif listlen == 0:
            output = ""
        elif listlen == 1:
            output = str(input[0])
        else:
            for i, element in enumerate(input):
                output += f"{str(input[i])}\n"
            output = output.strip()
        return output
