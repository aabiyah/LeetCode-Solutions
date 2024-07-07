import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
   scores_sorted = scores.sort_values(by='score', ascending=False)

   # The method='dense' option ensures that duplicate scores receive the same rank, and the next distinct score gets the next consecutive rank.

   scores_sorted['rank'] = scores_sorted['score'].rank(method='dense', ascending=False).astype(int)
   return scores_sorted[['score', 'rank']]