from pypulation import PopulationSimulator
import numpy as np

import matplotlib.pyplot as plt

def replace_nans(arr: np.ndarray, val=0):
    arr[np.isnan(arr)] = val
    return arr


def from_world_bank(
    year: int,
    regions: list[str] = [],
    path="/home/lionel/pypulations/data/Population-EstimatesData.csv",
) -> PopulationSimulator:

    import pandas as pd

    df = pd.read_csv(path)

    sim = PopulationSimulator(
        regions=df["Country Name"].unique(), time_step=1, max_age=100
    )

    for i in range(26):
        # Iterate over the ages for young people every year
        fe_this_year = df.loc[
            df["Indicator Code"] == f"SP.POP.AG{i:02}.FE.IN", str(year)
        ]


        sim.m[:, i, 0] = replace_nans(fe_this_year)
        sim.m[:, i, 1] = replace_nans(df.loc[
            df["Indicator Code"] == f"SP.POP.AG{i:02}.MA.IN", str(year)
        ])

    return sim


if __name__ == "__main__":
    for year in range(1980, 2022):
        fig, ax = plt.subplots()
        # Simple example, each couple will lead to two children
        sim = from_world_bank(year)
        # Start with two babies

        sim.plot(ax)
        fig.savefig(f"data/plots/pyramid_{year}.png")
