#!/usr/bin/env python
# -*- coding: utf-8 -*-

from validators.base import ValidatorBase

class HTMLSizeValidator(ValidatorBase):
    def validate(self):
        response = self._get(self.website)

        if response:
            if "content-length" in response.headers:
                content_length = int(response.headers["content-length"])/1000
            
                if content_length > self.config.get("MAX_PAGE_SIZE"):
                    self._add_violations("Content-length greater then %d. Got %d" % 
                        (self.config.get("MAX_PAGE_SIZE"), content_length))

            if response.content:
                page_size = len(response.content)/1000
                
                if page_size > self.config.get("MAX_PAGE_SIZE"):
                    self._add_violations("Page size greater then %d. Got %d" % 
                            (self.config.get("MAX_PAGE_SIZE"), page_size))