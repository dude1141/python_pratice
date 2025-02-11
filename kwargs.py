def func(**Kwargs):
	for i,val in Kwargs.items():
		print("....",(i,val))

func(s1='Geeks',s2='For')

       key    value
.... ('s1', 'Geeks')
.... ('s2', 'For')

# arguments are stored as  key-value pair




def funcs(*args,**Kwargs):
    print(args)  #tuple
    print(Kwargs) #dictionary

    
funcs(2,3,4,s1='zzzz',s2='xxxx')
(2, 3, 4)
{'s1': 'zzzz', 's2': 'xxxx'}
