# story-experiments
Experiments using story datasets

# Datasets
* TRIPOD 
    * Turning Point annotated dataset (Synopsis, Screenplay)
    * https://github.com/ppapalampidi/TRIPOD
* CMU Movie Summary
* StoryCommonsense
* WritingPrompts
    * Short stories collected from Reddit
    * (Prompt,Story) Pairs

# Experiments
## 2021.05 TRIPOD Processing
Process TRIPOD with Coreference Resolution, Semantic Role Labeling.
* Protagonist Identification with Coref Models
* Process to <s,r,o> tuples for COMET input

## 2021.05 C2PO using TRIPOD
Test forward, backward branching with COMET models

## 2021.05 Knowledge Tuple Retrieval
Retrieve relevant knowledge using SentenceBERT models

## 2021.05 CAST Relation Pair Inferences
Test various sentences with relation pairs mentioned in CAST.
Mainly test pair related to intentions
* \<oWant> - \<xIntent>

# References
TRIPOD
C2PO
CAST
COMET