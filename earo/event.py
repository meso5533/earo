#!/usr/bin/python
# -*- coding:utf-8 -*-


class Event:
    built_in_fields = ['event']

    def __init__(self, event_name, **kwarg):
        self.event_name = event_name
        self.params = {}
        self.__set_built_in_params()
        for k, v in kwarg.items():
            self.set_param(k, v)

    def __set_built_in_params(self):
        self.params['event'] = self

    def get_param(self, key, default=None):
        return self.params.get(key, default)

    def set_param(self, key, value):
        if key in self.built_in_fields:
            raise BuiltInEventParam(key)
        else:
            self.params[key] = value

    def contains_key(self, key):
        return key in self.params


class BuiltInEventParam(Exception):

    def __init__(self, field):
        self.field = field
        super(
            BuiltInEventParam,
            self).__init__(
                '[BuiltInEventParam] could not modify built in event param field : `%s`.' %
            field)
