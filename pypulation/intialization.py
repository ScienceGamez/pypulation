from enum import Enum, auto



class InitializationType(Enum):
    """Type of initialization.

    Following  https://en.wikipedia.org/wiki/Population_pyramid#Types

    "Stationary" pyramid or constant population pyramid
    A pyramid can be described as stationary if the percentages of population
    (age and sex) remain approximately constant over time.[7]
    In a stationary population, the numbers of births and death roughly
    balance one another.

    "Expansive" pyramid or Expanding population pyramid
    A population pyramid that is very wide at the younger ages, characteristic
    of countries with a high birth rate and perhaps low life expectancy.[6]
    The population is said to be fast-growing, and the size of each birth
    cohort increases each year.[8]

    "Constrictive" pyramid or Declining population
    A population pyramid that is narrowed at the bottom. The population is
    generally older on average, as the country has long life expectancy,
    a low death rate, but also a low birth rate.[6] This may suggest that in
    future there may be a high dependency ratio due to reducing numbers
    at working ages.
    This is a typical pattern for a very developed country,
    with a high level of education, easy access to and incentive
    to use birth control, good health care,
    and few negative environmental factors.[9]
    """

    Stationary = auto()
    Expansive = auto()
    Constrictive = auto()
