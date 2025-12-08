var = "I completely agree with you"
text = var.split()

result = list(map(lambda x: len(x),text))
print(result)

