#!/usr/bin/python
# -*- coding: utf-8 -*-

DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

from datetime import datetime


class Website(object):
    def __init__(self, url, title=None, created_at=None, updated_at=None, last_processed_at=None):
        self.url = url

        self.title = title

        self.created_at = created_at
        if self.created_at is None:
            self.created_at = datetime.now()

        self.updated_at = updated_at
        if self.updated_at is None:
            self.updated_at = datetime.now()

        self.last_processed_at = last_processed_at

    @classmethod
    def to_timestamp(cls, date):
        if date is None:
            return None

        dt = date.strftime(DATE_FORMAT)
        return dt

    @classmethod
    def from_timestamp(cls, timestamp):
        if timestamp is None:
            return None

        return datetime.strptime(str(timestamp), DATE_FORMAT)

    def to_dict(self):
        return {
            'title': self.title or '',
            'url': self.url,
            'created_at': self.to_timestamp(self.created_at),
            'updated_at': self.to_timestamp(self.updated_at),
            'last_processed_at': self.to_timestamp(self.last_processed_at),
        }

    @classmethod
    def from_dict(cls, values):
        return cls(
            title=values['title'],
            url=values['url'],
            created_at=cls.from_timestamp(values['created_at']),
            updated_at=cls.from_timestamp(values['updated_at']),
            last_processed_at=cls.from_timestamp(values['last_processed_at']),
        )
