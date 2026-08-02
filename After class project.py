quiz_scores = [90,85,43,55,68,72,88,89]
print("MY QUI RESULT SEARCHER")
print("Quiz scores = ", quiz_scores)

# O(1)  DIRECT ACESS // CONSTANT

first_scores=quiz_scores[0]
print("PART 1 : Direct acess")
print("First student score = ",first_scores)

# O(n).   LINEAR SEARCH 

target_score = 88
steps = 0
found = False
print(" PART 2 LINEAR SEARCH")
print("Searching for score ", target_score)
for score in quiz_scores:
    steps +=1
    if score == target_score:
        print("Score found", score)
        print("Steps taken", steps)
        break
    if found == False:
        print("Score not found")
        print("Steps taken ", steps)

    # O(n)2.  PAIR COMPARISION

    print("PART 3 PAIR COMPARISION")
    pair_steps= 0
    for score1 in quiz_scores:
        for score2 in quiz_scores:
            pair_steps = pair_steps +1
    print("Total Pair checks", pair_steps)


    # BEST AND WORST CASE

    print(" PART 4 CASE COMPARISIONS")
    best_case_score=90
    average_case_score = 55
    worst_case_score = 89

    print("best case target ",best_case_score, " Found near the begining")
    print("average case target ",average_case_score ," Found in the middle of the data")
    print("worst case target ",worst_case_score, " Found near the end")