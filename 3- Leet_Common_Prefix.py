# Verifique a lista de strings em busca do maior prefixo em comum entre elas

from sys import prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
      if not strs:
          return ""

      # Ordenando a string em ordem alfabética
      strs.sort()

      # Pegando a primeira e a ultima string da lista
      first_str = strs[0]
      last_str = strs[-1]

      # Verificando caracteres em comum entre as strings
      common_prefix = ""
      for i in range(len(first_str)):
          if i < len(last_str) and first_str[i] == last_str[i]:
              common_prefix += first_str[i]
          else:
              break

      return common_prefix
  
# Teste para a função
lista_string = ["flower","flight","flow"]
Solution().romanToInt(lista_string)