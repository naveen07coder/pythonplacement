# class Solution:
#     def shiftingLetters(self, ss, shift):
#
#         s = ss            #"abc"
#         shifts = shift            #[3,5,9]
#         res = ""
#         x = s
#         for i in range(len(s)):
#             s[i] = s[i-1]+shifts[i]
#             res = s[i]
#         return res
#
#
# ss= "abc"
# shift = [3,5,9]
# s = Solution()
# print(s.shiftingLetters(ss, shift))