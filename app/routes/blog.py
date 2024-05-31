#!/usr/bin/env python3
from flask import Blueprint, render_template, request, jsonify, abort
from app.models import Category, Article
from app.database import Session

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/blog', methods=['GET', 'POST'])
def blog():
    """
    Route to render the blog page and handle AJAX requests
    for fetching articles
    based on category.
    """
    session = Session()

    if request.method == 'POST' and request.is_xhr:
        category_id = request.form.get('category_id')
        articles = []
        if category_id:
            articles = session.query(Article) \
                 .filter_by(category_id=category_id) \
                 .all()
        return render_template('articles.html', articles=articles)

    categories = session.query(Category).all()
    selected_category_id = request.args.get('category_id', type=int)
    selected_category = None
    articles = []

    if selected_category_id:
        try:
            selected_category = session.query(Category) \
                    .filter_by(id=selected_category_id) \
                    .one()

            articles = selected_category.articles
        except NoResultFound:
            abort(404)
    elif categories:
        selected_category = categories[0]
        articles = selected_category.articles

    session.close()

    return render_template(
        'blog.html',
        categories=categories,
        selected_category=selected_category,
        articles=articles
    )


@blog_bp.route('/blog/fetch_articles', methods=['POST'])
def fetch_articles():
    """
    Route to handle AJAX requests for fetching articles based on category ID.
    """
    session = Session()

    data = request.get_json()
    if not data or 'category_id' not in data:
        session.close()
        return jsonify(error='Category ID is missing'), 400

    category_id = data['category_id']
    category = session.query(Category).get(category_id)

    if category is None:
        session.close()
        abort(404)

    articles = [
        {
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'photo_url': article.photo_url
         }
        for article in category.articles
    ]

    session.close()

    return jsonify(articles=articles)


@blog_bp.route('/blog/article/<int:article_id>')
def article(article_id):
    """
    Route to render a specific article based on the article ID.
    """
    session = Session()

    article = session.query(Article).get(article_id)

    if article is None:
        session.close()
        abort(404)

    session.close()

    return render_template('article.html', article=article)
