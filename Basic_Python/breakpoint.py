# def calculate(a,b):
#     result = a + b
#     breakpoint()
#     result = result * 2
#     return result

# print(calculate(10,10))
# s = "abaccdbbd"
# k = 3
# result = []

# i, j = 0, k
# while j <= len(s):
#     temp = s[i:j]
#     print(f"Printing temp : {temp}")
#     if temp[::-1] == temp:
#         result.append(temp)
#         print("The result - ", result)
#         j += 1
#     else:
#         j += 1
#         i += 1

# print(len(result))


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        result = []

        i, j = 0, k
        while j <= len(s):
            temp = s[i:j]
            if temp[::-1] == temp:
                result.append(temp)
                j += 1
            else:
                j += 1
                i += 1
        print(result)
        return len(result)