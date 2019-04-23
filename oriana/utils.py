# -*- coding: utf-8 -*-
# utils.py
# author : Antoine Passemiers

import numpy as np
import scipy.special


def logit(x):
    return np.log(x / (1. - x))


def sigmoid(x):
    return 1. / (1. + np.exp(-x))


def digamma(x):
    return scipy.special.digamma(x)


def digamma_prime(x):
    return scipy.special.polygamma(1, x)


def inverse_digamma(y):
    """Vectorized implementation of the inverse digamma
    method proposed by T. Minka.

    Reference:
        Estimating a Dirichlet distribution
        Thomas P. Minka
        2000; revised 2003, 2009, 2012
    """
    x = np.where(y >= 2.22, np.exp(y) + .5, -1. / (y + digamma(1)))
    for i in range(3):
        x -= ((digamma(x) - y) / digamma_prime(x))
    return x