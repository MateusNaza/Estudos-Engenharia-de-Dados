# %%
# Transforme o algarismo de Romano para Inteiro

class Solution(object):
    def romanToInt(self, s):
      dict = {
        'I': 1,'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000
      }

      pair_sub = [
        ('I', 'V'),
        ('I', 'X'),
        ('X', 'L'),
        ('X', 'C'),
        ('C', 'D'),
        ('C', 'M')]

      if len(s) > 1:
        total = dict[s[0]]

        for i in range(1, len(s)):

            if (s[i - 1], s[i]) in pair_sub:
                total += dict[s[i]] - 2 * dict[s[i - 1]]
            else:
                total += dict[s[i]]

        return total
      return dict[s]
  
# Teste para a função
Solution().romanToInt('XXII')