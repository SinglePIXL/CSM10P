# We get three test scores.
# if avg. is more than 95, then
# we display congratulations.

HIGH_SCORE = 95
# We prompt user to get 3 test scores
test1 = int( input( 'Enter the first test score: ' ) )
test2 = int( input( 'Enter the second test score: ' ) )
test3 = int( input( 'Enter the third test score: ' ) )

# We calculate average test score

avg = (test1 + test2 + test3) / 3
print( ' The average score is ', avg)

if avg >= HIGH_SCORE:
    print( 'Congratulations' )

else:
    print( 'Try harder next time' )