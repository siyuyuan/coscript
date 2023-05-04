# Coscript

Resources for our ACL 2023 paper: Distilling Script Knowledge from Large Language Models for Constrained Language Planning

# Ethics Statement
## Covered Domains in Coscript
Coscript is derived from wikiHow and encompasses 15 daily life goal categories. These categories cover a wide range of practical aspects of everyday life. 
However, it is important to emphasize that sensitive and high-risk domains, including medical, legal, and high-stakes financial advice, are excluded from the dataset to minimize potential risks related to inaccurate or misleading information. 
Researchers and developers can leverage this dataset to build models that accurately understand and respond to user queries on various non-sensitive, non-critical topics.


## Factuality and Biases
We recognize that the factuality of generated content is crucial, especially in high stakes scenarios. 
Therefore, during the validation and testing phases, annotators manually verify the adherence of generated scripts to constrained goals. 
They also assess and revise the content to minimize hallucinations, factual errors, and any inappropriate or misleading information, which helps ensure that the generated content is reliable and of high quality.
Furthermore, we annotated the limitations section regarding data distribution bias favoring causal LMs and took steps to manually correct the dev and test sets to mitigate this bias. 



## Toxic Contents
Previous work found that language models (including GPT-3s) may generate toxic contents.
It is crucial to emphasize that our dataset is not intended for safety-critical applications or as a substitute for expert advice in sensitive domains. 
Annotators are specifically instructed to discard offensive and harmful data during the review of the Coscript. 
Despite these precautions, there may still be some prejudicial data that goes unnoticed in our final dataset. 
However, the likelihood of harmful content has been minimized through the manual correction of the validation and test sets by the annotators. 


## Intended Use-Cases
Coscript is primarily designed to advance research and applications in natural language understanding and generation, with a particular focus on language planning in daily life scenarios. 
While the dataset is comprehensive, it remains crucial that its usage remains focused on non-critical and non-sensitive domains. Coscript is not intended for safety-critical applications or as a substitute for expert advice in sensitive areas such as medical, legal, and financial decision-making. 
By ensuring these boundaries are respected and by providing clear reminders of usage safety, Coscript aims to contribute positively to ongoing advancements in AI research and applications while minimizing potential risks and ethical concerns.
