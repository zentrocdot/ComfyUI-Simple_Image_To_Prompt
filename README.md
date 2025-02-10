> [!IMPORTANT]  
> <p align="justify">🚧 This documentation is still under 
> construction. The development of the node is a little bit
> ongoing. There might be small differenes in comparison of 
> node and documentation.</p>

# Preface

<p align="justify">This node is one result of my investigation
what one is able to do with Moondream. One important thing is
the Image To Prompt feature of Moondream.</p>

# Motivation

Image To Prompt can be used in different ways. One can get an
idea how to change or improve a Prompt by suggestions from Image
To Prompt. It is also possible to get informations about the art
and style of the image. This can be helpful to get the right key
words for further work.

# Introductory Words

The node is using the CPU and not the GPU. First way, the proposed one,
can be done with Moon dream directly. For the second way one needs 
Hugging face.

In the first versions of the node the model cannot be selected. At the moment
there are four models available. In one of the following versions I will add the
support for all of the four models.

In the future I need something like a download node, which should be offer the 
possibility to download and monitor the process of the download in the node and
not in the terminal window.

# Prerequisites

Download the Moon dream model

https://huggingface.co/vikhyatk/moondream2/resolve/9dddae84d54db4ac56fe37817aeaeb502ed083e2/moondream-2b-int8.mf.gz

and unzip it to

a folder called moondream to be created in the directory tree

ComfyUI/models

In this directory all other models from checkpoint over LoRAs to upscaler models. So it is the best way to place a model.

# Node Preview

Figure 1 shows a preview of the node. Over the connector on
the left side one can load the image of interest. The connectors 
on the right side have as output

* Answer (to a question or Prompt)
* Short caption
* Normal caption

<img src="./images/node_preview.png" alt="node preview" width="512">
<p><i>Figure 1: Node preview</i></p>

The current Version allows to ask a question which is not given by
the fixed one from the implemented source code

<code>What does the image show?</code>

Like I have done it in the example workflow one should output all three
to get the best answer or caption for each case.

One can ask what one likes to do e.g.

+ What do we see in the image?
+ What is the art style of the image?
+ What is the story behind the image?

and so on.

# Workflow Preview

Figure 2 shows the simple case of a workflow. From my point of view it
is not helpful to create in an automatic way new images from the given 
answer or caption.

<img src="./images/workflow_preview.png" alt="workflow preview" width="1024">
<p><i>Figure 2: Example workflow preview</i></p>

Read the next section why I do not propose to use a automatic image generation.

What the Workflow/Node Does

Each time one let run the workflow Moon dream is generating a new answer. 
No two answers will be the same. This way it make sense to run the workflow
different times untill one get an answer which one likes more than an other
answer.

# Installation

## Model Directory

<p align="justify">To be compatible with ComfyUI there should be a directory created in the ComfyUI directory</p>

<pre>moondream</pre>

<p align="justify">In this directory the Moondream models should be placed.</p>

## Node Installation

<p align="justify">Use the ComfyUI Manager for the installation.
Search for my nick 'zentrocdot' or search for 'ComfyUI-Simple_Image_To_Prompt'.</p>

<p align="justify">Alternative one can install the node from within the directory <code>custom_nodes</code> by</p>

```
git clone https://github.com/zentrocdot/ComfyUI-Simple_Image_To_Prompt
```

# Troubleshooting

<p align="justify">If one get an error message like this</p> 

<code>ImportError: tokenizers>=0.21,<0.22 is required for a normal functioning of this module, but found tokenizers==0.20.3.</code>

<p align="justify">after installing this node then do this</p> 

```pip install -U transformers```

# Open Issue

<p align="justify">The one and only open issue is how to unload a loaded
model. Memory is locked after loading a model independend if the workflow
with the node is open or closed.</p>

# Do-Do

Improvement of the documentation. 

The open issue that I did not found a way to unload a loaded model makes 
much more test runs necessary.

The algorithm I found works well for the moment. Some approaches I tried
before not. This has to be tested if this approach works all the time.

Dependencies while installation have to be checked to prevent the error message 
from the last section. In the past I solved this problem for my other programs.

# References

[1] https://github.com/vikhyat/moondream/tree/main/clients/python

[2] https://moondream.ai/playground

[3] https://moondream.ai/

[4] https://github.com/vikhyat/moondream
