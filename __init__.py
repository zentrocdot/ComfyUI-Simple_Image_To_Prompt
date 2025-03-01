'''RealEsrganUpscaler __init__ file.'''

# Import the Python modules.
from .nodes.image2text import *
from .nodes.image2text_noupdate import *
from .nodes.show_data import *

NODE_CLASS_MAPPINGS = { 
    "👁️ Image To Prompt": Image2Text,
    "👁️ Image To Prompt (NO UPDATE)": Image2Text_NoUpdate,
    "🧳 Show Data": ShowData,
    }
    
WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

# Print message into the terminal window.
print("\033[34mComfyUI RealEsrganUpscaler Nodes: \033[92mLoaded\033[0m")
