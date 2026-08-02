n=5
print("MY RUNNING LAP TRACKER")
print("number of laps,",n)
print()

#.  FORMULA METHOD

formula_total = n*(n+1) //2
print("Solution 1 : Formula method")
print("Total Running points : ", formula_total)

# Loop WAY

loop_total = 0
stepsloop= 0
for lap in range (1,n+1):
    loop_total= loop_total+lap
    stepsloop= stepsloop + 1
    print("Solution 2 : Loop Way")
    print("Total Running points :", stepsloop)


# NESTED LOOP METHOD

nested_total = 0
nested_steps =0 
for lap in range(1, n+1):
    for point in range(1,lap+1):
        nested_total=nested_total+1
        nested_steps=nested_steps+1
print("Solution 3 : Nested Loop Method")
print("Total Running Points :",nested_steps)
