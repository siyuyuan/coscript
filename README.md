# Coscript

Resources for our ACL 2023 paper: Distilling Script Knowledge from Large Language Models for Constrained Language Planning

## Dataset Format

Each data entry in the dataset is a JSON object containing the following fields:

- `id`: A unique integer identifier for the data sample
- `Abstract Goal`: A goal with prototypical scripts
- `Specific Goal`: inherits from an abstract one but with new information as a constraint to limit the scope.
- `Constraint`: Any constraint or condition related to the specific goal
- `Script`: An ordered list of steps to achieve the specific goal
- `Category`: The category the goal belongs to

### Example Data Entry

Here's an example data entry from the dataset:

```json
{
  "id": 42415,
  "Abstract Goal": "Make a Studio",
  "Specific Goal": "Make a Studio for Photography",
  "Constraint": "for Photography",
  "Script": [
    "1. Choose a room with lots of natural light.",
    "2. Clear out the room.",
    "3. Cover the windows with blackout curtains.",
    "4. Install diffusers and/or reflectors.",
    "5. Set up your backdrop.",
    "6. Set up your lighting.",
    "7. Set up your camera.",
    "8. Start shooting!"
  ],
  "Category": "Arts and Entertainment"
}
```


## Ethics Statement
### Covered Domains in Coscript
Coscript is derived from wikiHow and encompasses 15 daily life goal categories. These categories cover a wide range of practical aspects of everyday life. 
However, it is important to emphasize that sensitive and high-risk domains, including medical, legal, and high-stakes financial advice, are excluded from the dataset to minimize potential risks related to inaccurate or misleading information. 
Researchers and developers can leverage this dataset to build models that accurately understand and respond to user queries on various non-sensitive, non-critical topics.

### wikiHow Source
The content available on wikiHow is shared under a Creative Commons License (CC-BY-NC-SA)1, which permits others to share, copy, distribute, and adapt the content for non-commercial purposes. In our research, we use wikiHow as an initial dataset for providing examples to construct our dataset. Our dataset is released on GitHub and is only used to advance academic research on language planning with more complex and diverse goals and constraints. Therefore, we emphasize that our usage aligns with the requirements under the license.

### Factuality and Biases
We recognize that the factuality of generated content is crucial, especially in high stakes scenarios. 
Therefore, during the validation and testing phases, annotators manually verify the adherence of generated scripts to constrained goals. 
They also assess and revise the content to minimize hallucinations, factual errors, and any inappropriate or misleading information, which helps ensure that the generated content is reliable and of high quality.
Furthermore, we annotated the limitations section regarding data distribution bias favoring causal LMs and took steps to manually correct the dev and test sets to mitigate this bias. 

### Toxic Contents
Previous work found that language models (including GPT-3s) may generate toxic contents.
It is crucial to emphasize that our dataset is not intended for safety-critical applications or as a substitute for expert advice in sensitive domains. 
Annotators are specifically instructed to discard offensive and harmful data during the review of the Coscript. 
Despite these precautions, there may still be some prejudicial data that goes unnoticed in our final dataset. 
However, the likelihood of harmful content has been minimized through the manual correction of the validation and test sets by the annotators. 


### Intended Use-Cases
Coscript is primarily designed to advance research and applications in natural language understanding and generation, with a particular focus on language planning in daily life scenarios. 
While the dataset is comprehensive, it remains crucial that its usage remains focused on non-critical and non-sensitive domains. Coscript is not intended for safety-critical applications or as a substitute for expert advice in sensitive areas such as medical, legal, and financial decision-making. 
By ensuring these boundaries are respected and by providing clear reminders of usage safety, Coscript aims to contribute positively to ongoing advancements in AI research and applications while minimizing potential risks and ethical concerns.
