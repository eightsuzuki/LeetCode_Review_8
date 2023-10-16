class AdditiveNumber:
    def is_additive_number(self, num: str) -> bool:
        """Function to judge whether the num is additive or not.

        Args:
            num(str): string

        Returns:
            bool: True if num is additive number, otherwise False
        """
        if len(num) < 2:
            return False

        for i in range(1, len(num)//2 + 1):
            for j in range(1, (len(num)-i)//2 + 1):
                if self.isValid(num[: i], num[i: i+j], num[i+j:]):
                    return True

        return False

    def is_valid(self, first: str, second: str, others: str) -> bool:
        """Function to judge whether the current combination is valid or not.

        Args:
            first(str): a part of num
            second(str): a part of num
            others(str): a part of num

        Returns:
            bool: True if num is additive number, otherwise False
        """
        if len(first) > 1 and first[0] == "0" or len(second) > 1 and second[0] == "0":
            return False

        sum_str = str(int(first) + int(second))
        if sum_str == others:
            return True

        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])

        return False
