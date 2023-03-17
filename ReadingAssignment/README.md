# NLP-Assignment

## Reading 1
### Reference: Structural Characterization for Dialogue Disentanglement
### Link: https://aclanthology.org/2022.acl-long.23.pdf
Date: 31/01/2023
| Topic        | Structural Characterization for Dialogue Disentanglement |
|--------------|--------------------------------------------------------------------------------------------------------|
| Problem   | - It can be challenging for a new participant to understand the previous chatting log due to multi-party dialogues always exhibit disorder and complication (for example: consistency and continuity are broken by tangled reply-to dependencies between non-adjacent utterances). <br /> - In other word, there are little attentions that paid to the characteristics of dialogues. |
| Key Related Work | - Providing contextualized backbones with Pre-trained Language Models (PrLMs). <br /> - Early works in Dialogue Disentanglement can be summarized as feature encoder and clustering algorithms to predict whether a pair of utterances are alike or different. <br /> - Then end-to-end approach is proposed by mapping the states of each dialogue thread with clustered utterances. |
| Solution     | - Apply speaker-aware and reference-aware (characteristic features) for the motivation of disentanglement based on the fact that dialogues are developed according to the behavior of speakers (incorporates dialogue-specific characters). <br /> - In detail, following by two highlights: Firstly, speaker properties of each utterance and secondly, reference of speakers between utterances. |
| Result       | Speaker and dependency-aware deserve to be studied more in multi-turn dialogue modeling, because it achieves superior performance on most metrics which compared to previously proposed models (for example: Ptr-Net, DialBERT, Elsner,...) with the using of a large scale multi-party dialogue log dataset Ubuntu IRC. |


## Reading 2
### Reference: PLOME: Pre-training with Misspelled Knowledge for Chinese Spelling Correction
### Link: https://aclanthology.org/2021.acl-long.233.pdf
Date: 13/02/2023
| Topic        | PLOME: Pre-training with Misspelled Knowledge for Chinese Spelling Correction |
|--------------|--------------------------------------------------------------------------------------------------------|
| Problem   | - Correcting spelling in the Chinese language is a complex task due to the abundance of homonyms, where words that are pronounced similarly can have vastly different meanings, and even a minor spelling mistake can alter the intended meaning of a word. <br /> - Furthermore, Chinese spelling correction systems commonly experience inadequate performance, especially when dealing with misspellings that occur in the real world, such as typing and pronunciation errors. Besides, these systems only receive training from a restricted amount of correctly spelled data, and do not include information about misspelled words in their training regimen. |
| Key Related Work | - Early work on CSC followed the pipeline of error identification, candidate generation and selection. <br /> - Some researchers focused on unsupervised approaches, which typically adopted a confusion set to find correct candidates and employed language model to select the correct one. <br /> - Discriminative sequence tagging methods and sequence-to-sequence generative models were deloyed to cope with the correction on the input sentence. |
| Solution     | - Propose a new pre-training method called PLOME (Pre-training with Misspelled Knowledge), which includes knowledge of misspelled words into its pre-training phase. <br /> - Besides, PLOME leverages GRU networks to model knowledge of phonology and visual similarity based on the phonetics and stroke structure of characters. <br /> - Moreover, PLOME also incorporates pronunciation prediction to acquire misspelled knowledge on a phonetic level. |
| Result       | - The PLOME approach proposed in the paper outperforms existing state-of-the-art Chinese spelling correction systems, indicating the effectiveness of incorporating misspelled knowledge into the pre-training process. <br /> - In addition, PLOME is the first model to make decisions by jointly considering both the target pronunciation and character distributions, making it a unique and innovative approach to Chinese spelling correction. |


## Reading 3
### Reference: Attention Is All You Need
### Link: https://arxiv.org/pdf/1706.03762.pdf
Date: 28/02/2023
| Topic        | Attention Is All You Need |
|--------------|--------------------------------------------------------------------------------------------------------|
| Problem   | - Previous state-of-the-art sequence-to-sequence models that utilized recurrent or convolutional neural networks faced two significant challenges: high computational cost and slow training. <br /> - Fore more detail, they struggled to handle longer sequences due to their sequential nature, which made it difficult to parallelize the computations. As a result, these issues hindered the effective performance of these previous models. |
| Key Related Work | - Language modeling and machine translation. <br /> - Factorization tricks and conditional computation. <br /> - Attention mechanisms which mostly combined with a recurrent network have been used before as a part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences. |
| Solution     | - Propose a new simple network architecture, the Transformer, which based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. <br /> - By employing a self-attention mechanism, the Transformer architecture simultaneously computes contextualized representations of every position in the input sequence. |
| Result       | - This new architecture has efficient computation and the ability to handle longer sequences, leading to significant improvements in both training speed and model performance. <br /> - It also achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. <br /> - In addition, on the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs. <br /> - Moreover, the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.  |


## Reading 4
### Reference: BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension
### Link: https://aclanthology.org/2020.acl-main.703.pdf
Date: 13/03/2023
| Topic        | BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension |
|--------------|--------------------------------------------------------------------------------------------------------|
| Problem   | - To cope with corrupted text on various noising functions. |
| Key Related Work | - Devlin et al. (2019) introduced the concept of masked language modelling called BERT, which enabled pre-training models to learn in a manner similar to BART. <br /> - Yang et al. (2019) extended BERT's capabilities by training models to predict masked tokens in a permuted order, resulting in the XL-Net architecture. <br /> - Raffel et al. (2019) introduced a pre-trained denoising sequence-to-sequence model, T5, which used a similar range of noising tasks to BART. <br /> - Dong et al. (2019) fine-tuned BERT with an ensemble of masks, including some that only allowed leftward context, resulting in the UniLM model.  |
| Solution     | - Propose a new pre-training method based on the transformer architecture. BART which stands for Bidirectional and Auto-Regressive Transformer is designed to pre-train models for a variety of natural language processing tasks, including text generation, translation, summarization, and comprehension. <br /> - BART is a bidirectional model that can encode the entire input sequence and use the entire sequence to generate each output token as well as it can generate each output token based on the previously generated tokens. |
| Result       | - Particularly effective when fine tuned for text generation but also works well for comprehension tasks. <br /> - Achieves new state of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks, with gains of up to 3.5 ROUGE. BART. <br /> - In addition, provides a 1.1 BLEU increase over a back-translation system for machine translation, with only target language pretraining.  |
