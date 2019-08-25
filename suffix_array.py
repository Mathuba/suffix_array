# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  t_len = len(text)
  result = [0] * t_len

  suffixes = [ (i, text[i:]) for i in range(t_len)]
  suffixes.sort(key=lambda x: x[1])

  for i, _ in enumerate(suffixes):
    result[i] = suffixes[i][0]
    
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
