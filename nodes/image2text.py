#!/usr/bin/python
'''Image to prompt node.'''
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=unused-argument
# pylint: disable=unused-variable

# Import the Python modules.
import warnings
import hashlib
import pathlib
import time
import gc
import os

# Import the third party Python modules.
import moondream as md
import torch
import numpy as np
from PIL import Image

# Set some module strings.
__author__ = "zentrocdot"
__copyright__ = "© Copyright 2025, zentrocdot"
__version__ = "0.0.0.3"

# Disable future warning.
warnings.filterwarnings("ignore", category=FutureWarning)

# Set some paths.
SCRIPT_PATH = pathlib.Path(__file__).parent.resolve()
PARENT_PATH = SCRIPT_PATH.parent.absolute()
CUSTOM_NODES_PATH = pathlib.Path(PARENT_PATH).parent.resolve()
COMFYUI_PATH = pathlib.Path(CUSTOM_NODES_PATH).parent.resolve()
MODELS_PATH = ''.join([str(COMFYUI_PATH), "/models/moondream"])

# Read models in dir into list.
MODS = []
for f in os.listdir(MODELS_PATH):
    if f.endswith('.mf'):
        MODS.append(f)

# Create a context manager.
class ClearCache:
    '''Clear cache class.'''
    def __enter__(self):
        gc.collect()
        torch.cuda.empty_cache()

    def __exit__(self, exc_type, exc_val, exc_tb):
        gc.collect()
        torch.cuda.empty_cache()

# -------------------------------
# Convert Tensor to PIL function.
# -------------------------------
def tensor2pil(image):
    '''Tensor to PIL image.'''
    # Return a PIL image.
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# Define function.
def answer_question(model, image, prompt):
    '''Answer question function.'''
    # Create a PIL image.
    image = tensor2pil(image)
    # Initialise the return variables.
    answer = ""
    caption_s = ""
    caption_n = ""
    # Encode the image.
    encoded_img = model.encode_image(image)
    # Get answer and caption for the question.
    answer = model.query(encoded_img, prompt)["answer"].lstrip()
    caption_s = model.caption(encoded_img, length="short")["caption"].lstrip()
    caption_n = model.caption(encoded_img, length="normal")["caption"].lstrip()
    # Print results to terminal window.
    print("\nAnswer:", answer)
    print("\nCaption (short):", caption_s)
    print("\nCaption (normal):", caption_n, "\n")
    # Return the results.
    return answer, caption_s, caption_n

# Set notLOADED to True.
notLOADED = True

# Set loaded model.
LOADED_MODEL = None

# ++++++++++++++++
# Class Image2Text
# ++++++++++++++++
class Image2Text:
    '''Image2Text.'''

    #def __init__(self):
    #    self.selected_model = None
    #    self.model_loaded = False

    @classmethod
    def IS_CHANGED(cls, *args, **kwargs):
        '''Class method IS_CHNAGED.'''
        #m = hashlib.sha256().update(str(time.time()).encode("utf-8"))
        m = hashlib.sha256()
        bytes_string = str(time.time()).encode("utf-8")
        m.update(bytes_string)
        return m.digest().hex()

    @classmethod
    def INPUT_TYPES(cls):
        '''Define the node input types.'''
        return {
            "required": {
                "image": ("IMAGE",),
                "models": (MODS, {}),
            }
        }

    # Set the ComfyUI related variables.
    RETURN_TYPES = ("STRING", "STRING", "STRING",)
    RETURN_NAMES = ("answer", "clip normal", "clip long",)
    FUNCTION = "answer_a_question"
    CATEGORY = "👀 Image To Prompt"
    DESCRIPTION = "Upscaling using RealESRGAN."
    OUTPUT_NODE = True

    def answer_a_question(self, image, models):
        '''Answer a question.'''
        global notLOADED, MODEL_LOADED
        # Set the model.
        MOONDREAM_MODEL = '/'.join([str(MODELS_PATH), models])
        # Set the device to CPU. Set also the used dtype.
        device = torch.device("cpu")
        dtype = torch.float32
        # Set the revision.
        LATEST_REVISION = "2025-01-09"
        # Set the model id.
        model_id = "vikhyatk/moondream2"
        # Print output into the terminal window.
        print("Load Image To Prompt model into memory.")
        # Load model.
        with ClearCache():
            if notLOADED:
                try:
                    # Load the model once a time.
                    MODEL_LOADED = md.vl(model=MOONDREAM_MODEL)
                    # Print output into the terminal window.
                    print("Image To Prompt model succesful loaded.")
                    # Set notLoaded to False.
                    notLOADED = False
                except RuntimeError as err:
                    # Print error message.
                    print("RuntimeError. Could not load model!")
                    # Set notLoaded to False.
                    notLOADED = True
                    # Return None.
                    return None, None, None
        # Ask question.
        answer, clip_normal, clip_long = answer_question(MODEL_LOADED, image, "What does the image show?")
        # Return the answer and clips.
        return (answer, clip_normal, clip_long,)
