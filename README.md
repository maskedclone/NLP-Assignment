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
| Key Related Work | - Providing contextualized backbones with Pre-trained Language Models (PrLMs). <br /> - Early works in Dialogue Disentanglement can be summarized as feature encoder and clustering algorithms to predict whether a pair of utterances are alike or different. <br /> - Then end-to-end approach is proposed by mapping the states of each dialogue thread with clustered utterances. |
| Solution     | - Propose a new pre-training method called PLOME (Pre-training with Misspelled Knowledge), which includes knowledge of misspelled words into its pre-training phase. <br /> - Besides, PLOME leverages GRU networks to model knowledge of phonology and visual similarity based on the phonetics and stroke structure of characters. <br /> - Moreover, PLOME also incorporates pronunciation prediction to acquire misspelled knowledge on a phonetic level. |
| Result       | Speaker and dependency-aware deserve to be studied more in multi-turn dialogue modeling, because it achieves superior performance on most metrics which compared to previously proposed models (for example: Ptr-Net, DialBERT, Elsner,...) with the using of a large scale multi-party dialogue log dataset Ubuntu IRC. |
