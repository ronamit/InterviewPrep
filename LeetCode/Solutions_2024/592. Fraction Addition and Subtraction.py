from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        # split the string to operands
        operands = []
        if expression[0].isdigit():
            expression = "+" + expression

        last_sign = expression[0]
        last_num = ""

        for char in expression[1:]:
            if char in {"+", "-"}:
                operands.append(last_sign + last_num)
                last_num = ""
                last_sign = char
            else:
                last_num += char
        operands.append(last_sign + last_num)
        print(operands)
        numerators = []
        denom_list = []
        signs = []
        for operand in operands:
            sign_str = operand[0]
            num_str = operand[1:]
            numerator_str, denom_str = num_str.split("/")
            numerators.append(int(numerator_str))
            denom_list.append(int(denom_str))
            signs.append(1 if sign_str == "+" else -1)

        common_denom = 1
        for i_ in range(len(denom_list)):
            common_denom *= denom_list[i_]

        result_numerator = 0
        n_operands = len(operands)
        for i in range(n_operands):
            mult = common_denom // denom_list[i]
            result_numerator += mult * numerators[i] * signs[i]

        comm_div = gcd(result_numerator, common_denom)
        common_denom = common_denom // comm_div
        result_numerator = result_numerator // comm_div
        result_sign_str = "" if result_numerator >= 0 else "-"
        result_str = result_sign_str + str(abs(result_numerator)) + "/" + str(common_denom)
        return result_str


if __name__ == "__main__":
    s = Solution()
    print(s.fractionAddition("-1/2+1/2+1/3"))
