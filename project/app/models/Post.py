"""Post Model."""

from masoniteorm.models import Model


class Post(Model):
    """Post Model."""
    __fillable__ = ['post', 'user_id']