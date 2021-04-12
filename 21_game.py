# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:47:38 2020

@author: anmol
"""

from random import choices



# situations = [[[],[10,10,10]] for i in range (19)]
# situations.append([[],[10,10]])
# situations.append([[],[10]])

# a = choices([1,2,3],[1,1,1],k= 20)

situations = {}
for i in range(19) :
    situations.update({ i : {'all numbers' : [] , 'result' : [] , 'choices' : [i+1,i+2,i+3] , 'weights' : [20,20,20]  }})
situations.update({ 19 : {'all numbers' : [] , 'result' : [] , 'choices' : [20,21] , 'weights' : [20,20]  }})
situations.update({ 20 : {'all numbers' : [] , 'result' : [] , 'choices' : [21] , 'weights' : [20]  }})


###### Game #####

for j in range (1000):
    current_number = 0
    turn = 1
    
    print ('current number is ' + str(current_number) )
    
    moves = {'player 1' : {'situation' : [], 'choice' : []} , 'player 2' : {'situation' : [], 'choice' : []}, 'result' : []}
    while current_number < 21 :   
        while True :
            if current_number == 19 :            
                a = choices(situations[current_number]['choices'],situations[current_number]['weights'])[0]
                if (a == current_number + 1) or (a == current_number + 2)  :
                    break
            elif current_number == 20 :
                a = choices(situations[current_number]['choices'],situations[current_number]['weights'])[0]
                if (a == current_number + 1)  :
                    break
            else :
                a = choices(situations[current_number]['choices'],situations[current_number]['weights'])[0]
                if (a == current_number + 1) or (a == current_number + 2) or (a == current_number + 3) :
                    break
                
            
        if turn % 2 == 1 :
            print ('Player 1 chose ' + str(a) )
            moves['player 1']['choice'].append(a)
            moves['player 1']['situation'].append(current_number)            
            situations[current_number]['all numbers'].append(a)
        else :
            print ('Player 2 chose ' + str(a) )
            moves['player 2']['choice'].append(a)
            moves['player 2']['situation'].append(current_number)
            situations[current_number]['all numbers'].append(a)        
        current_number = a
        turn += 1
    
    if turn % 2 == 0 :
        print ('Player 1 won!')
        moves['result'].append(0)
    else :
        print ('Player 2 won!')
        moves['result'].append(1) 
        
    ### Neural Network
        
    # Updating the lists    
        
    if moves['result'] == [0] :
        for i in range (len(moves['player 1']['situation'])) :        
            n = moves['player 1']['situation'][i] #0
            m = moves['player 1']['choice'][i] #3
            situations[n]['result'].append(1)
        for i in range (len(moves['player 2']['situation'])) :        
            n = moves['player 2']['situation'][i] #0
            m = moves['player 2']['choice'][i] #3
            situations[n]['result'].append(0)
    else :
        for i in range (len(moves['player 1']['situation'])) :        
            n = moves['player 1']['situation'][i] #0
            m = moves['player 1']['choice'][i] #3
            situations[n]['result'].append(0)
        for i in range (len(moves['player 2']['situation'])) :        
            n = moves['player 2']['situation'][i] #0
            m = moves['player 2']['choice'][i] #3
            situations[n]['result'].append(1)
    del n,m
    
    # Using the lists to shift weights
            
    for q in moves['player 1']['situation'] :
        if situations[q]['result'][-1] == 0 :            
            l = situations[q]['all numbers'][-1] # chosen number
            m = situations[q]['choices'].index(l) #index in weights
            situations[q]['weights'][m] -= 1
            del l,m
            
        elif situations[q]['result'][-1] == 1 :       
            l = situations[q]['all numbers'][-1] # chosen number
            m = situations[q]['choices'].index(l) #index in weights
            situations[q]['weights'][m] += 1
            del l,m
    for r in moves['player 2']['situation'] :
        if situations[r]['result'][-1] == 0 :            
            l = situations[r]['all numbers'][-1] # chosen number
            m = situations[r]['choices'].index(l) #index in weights
            situations[r]['weights'][m] -= 1
            del l,m
        elif situations[r]['result'][-1] == 1 :
            l = situations[r]['all numbers'][-1] # chosen number
            m = situations[r]['choices'].index(l) #index in weights
            situations[r]['weights'][m] += 1
            del l,m        
            
            


        
    