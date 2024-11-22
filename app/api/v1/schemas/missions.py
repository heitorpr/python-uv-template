from app.domain.models.hero_association import HeroBase, MissionBase


class MissionSchema(MissionBase):
    heroes: list[HeroBase]
