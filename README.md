> [!IMPORTANT]  
> <p align="justify">🚧 This documentation is still under 
> construction. The development of the upscaler is a ongoing 
> activity. There might be small differenes in comparison of 
> node and documentation.</p>

# Preface

<p align="justify">This node is one result of my investigation
what one is able to do with Moondream. One important thing is
the Image To Prompt feature of Moondream.</p>

# Node Preview

<img src="./images/node_preview.png" alt="node preview" width="512">
<p><i>Figure 1: Node preview</i></p>

# Workflow Preview

<img src="./images/workflow_preview.png" alt="workflow preview" width="1024">
<p><i>Figure 2: Example workflow preview</i></p>

# Installation

## Model Directory

To be compatible with ComfyUI there should be a directory created in the ComfyUI directory

<pre>moondream</pre>

In this directory the Moondream models should be placed.

## Node Installation

<p align="justify">Use the ComfyUI Manager for the installation.
Search for my nick 'zentrocdot' or search for 'ComfyUI-Simple_Image_To_Prompt'.</p>

Alternative one can install the node from within the directory <code>custom_nodes</code> by

```
git clone https://github.com/zentrocdot/ComfyUI-Simple_Image_To_Prompt
```

# Troubleshooting

If one get an error message like this 

<code>ImportError: tokenizers>=0.21,<0.22 is required for a normal functioning of this module, but found tokenizers==0.20.3.</code>

after installing this node then do this

```pip install -U transformers```

# Open Issue

<p align="justify">One open issue is how to unload a loaded model.</p>

# Do-Do

Improvement of the documentation.

# References

[1] https://github.com/vikhyat/moondream/tree/main/clients/python

[2] https://moondream.ai/playground

[3] https://moondream.ai/

[4] https://github.com/vikhyat/moondream
