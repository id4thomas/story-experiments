# Modeling Suspense Experiment

## Experiment
Clone code & provided model weights from [repo](https://github.com/dwlmt/Story-Untangling).
Try model inference using TRIPOD data

### Included Files
* ```tripod_prepare.py``` Selects sample synopses from test set into a text file
* ```reader.json``` Separated reader params into separate files (put in ```examples_models_and_data``` folder)
* ```predict.ipynb``` Model prediction examples

### Analyzed Files
* ```story_untangling/dataset_readers/writing_prompts_whole_story.py```
    * AllenNLP DatasetReader used for reading WritingPrompts
* ```story_untangling/models/uncertain_reader.py```
    * Main model file

### Notes
#### AllenNLP Iterators
* AllenNLP version is based on 0.8.5 which contains Iterators.
    Iterators is deprecated as of version 1.0 [Release Note](https://github.com/allenai/allennlp/releases?after=v1.0.0rc3)
    Referenced code at allennlp [0.8.4](https://github.com/allenai/allennlp/tree/v0.8.4) for debugging.

#### Model trained in 50 sentences chunks
Batch chunking part from ```_read``` function in ```story_untangling/dataset_readers/writing_prompts_whole_story.py```
```
for sentence_batch in list(more_itertools.chunked(sentences, self._story_chunking)):
    # Filter out non English and gibberish sentences.

    yield self.text_to_instance(sentence_batch, story, db=db, batch_num=batch_num)
    batch_num += 1
```
```story_chunking``` parameter is set as 50 in model training param ```experiments/uncertain_reader/lstm_fusion_big_full_experiment.json```
## References
[Modelling Suspense in Short Stories as Uncertainty Reduction over Neural Representation](https://www.aclweb.org/anthology/2020.acl-main.161/)