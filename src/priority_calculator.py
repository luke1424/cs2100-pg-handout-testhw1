class HousingPriorityCalculator:
    def points_for_class_year(self, year: int) -> int:
        return year

    def points_for_graduation(self, is_graduating: bool) -> int:
        return 5 if is_graduating else 0

    def points_for_credits(self, num_credits: int) -> int:
        return min(num_credits, 50)

    def points_for_additional_questions(self, responses: dict[str, bool]) -> int:
        score = 0
        if responses.get("old23", False):
            score += 2
        if responses.get("honors", False):
            score += 3
        return score

    def calculate_total_score(
        self,
        year: int,
        is_graduating: bool,
        num_credits: int,
        additional_responses: dict[str, bool],
    ) -> int:
        return (
            self.points_for_class_year(year)
            + self.points_for_graduation(is_graduating)
            + self.points_for_credits(num_credits)
            + self.points_for_additional_questions(additional_responses)
        )
