# Setting up

```bash
python3 -m venv .venv
pip install -r requirements.txt
```

# Porównanie fine-tuningu pretrenowanych modeli:

Najlepszy osiągnięty wynik na zbiorze testowym podczas treningu

| Długość sekwencji | DistilBERT                | Mamba                      | Czas na epokę DistilBERT (s) | Czas na epokę Mamba (s) |
| :---------------- | :------------------------ | :------------------------- | :--------------------------- | :---------------------- |
| 128               | ~87.6% Accuracy, 87.6% F1 | ~89.5% Accuracy, ~89.5% F1 | 70                           | 164                     |
| 256               | ~91% Accuracy, 91% F1     | ~92.7% Accuracy, ~92.7% F1 | 150                          | 255                     |
| 512               | ~93.1% Accuracy, 93.1% F1 | ~94.5% Accuracy, ~94.5% F1 | 311                          | 445                     |
| 1024              | ~88.0% Accuracy, 88.0% F1 | ~94.8% Accuracy, ~94.8% F1 | 588                          | 715                     |

Czas treningu dla DistilBert zależy prawie liniowo od długości sekwencji.  
Mamba trenuje się dłużej, ale skaluje się lepiej czasowo i ogólnie ma lepsze wyniki.  
Model Mamba jest około 2x większy niż DistilBERT (130M vs. 66M parametrów).  
Dla modelu Mamba zwiększenie długości sekwencji z 512 na 1024 przynosi niewielkie korzyści, dla modelu DistilBERT pogarsza wyniki (Mamba ma lepszą skalowalność).
