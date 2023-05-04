
import os
import json
import random
import heapq
import evaluate
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from nltk.stem import WordNetLemmatizer

random.seed(123)
rouge = evaluate.load('rouge')
bertscore = evaluate.load("bertscore")


def blue(address):
    print(address)
    json_data = []
    with open(address, 'r', encoding="utf-8") as f:
        for jsonstr in f.readlines():
            jsonstr = json.loads(jsonstr)
            json_data.append(jsonstr)
    p = []
    r = []
    reference = []
    candidate = []
    for data in json_data:
        p.append(data["Generated Events"])
        r.append(data["Golden Events"])

    print("bertscore")
    l = len(r)
    scores = []
    for i in range(l):
        score = bertscore.compute(predictions=[p[i]], references=[r[i]], model_type="distilbert-base-uncased")['f1'][0]
        scores.append(score)
    print(round(sum(scores) / l, 4))

    print("blue")
    l = len(r)
    score = []
    for i in range(l):
        score.append(sentence_bleu([r[i].split()], p[i].split(), weights=(1, 0, 0, 0)))
    print(round(sum(score) / l, 4))

    print("rougeL")
    results = rouge.compute(predictions=p, references=r, use_aggregator=True)
    print(results)


wnl = WordNetLemmatizer()

blue('YOUR_RESULT')
