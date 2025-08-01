# -*- coding: utf-8 -*-
"""A library to make psychrometric charts and overlay information in them."""
import matplotlib.pyplot as plt

from chart import PsychroChart


def main():
    """CLI entry point to show the default psychrometric chart."""
    PsychroChart().plot(ax=plt.gca())


if __name__ == "__main__":
    main()
    plt.show()