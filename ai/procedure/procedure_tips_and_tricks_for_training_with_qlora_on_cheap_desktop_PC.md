In this directory I will put a collection of tips and scripts that I've used to generate dataset locally and then train a model locally on that dataset.

I wanted to start training my own LoRA's after I saw that llama.cpp PR had working prototype of training working on CPU
https://rentry.org/cpu-lora
https://github.com/ggerganov/llama.cpp/pull/2632

Making your own fine-tune requires a few things to be in place before you start
- you need a model that you want to use as a base
- you need to get a dataset that will be used to communicate to the model the things you expect it to do
- you need to have access to hardware that you will use for training and a training method that will work on this hardware.

1.
For the model, I know I wanted to go with llama 2 7B model or something that would be based on that to have reasonable coherency and small size. 
If your GPU has less than 6GB of VRAM, you might want to try training some 3B OpenLLAMA/RedPajama model or phi 1.5 maybe.
Spicyboros 2.2 7B is already trained for conversations and assistant use, so I figured that
it would be easier to fine tune the response style to match Thomas Sowell than train base model to do conversations/instructions and also imitate Thomas Sowell in the same run.
Also, base llama2 7b is aligned and this could result in refusals and more AAML, which I simply don't like. Spicyboros has this handled with small de-alignment dataset. 
Great stuff.
You can find the model here https://huggingface.co/jondurbin/spicyboros-7b-2.2 . Download all files from there, you need the jsons too.
You need the have the full 16-bit model to do QLORA 4-bit training. I don't understand how it works, but using quantized model won't work.

2.
For the dataset, you need a corpus of data. I heard that you need to have 500-2000 samples at least. The more samples you have, the more time it will take to train
the model on that dataset. You probably don't want to write it down yourself entirely.
Possible strategies here are to download a big dataset and pick only a part of it to train on, building a completely synthethic dataset with a script
or creating small number of your own samples and synthetically expanding it in a way to make it more diverse but keeping the core of your manually entered samples.
Jon Durbin made great tool airoboros that can help with synthetically expanding the small dataset, I haven't used it and if it's compatible models, but it shouldn't be
too hard to fork it to use with Kobold API. My thinking was that I want to use book as the dataset, but books are just
continous strings and if you train the model on raw book corpus, it will maybe allow you to write a similar book in the story mode in kobold.cpp, but it won't give you
answer to question that could be answered by someone who read the book. For this, we need to transform the data from basic continous monologue to discussion where we have
the name of the person who asks the question, followed by question, followed by newline and name of the person who responded to the question and an answer to the question.
I've used this script as a base for my script https://pastebin.com/4DTKWpmY
TODO