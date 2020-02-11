# tweet-spam-detection

WARNING: Data not included!

Download https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit and place the `.gz` file into the root directory to get the needed embedding vector files.

### `generate_scores.py` will do the following:

If `gnews.embedding` is not present, the vector file will be used to generate one. This will take a few minutes.

If `classifier.joblib` is not present, the network will be trained with the CSV data, which is also not included in this project. You should not normally need to do this.

If `leaderboard.txt` is not present, a new spam leaderboard will be generated with dictionary data (not included.) This takes a LONG time. Do not remove this file. You will be sorry.

### `plot.py` will:
Generate a graph of the "spammiest" words using a snapshot of the leaderboard file. The graph is included at `img/spammiest.png`, so there is no need to rerun this.