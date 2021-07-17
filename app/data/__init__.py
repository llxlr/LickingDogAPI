#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkg_resources import resource_filename as rf


def fake_useragent():
    return rf(__name__, 'fake-useragent.json')


def github_trending():
    return rf(__name__, 'gh-trending.json')


def hitokoto_():
    return rf(__name__, 'hitokoto.json')


def hubble():
    return rf(__name__, 'hubble-birthdays-full-year.csv')


def mnist_images():
    return rf(__name__, 'mnist_images.png')


def mnist_labels_uint8():
    return rf(__name__, 'mnist_labels_uint8')


def tiangou():
    return rf(__name__, 'tiangou.json')


def test():
    return rf(__name__, 'test.json')


if __name__ == '__main__':
    pass
