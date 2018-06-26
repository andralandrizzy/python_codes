# OPEN A FILE
fo = open('textTutorial.txt', 'w')

# GET SOME INFO
print('Name: ', fo.name)

# CHECK IF THE FILES IS CLOSE OR NOT.
print('Is Closed: ', fo.closed)

# OPENING MODE
print('Opening Mode: ', fo.mode)

# WRITE ON THE FILE
fo.write('''\nIgnorant saw her her drawings marriage laughter. 
Case oh an that or away sigh do here upon. Acuteness you exquisite ourselves now end forfeited.
Enquire ye without it garrets up himself. Interest our nor received followed was.
Cultivated an up solicitude mr unpleasant.''')
fo.close()


# READ FROM FILE
fo = open('textTutorial.txt', 'r+')
text = fo.read()
print(text)
fo.close()
