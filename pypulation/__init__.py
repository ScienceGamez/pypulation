from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np

from pypulation.intialization import InitializationType

if TYPE_CHECKING:
    import matplotlib


class PopulationSimulator:
    """A population simulator.

    :arg m: The matrix of the population.
        shape = (n_regions, n_ages, n_genders)
    """

    m: np.ndarray

    def __init__(
        self,
        regions: list[str] = ["single region"],
        time_step: int = 365,
        max_age: int = 120 * 365,
        n_genders: int = 2,
        initialization: InitializationType = InitializationType.Stationary,
    ) -> None:
        """Create a simulator.

        :arg regions: The regions that are simulated.
        :arg time_step: The
        """
        self.m = np.zeros((len(regions), max_age // time_step, n_genders))
        self.n_genders = n_genders
        self.regions = regions
        self.n_ages = self.m.shape[1]

    def step(self, births: np.ndarray, mortality: np.ndarray[float]):
        """Update the age of the population.

        births: The births. shape = (n_regions, n_genders)
        mortality: The death rate (between 0 and 1),
            shape = (n_regions, n_ages, n_genders)
        """

        m = self.m - self.m * mortality

        self.m = np.roll(m, 1, axis=1)
        self.m[:, 0, :] = births

    def plot(
        self, ax: matplotlib.axes.Axes | None = None, region: str | None = None
    ):
        """Plot as a pyramid of ages."""
        import matplotlib.pyplot as plt

        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = None
        if region is None:
            pop_array = np.sum(self.m, axis=0)
        else:
            pop_array = self.m[self.regions.index(region), :, :]

        if self.n_genders == 2:

            women_pop = pop_array[:, 0]
            men_pop = pop_array[:, 1]

            x = np.arange(self.m.shape[1])

            ax.barh(x, women_pop, height=1, color="r")
            ax.barh(x, -men_pop, height=1, color="b")

        if fig:
            plt.show()


if __name__ == "__main__":
    # Simple example, each couple will lead to two children
    sim = PopulationSimulator()
    # Start with two babies
    sim.step([[1, 1]],  np.zeros_like(sim.m))
    for i in range(120):
        sim.step(np.sum(sim.m, axis=1), np.zeros_like(sim.m))
    sim.plot()
