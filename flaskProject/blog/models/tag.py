from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import relationship

from blog.models.article_tag import article_tag_association_table
from blog.models.database import db


class Tag(db.Model):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    articles = relationship('Article', secondary=article_tag_association_table, back_populates='tags')

    def __str__(self):
        return self.name