from datetime import datetime
from typing import NewType

from attr import attrib, attrs


UserId = NewType("UserId", int)


@attrs
class User:
    primary_key = attrib(type=UserId)
    created = attrib(type=datetime)
    modified = attrib(type=datetime)
    name = attrib(type=str)
    about = attrib(type=str)
    avatar = attrib(type=str)


ChatId = NewType("ChatId", int)


@attrs
class Chat:
    primary_key = attrib(type=ChatId)
    name = attrib(type=str)
    is_hidden = attrib(type=bool)


MessageId = NewType("MessageId", int)


@attrs
class Message:
    primary_key = attrib(type=MessageId)
    user = attrib(type=User)
    text = attrib(type=str)

    def written_by(self, user):
        # type: (User) -> bool
        return self.user.primary_key == user.primary_key
