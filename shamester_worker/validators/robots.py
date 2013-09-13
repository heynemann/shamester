#!/usr/bin/env python
# -*- coding: utf-8 -*-

from validators.base import ValidatorBase

class RobotsValidator(ValidatorBase):
    def validate(self):
        response = self._get("%s/robots.txt" % self.website)

        if not response:
            self._add_violations("Robots not found")
            return

        if not response.content:
            self._add_violations("Empty robots")
            return

        if "User-agent:" not in response.content:
            self._add_violations("Robots without 'User-agent:'")