import pandas as pd


files = {
    'max.csv': 1.3,
    'raph.csv': 1,
    'adil.csv': 1,
}

subs = {file: pd.read_csv(file) for file in files}

print(pd.DataFrame({file: sub['target'] for file, sub in subs.items()}).corr())

blend = subs[list(subs.keys())[0]].copy()
blend['target'] = 0
for file, sub in subs.items():
    blend['target'] *= (files[file] * sub['target'])
blend['target'] **= 1 / sum(files.values())

blend.to_csv('blend.csv', index=False)
