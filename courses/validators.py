import re

from rest_framework import serializers


class LessonValidator:
    def __init__(self, name):
        self.name = name

    def __call__(self, value1):
        pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
        tmp_name = dict(value1).get(self.name)
        result = re.findall(pattern, tmp_name)

        if len(result) > 0:
            for match in result:
                if 'youtube.com' in match:
                    pass
                else:
                    raise serializers.ValidationError(f'{self.name} must be YouTube link')

