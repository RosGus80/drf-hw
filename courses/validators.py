import re

from rest_framework import serializers


class LessonValidator:
    def __init__(self, name):
        self.name = name

    def __call__(self, value1):
        pattern = re.compile('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
        tmp_name = dict(value1).get(self.name)

        if bool(pattern.match(tmp_name)):
            if bool(pattern.match(tmp_name)):
                if 'youtube.com' in tmp_name:
                    pass
            else:
                raise serializers.ValidationError('Only youtube videos are allowed')

