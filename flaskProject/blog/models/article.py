from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import relationship

from blog.models.article_tag import article_tag_association_table
from blog.models.database import db



class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    title = Column(String(255), nullable=False, default='', server_default='')
    text = Column(Text, nullable=False, default='', server_default='')
    
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=func.now())

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_association_table, back_populates='articles')

    def __str__(self):
        return self.title