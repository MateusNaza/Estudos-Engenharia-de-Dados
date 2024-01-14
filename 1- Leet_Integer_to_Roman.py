# %%
# Transforme o algarismo de Inteiro para Romano

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''

        # Dicionários para mapear os valores e símbolos romanos
        romanDict = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
            'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
            }

        # Iterar sobre os valores e símbolos
        for letter, number in romanDict.items():
            while num >= number:
                result += letter
                num -= number

        return result

# Teste para a função, coloque o valor que deseja entre os ()
Solution().intToRoman(1997)