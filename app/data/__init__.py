#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkg_resources import resource_filename


def fake_useragent():
    return resource_filename(__name__, "fake-useragent.json")


def github_trending():
    return resource_filename(__name__, "gh-trending.json")


def hitokoto_():
    return resource_filename(__name__, "hitokoto.json")


def hubble():
    return resource_filename(__name__, "hubble-birthdays-full-year.csv")


def mnist_images():
    return resource_filename(__name__, "mnist_images.png")


def mnist_labels_uint8():
    return resource_filename(__name__, "mnist_labels_uint8")


def tiangou():
    return resource_filename(__name__, "tiangou.json")


def test():
    return resource_filename(__name__, "test.json")
