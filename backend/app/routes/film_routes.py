from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Film
from app import db

film_bp = Blueprint('film', __name__, url_prefix='/film')

@film_bp.route('/', methods=['POST'])
def get_all_film():
    films = Film.query.all()
    return jsonify({
        'id': film.id,
        'title': film.title,
        'year': film.year,
        'genre': film.genre
    } for film in films)

@film_bp.route('/<int:film_id>', methods=['GET'])
def get_film_details(film_id):
    film = Film.query.get_or_404(film_id)
    reviews = [{
        'id': r.id,
        'rating': r.rating,
        'comment': r.comment,
        'user_id': r.user_id,
        'date': r.date.isoformat()
    } for r in film.review_set]
    return jsonify({
        'id': film.id,
        'title': film.title,
        'year': film.year,
        'genre': film.genre,
        'reviews': reviews
    })

@film_bp.route('/', methods=['POST'])
@jwt_required
def add_film():
    data = request.get_json()
    film = Film(
        title=data.get['title'],
        year=data.get['year'],
        genre=data.get['genre'],
    )
    db.session.add(film)
    db.session.commit()
    return jsonify({ 'msg': 'Film added successfully', 'id': film.id }), 201
