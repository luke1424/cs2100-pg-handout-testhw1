from src.question_asker import HousingQuestionAsker
from src.priority_calculator import HousingPriorityCalculator

def calculate_score() -> int:
    asker = HousingQuestionAsker()
    student_info = asker.ask_basic_questions()

    if student_info.get("year") == "senior":  
        student_info["graduating"] = asker.ask_graduation_status()

    calculator = HousingPriorityCalculator(student_info)
    score = calculator.compute_score()
    return score

def main() -> None:
    print("========== Housing Priority Calculator ==========")
    total_score = calculate_score()
    print(f"Your final housing priority score is: {total_score}")
    print("=================================================")

if __name__ == "__main__":
    main()
