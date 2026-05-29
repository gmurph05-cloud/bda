# Session 7 datasets

The following datasets are available for the pandas and data cleaning exercises:

- `Movies.json`
- `Pokemon.csv`

Load them from Python using paths such as:

```python
movies = pd.read_json("datasets/Movies.json")
pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")
```

`Pokemon.csv` uses an older text encoding, so load it with `encoding="cp1252"`.
