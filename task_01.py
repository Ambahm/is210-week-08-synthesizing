#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to create The Cartesian sets
   X×Y between two sets X and Y is the set
   of all possible ordered pairs with first
   element from X and second element from Y
   Total number of elements = n^2.
"""

def get_matches(players):
    """ This fnction creates Cartesian product for a list.

    Args:
        players (List): list of players in a game.

    Return:
        tuple: Tubles for cartesian product

    Example:
       >>>get_matches(['Harry', 'Howard', 'Hugh'])
       [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """

    player_list = []                                # empty list to fill in
    for x_axis, x_play in enumerate(players):       # x coordinate
        for y_axis, y_play in enumerate(players):   # y coordnate
            if x_axis < y_axis:                     # Deselect 1st member
                create_tuple = (x_play, y_play)
                player_list.append(create_tuple)


    return sorted(player_list)


if __name__ == '__main__':
    print get_matches(['Harry', 'Howard', 'Hugh'])




