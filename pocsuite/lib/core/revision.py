#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from gitapi import Repo


def get_revision_number():
    root = os.path.dirname(os.path.abspath(__file__))

    while True:
        git = os.path.join(root, ".git")

        if os.path.exists(git):
            break
        else:
            root = os.path.dirname(root)

    repo = Repo(root)
    git_id = repo.git_id()

    return git_id and git_id[:7] or None
