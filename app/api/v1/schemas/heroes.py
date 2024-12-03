from app.domain.models.hero_association import HeroBase, Mission, Team


class HeroSchema(HeroBase):
    id: int | None = None
    team: Team | None = None
    missions: list[Mission] | None = None
