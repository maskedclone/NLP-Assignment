# Topic: A Fast and Accurate Dependency Parser using Neural Networks
### https://aclanthology.org/D14-1082.pdf

#### Problem:  encoding all the available information from the configuration and modeling higher-order features based on the dense representations.
#### Solution: <br/> - new way for learning a neural network classifier for use in a greedy, transition-based dependency parse. <br/> - a neural network classifier to make parsing decisions within a transition-based dependency parser.
#### Result: <br/>- outperforms other greedy parsers using sparse indicator features in both accuracy and speed. <br/>- for detail, parsing more than 1000 sentences per second at 92.2% unlabeled attachment score on the English Penn Treebank. <br/>- 2% improvement in unlabeled and labeled attachment scores onboth English and Chinese datasets
