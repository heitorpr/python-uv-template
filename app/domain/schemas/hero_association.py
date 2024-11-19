from app.domain.models.hero_association import HeroBase, Team


class HeroSchema(HeroBase):
    id: int | None = None
    team: Team | None = None
