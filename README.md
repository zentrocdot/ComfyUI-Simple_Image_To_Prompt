> [!IMPORTANT]  
> <p align="justify">🚧 This documentation is still under construction.
> Parts of the node are still under development. There may therefore be
> minor differences between the node itself and the documentation for
> the node. The documentation is also not yet complete.</p>

# Preface

<p align="justify">This node is one result of my investigation
what one is able to do with Moondream. One important thing is
the Image To Prompt feature of Moondream.</p>

# Motivation

<p align="justify">Image To Prompt can be used in different ways. 
One can get an idea how to change or improve a Prompt by suggestions 
from Image To Prompt. It is also possible to get informations about 
the art and style of the image. This can be helpful to get the right 
key words for further work.</p>

# Introductory Words

<p align="justify">The node is using the CPU and not the GPU. First 
way, the proposed one, can be done with Moon dream directly. For the
second way one needs Huggingface.</p>

<p align="justify">In the first versions of the node the model cannot
be selected. At the moment there are four models available. In one of
the following versions I will add the support for all of the four models.</p>

<p align="justify">In the future I need something like a download node,
which should be offer the possibility to download and monitor the process
of the download in the node and not in the terminal window.</p>

# Prerequisites

Download the Moon dream model

https://huggingface.co/vikhyatk/moondream2/resolve/9dddae84d54db4ac56fe37817aeaeb502ed083e2/moondream-2b-int8.mf.gz

and unzip it to

<p align="justify">a folder called moondream to be created in the directory tree</p>

<pre>ComfyUI/models</pre>

<p align="justify">In this directory all other models from checkpoint
over LoRAs to upscaler models. So it is the best way to place a model.</p>

# Node Preview

<p align="justify">Figure 1 shows a preview of the node. Over the 
connector on the left side one can load the image of interest. The
connectors on the right side have as output</p>

* Answer (to a question or Prompt)
* Short caption
* Normal caption

<img src="./images/node_preview.png" alt="node preview" width="512">
<p><i>Figure 1: Node preview</i></p>

<p align="justify">The current Version allows to ask a question which is not given by
the fixed one from the implemented source code</p>

<code>What does the image show?</code>

<p align="justify">Like I have done it in the example workflow one should output all three
to get the best answer or caption for each case.</p>

<p align="justify">One can ask what one likes to do e.g.</p>

+ What do we see in the image?
+ What is the art style of the image?
+ What is the story behind the image?

and so on.

# Workflow Preview

<p align="justify">Figure 2 shows the simple case of a workflow. From my point of view it
is not helpful to create in an automatic way new images from the given 
answer or caption.</p>

<img src="./images/workflow_preview.png" alt="workflow preview" width="1024">
<p><i>Figure 2: Example workflow preview</i></p>

<p align="justify">Read the next section why I do not propose to use a automatic image generation.</p>

What the Workflow/Node Does

<p align="justify">Each time one let run the workflow Moon dream is generating
a new answer. No two answers will be the same. This way it make sense to run the
workflow different times untill one get an answer which one likes more than an
other answer.</p>

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

## Error Message

<p align="justify">If one get an error message like this</p> 

<code>ImportError: tokenizers>=0.21,<0.22 is required for a normal functioning of this module, but found tokenizers==0.20.3.</code>

<p align="justify">one can fix this error message easily.</p>

## Error Fixing 
  
<p align="justify">After installing of this node one has to do</p> 

```pip install -U transformers```

<p align="justify">and the error message is gone.</p> 

## General Solution

<p align="justify">By changing the <code>requirements.txt</code>
this error should no longer occur.</p> 

# Open Issue

<p align="justify">The one and only open issue is how to unload a loaded
Moondream model. Memory is locked after loading a model independend if the
workflow with the node is open or closed.</p>

<p align="justify">Not being able to unload the model from memory is a serious
problem if you want to use Moondream in this way.</p>

# Do-Do

<p align="justify">Improvement of this documentation.</p> 

<p align="justify">The open issue that I did not found a way to unload
a loaded model makes much more test runs necessary.</p>

<p align="justify">The algorithm I found for Image To Prompt using Moondream
works well for the moment. Some other approaches I tried before not. It has
to be tested if the current approach works well under different conditions all
the time.</p>

# Conclusion

<p align="justify">I am on the way to finishing the work on this node. The
node does what the node should be. For my work the node in the current state
is sufficient.</p> 

# Remark

<p align="justify">If one needs an improvment of this node, feel free to make
a donation. Tell me what you need. I will take a look if it is possible. </p> 

# References

[1] https://github.com/vikhyat/moondream/tree/main/clients/python

[2] https://moondream.ai/playground

[3] https://moondream.ai/

[4] https://github.com/vikhyat/moondream

[5] https://www.copus.io/work/474668694161482d83005265199b4995?spaceId=zentrocdotsposts
