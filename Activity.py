names = ["Aarav","Priya","Dev","Meera","Kabir"]
scores = [90,75,88,62,95]
n= len(scores)
for i in range(n):
    print(i+1, names[i],":", scores[i])
print()


steps=1
print("scores at index 0 :",scores[0],"steps are",steps)
print()


target = 'Aarav'
steps=0
for i in names:
    steps+= 1
    if i == target :
        break
print("Search for",target,"steps taken",steps)


target ='Kabir'
steps= 0
for i in names:
    steps+= 1
    if i == target:
        break
print("Search for",target,"Steps taken =",steps)
print()

steps=0
target_sum=150
for i in range(n):
    for j in range(i+1,n):
        steps+=1
        if scores [i] + scores [j] ==target_sum:
            print(names[i],"+",names[j],"=",scores[i],+scores[j])
print("Total comparisons are",steps)

# ── PART 5: Asymptotic Summary ────────────────────────────────────────────────
# Asymptotic analysis: only the dominant (fastest-growing) term matters.
# Example: 3n^2 + 5n + 9 -> O(n^2). Smaller terms become irrelevant at large n.
print("=== Asymptotic Summary ===")
print("Theta(1) : index access - always 1 step, tight bound")
print("Omega(1) : best case - found in 1 step, lower bound")
print("O(n) : worst case - found after n =", n, "steps, upper bound")
print("O(n^2) : pair check - n*(n-1)/2 =", n * (n - 1) // 2, "comparisons")
print()
print("Drop constants. Keep the dominant term. That is asymptotic analysis!")