from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Review, Film
from app import db

review_bp = Blueprint('review', __name__)


@review_bp.route('/<int:film_id>/reviews', methods=['GET'])
def get_reviews(film_id):
    reviews = Review.query.filter_by(film_id=film_id).all()
    return jsonify([{
        'id': r.id,
        'rating': r.rating,
        'comment': r.comment,
        'user_id': r.user_id,
        'date': r.date.isoformat(),
    } for r in reviews])

@review_bp.route('/<int:film_id>/reviews', methods=['POST'])
@jwt_required()
def add_review(film_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    review = Review(
        rating=data.get['rating'],
        comment=data.get['comment'],
        film_id=film_id,
        user_id=user_id
    )
    db.session.add(review)
    db.session.commit()
    return jsonify({'msg': 'Critique ajoutée', 'id': review.id}), 201


@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
@jwt_required()
def delete_review_by_id(review_id):
    user_id = get_jwt_identity()
    review = Review.query.get_or_404(review_id)
    if review.user_id != user_id:
        return jsonify({'msg': 'Non autorisé'}), 403

    db.session.delete(review)
    db.session.commit()
    return jsonify({'msg': 'Critique supprimé'}), 204

