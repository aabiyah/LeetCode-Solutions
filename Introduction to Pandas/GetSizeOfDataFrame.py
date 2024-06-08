import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = pd.DataFrame(players, columns=['player_id', 'name', 'age', 'position', 'team'])
    size = list(df.shape)
    return size