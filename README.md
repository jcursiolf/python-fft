# Readme

This is a simple sample Python/Jupyter script for FFT, considering an input file `FormaOnda2.csv` with the following columns ("Tempo" means "time" in Portuguese):

| Tempo             | Axial              | Horizontal         | Vertical           |
|-------------------|--------------------|--------------------|--------------------|
| 0.000149821878484 | -0.112416830781069 | -0.982877734073746 | -0.381719785308371 |
| ...               | ...                | ...                | ...                |

The Python script saves the results as `result_python.csv`.

The Jupyter script saves the results as `result_jupyter.csv`, but also has a few charts so that you are able to visually verify the results.

## Notes: 
- Code is mostly commented in Portuguese, as this was created to help a Brazilian friend.
- "Tempo" means "time" in Portuguese.
- Tested with Python 3.8.10