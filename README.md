# story-experiments
Experiments using story datasets

# Datasets
| Dataset   | Desciption                                                | Links |
| ------ | ------------------------------------------------------------ | ----- |
| TRIPOD    | Turning Point annotated dataset (Synopsis, Screenplay)  | https://github.com/ppapalampidi/TRIPOD
| CMU Movie Summary    |   |    |
| StoryCommonsense    |   |     |
| WritingPrompts    | Short stories collected from Reddit. (Prompt,Story) Pairs  |   |

<!-- * TRIPOD 
    * Turning Point annotated dataset (Synopsis, Screenplay)
    * https://github.com/ppapalampidi/TRIPOD
* CMU Movie Summary
* StoryCommonsense
* WritingPrompts
    * Short stories collected from Reddit
    * (Prompt,Story) Pairs -->

# Experiments
## 2021.06
| Folder   | Description                                                |
| ------ | ------------------------------------------------------------ |

## 2021.05
| Folder   | Description                                                |
| ------ | ------------------------------------------------------------ |
| TRIPOD_processing  | Process TRIPOD with Coreference Resolution, Semantic Role Labeling. <ul><li>Protagonist Identification</li><li>Process to <s,r,o> tuples for COMET input</li></ul>     |
| C2PO_TRIPOD  | Test forward, backward branching with COMET models & calculate path probability <ul><li>forward, backward branching</li><li>Retrieve relevant knowledge tuples using SentenceBERT</li></ul>   |
| CAST_pairs  | Test various sentences with relation pairs mentioned in CAST. Mainly test pair related to intentions  |
| Modeling_suspense | Test the provided model at official [repo](https://github.com/dwlmt/Story-Untangling)    |
<!-- ### TRIPOD Processing
Process TRIPOD with Coreference Resolution, Semantic Role Labeling.
* Protagonist Identification with Coref Models
* Process to <s,r,o> tuples for COMET input

### C2PO using TRIPOD
1. Test forward, backward branching with COMET models
    - Create path using C2PO branching implementation
        - https://github.com/rajammanabrolu/C2PO/blob/master/C2PO/scripts/text-gen/generate.py
    - Calculate path probability
2. Retrieve relevant knowledge tuples using SentenceBERT models -->

<!-- ### CAST Relation Pair Inferences
Test various sentences with relation pairs mentioned in CAST.
Mainly test pair related to intentions
* \<oWant> - \<xIntent> -->

# References
* TRIPOD
* C2PO
* CAST
* COMET
* [Modelling Suspense in Short Stories as Uncertainty Reduction over Neural Representation](https://www.aclweb.org/anthology/2020.acl-main.161/)