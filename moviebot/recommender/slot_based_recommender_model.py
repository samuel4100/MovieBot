"""Recommender model based on slot value pairs."""

from typing import Any, Dict, List

from moviebot.database.db_movies import DataBase
from moviebot.dialogue_manager.dialogue_state import DialogueState
from moviebot.domain.movie_domain import MovieDomain
from dialoguekitrec.recommender.recommendation_engine import (
    RecommendationEngine,
)


class SlotBasedRecommenderModel(
    RecommendationEngine
):  # RecommendationRetriever):
    def __init__(self, db: DataBase, domain: MovieDomain) -> None:
        """Instantiates a slot-based recommender model.

        Args:
            db: Database with available items.
            domain: Domain knowledge.
        """
        super().__init__()
        self.item_db = db
        self._domain = domain

    def retrieve_items(
        self, dialogue_state: DialogueState
    ) -> List[Dict[str, Any]]:
        """Recommends movies based on slot-value pairs.

        Args:
            dialogue_state: Dialogue state.

        Returns:
            Recommended movies.
        """
        self.stored_items = self.item_db.database_lookup(
            dialogue_state, self._domain
        )
        return self.stored_items
