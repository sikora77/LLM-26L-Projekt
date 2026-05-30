# Setting up

```bash
python3 -m venv .venv
pip install -r requirements.txt
```

# Porównanie modeli:

Najlepszy osiągnięty wynik na zbiorze testowym podczas treningu

|      | DistillBERT               | Mamba                      | Czas na epokę DistillBERT (s) | Czas na epokę Mamba (s) |
| :--- | :------------------------ | :------------------------- | :---------------------------- | :---------------------- |
| 128  | ~87.6% Accuracy, 87.6% F1 | ~89.5% Accuracy, ~89.5% F1 | 67                            |                         |
| 256  | ~91% Accuracy, 91% F1     | ~92.7% Accuracy, ~92.7% F1 | 136                           | 255                     |
| 512  | ~93.1% Accuracy, 93.1% F1 | ~94.5% Accuracy, ~94.5% F1 | 311                           | 445                     |
| 1024 | ~88.0% Accuracy, 88.0% F1 | ~92% Accuracy, ~92% F1     | 588                           |                         |

Czas treningu dla DistillBert zależy prawie liniowo od długości sekwencji
