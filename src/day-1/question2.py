import re


NUMBER_WORDS = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4', 
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

def find_numeric_digits(s, left_max, right_max, left_num, right_num):
  l = 0
  r = len(s) - 1
  
  l_found = False
  r_found = False
  
  while l <= r and ((not l_found and l <= left_max) or (not r_found and r >= right_max)):
    if l <= left_max and not l_found:
      if s[l].isnumeric():
        left_num = s[l]
        l_found = True
      else:
        l += 1
    
    if r >= right_max and not r_found:
      if s[r].isnumeric() and not r_found:
        right_num = s[r]
        r_found = True
      else:
        r -= 1
  
  if not left_num or not right_num:
    return 0
  return left_num + right_num

def find_digits(s):
  regex = r'(?=(one|two|three|four|five|six|seven|eight|nine))'
  
  left_max = len(s) -1
  right_max = 0
  left_num = None
  right_num = None
  
  matches = re.finditer(regex, s, re.MULTILINE)
  for _, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
      groupNum = groupNum + 1
      
      if match.start(groupNum) < left_max:
        left_max = match.start(groupNum)
        left_num = NUMBER_WORDS[match.group(groupNum)]
        
      if match.end(groupNum) > right_max:
        right_max = match.end(groupNum)
        right_num = NUMBER_WORDS[match.group(groupNum)]

  return find_numeric_digits(s, left_max, right_max, left_num, right_num);
  

if __name__ == "__main__":
  with open("./src/day-1/input.txt", "r") as f:
    lines = f.read().split('\n')
  
  print(sum([int(find_digits(line)) for line in lines if line]))
  
  