def find_digits(s):
  return next((char for char in s if char.isdigit()), '0') + next((char for char in reversed(s) if char.isdigit()), '0')

if __name__ == "__main__":
  with open("./src/day-1/input.txt", "r") as f:
    lines = f.read().split('\n')
  
  print(sum([int(find_digits(line)) for line in lines if line]))
  