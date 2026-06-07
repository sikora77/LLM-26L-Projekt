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

| Model          | Długość sekwencji | Epoch 1 (s) | Epoch 2 (s) | Epoch 3 (s) |  Avg / Epoch  |
| :------------- | :---------------: | :---------: | :---------: | :---------: | :-----------: |
| **DistilBERT** |        128        |   337.18    |   335.92    |   363.30    | **~345.47s**  |
| **DistilBERT** |        256        |   637.55    |   640.63    |   635.54    | **~637.91s**  |
| **DistilBERT** |        512        |   1365.68   |   1368.60   |   1456.24   | **~1396.84s** |
| **DistilBERT** |       1024        |   2373.48   |   2381.67   |   2341.30   | **~2363.21s** |
| **Mamba**      |        128        |   511.95    |   511.88    |   517.99    | **~513.94s**  |
| **Mamba**      |        256        |   838.00    |   837.64    |   836.92    | **~837.52s**  |
| **Mamba**      |        512        |   1623.09   |   1636.30   |   1633.26   | **~1630.88s** |
| **Mamba**      |       1024        |   2525.73   |   2537.53   |   2535.23   | **~2532.83s** |
