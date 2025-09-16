class HousingQuestionAsker:
    def ask_class_year(self) -> int:
        while True:
            try:
                year = int(input("Enter your class year (1=Freshman, 2=Sophomore, 3=Junior, 4=Senior): "))
                if year in [1, 2, 3, 4]:
                    return year
            except ValueError:
                pass
            print("Invalid input. Please enter 1, 2, 3, or 4.")

    def ask_graduation_status(self) -> bool:
        while True:
            response = input("Are you graduating this semester? (y/n): ").strip().lower()
            if response in ["y", "n"]:
                return response == "y"
            print("Invalid input. Please enter 'y' or 'n'.")

    def ask_credits_earned(self) -> int:
        while True:
            try:
                credits = int(input("How many credits have you earned? "))
                if credits >= 0:
                    return credits
            except ValueError:
                pass
            print("Invalid input. Please enter a non-negative integer.")

    def ask_additional_questions(self) -> dict[str, bool]:
        responses = {}

        while True:
            ans = input("Are you older than 23? (y/n): ").strip().lower()
            if ans in ["y", "n"]:
                responses["old23"] = ans == "y"
                break
            print("Invalid input. Please enter 'y' or 'n'.")

        while True:
            ans = input("Are you in the honors program? (y/n): ").strip().lower()
            if ans in ["y", "n"]:
                responses["honors"] = ans == "y"
                break
            print("Invalid input. Please enter 'y' or 'n'.")

        return responses
