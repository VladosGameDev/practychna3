letters_with_star = {      #i mean '*'
"a":        #A
'''
 *** 
*   *
*   *
*****
*   *
*   *
*   *
'''
,
"b":        #B
'''
****
*   *
*   *
****
*   *
*   *
****
'''
,
"c":        #C
'''
 ***
*   *
*
*
*
*   *
 ***
'''
,
"d":        #D
'''
****         
*   *   
*   *
*   *     
*   *     
*   * 
****
'''
,
"e":        #E
'''
*****
*
*
***
*
*
*****
'''
,
"f":        #F
'''
*****
*
*
***
*
*
*
'''
,
"g":        #G
'''
 ***
*   *
*
*  **
*   *
*   *
 ***
'''
,
"h":        #H
'''
*   *           
*   *    
*   *   
*****       
*   *        
*   *    
*   *
'''
,
"i":        #I
'''
***
 * 
 * 
 * 
 * 
 * 
***
'''
,
"j":        #J
'''
 ***
  * 
  * 
  * 
  * 
  * 
**  
'''
,
"k":        #K
'''
*   *
*  * 
* *  
**   
* *  
*  * 
*   *
'''
,
"l":        #L
'''
*
*
*
*
*
*
*****
'''
,
"m":        #M
'''
*   *
*   *
** **
* * *
*   *
*   *
*   *
'''
,
"n":        #N
'''
*   *
*   *
**  *
* * *
*  **
*   *
*   *
'''
,
"o":        #O
'''
 *** 
*   *
*   *
*   *
*   *
*   *
 *** 
'''
,
"p":        #P
'''
****
*   *
*   *
****
*
*
*
'''
,
"q":        #Q
'''
 *** 
*   *
*   *
*   *
*   *
*  * 
 ** *
'''
,
"r":        #R
'''
**** 
*   *
*   *
**** 
* *  
*  * 
*   *
'''
,
"s":        #S
'''
 ****
*    
*    
 *** 
    *
    *
 *** 
'''
,
't':        #T
'''
*****
  *  
  *  
  *  
  *  
  *  
  *  
'''
,
"u":        #U
'''
*   *
*   *
*   *
*   *
*   *
*   *
 ***
'''
,
"v":        #V
'''
*   *
*   *
*   *
*   *
*   *
 * * 
  *  
'''
,
"w":        #W
'''
*   *
*   *
*   *
* * *
** **
*   *
*   *
'''
,
"x":        #X
'''
*   *
*   *
 * * 
  *  
 * * 
*   *
*   *
'''
,
"y":        #Y
'''
*   *
*   *
 * *
  *
  *
  *
  *

'''
,
"z":        #Z
'''
*****
    *
   *
  *
 *
*
*****
'''
}

#This for '#' letters
letters_with_cage = {
"a":        #A
'''
 ### 
#   #
#   #
#####
#   #
#   #
#   #
'''
,
"b":        #B
'''
####
#   #
#   #
####
#   #
#   #
####
'''
,
"c":        #C
'''
 ###
#   #
#
#
#
#   #
 ###
'''
,
"d":        #D
'''
####         
#   #   
#   #
#   #     
#   #     
#   # 
####
'''
,
"e":        #E
'''
#####
#
#
###
#
#
#####
'''
,
"f":        #F
'''
#####
#
#
###
#
#
#
'''
,
"g":        #G
'''
 ###
#   #
#
#  ##
#   #
#   #
 ###
'''
,
"h":        #H
'''
#   #           
#   #    
#   #   
#####       
#   #        
#   #    
#   #
'''
,
"i":        #I
'''
###
 # 
 # 
 # 
 # 
 # 
###
'''
,
"j":        #J
'''
 ###
  # 
  # 
  # 
  # 
  # 
##  
'''
,
"k":        #K
'''
#   #
#  #
# #  
##   
# #  
#  # 
#   #
'''
,
"l":        #L
'''
#
#
#
#
#
#
#####
'''
,
"m":        #M
'''
#   #
#   #
## ##
# # #
#   #
#   #
#   #
'''
,
"n":        #N
'''
#   #
#   #
##  #
# # #
#  ##
#   #
#   #
'''
,
"o":        #O
'''
 ### 
#   #
#   #
#   #
#   #
#   #
 ### 
'''
,
"p":        #P
'''
####
#   #
#   #
####
#
#
#
'''
,
"q":        #Q
'''
 ### 
#   #
#   #
#   #
#   #
#  # 
 ## #
'''
,
"r":        #R
'''
#### 
#   #
#   #
#### 
# # 
#  # 
#   #
'''
,
"s":        #S
'''
 ####
#    
#    
 ### 
    #
    #
 ### 
'''
,
't':        #T
'''
#####
  #  
  #  
  #  
  #  
  #  
  #
'''
,
"u":     #U
'''
#   #
#   #
#   #
#   #
#   #
#   #
 ###
'''
,
"v":        #V
'''
#   #
#   #
#   #
#   #
#   #
 # # 
  #  
'''
,
"w":        #W
'''
#   #
#   #
#   #
# # #
## ##
#   #
#   #
'''
,
"x":        #X
'''
#   #
#   #
 # # 
  #  
 # # 
#   #
#   #
'''
,
"y":        #Y
'''
#   #
#   #
 # #
  #
  #
  #
  #
'''
,
"z":        #Z
'''
#####
    #
   #
  #
 #
#
#####
'''
}

while True:
    not_letters_count = 0   #this variable for not English letter in word

    word = input('Enter English word(or "123" if you want exit): ').lower()        #We ask user for input word that be print

    if word == '123': break    #break 'while' operation if user input '123'
        
    while True: #Check if user input not number
        
        symbol = input('You want print this word(s) with "*"(enter any even number) or "#"(enter any odd number)? ')    #Ask for symbol

        try:    #Try choose from which symbols the letters will be composed
            if int(symbol) % 2 == 0:       #This for *
                a = letters_with_star
                break   #Finish the "while" operation

            elif int(symbol) % 2 > 0:      #This for #
                a = letters_with_cage
                break   #Finish the "while" operation

        except Exception:   #if any error -->
            print('You enter wrong data, try again:')
            continue

    for letter in word:     #Go through the letters in the word -->
         if letter == ' ' or not letter.isalpha():   #Check the word for whitespaces/numbers/symbols and if they are, don't print them
             not_letters_count += 1   #count not English letter
             continue
         if letter == 'a': print(a['a'])
         if letter == 'b': print(a['b'])
         if letter == 'c': print(a['c'])
         if letter == 'd': print(a['d'])
         if letter == 'e': print(a['e'])
         if letter == 'f': print(a['f'])
         if letter == 'g': print(a['g'])
         if letter == 'h': print(a['h'])
         if letter == 'i': print(a['i'])
         if letter == 'j': print(a['j'])
         if letter == 'k': print(a['k'])
         if letter == 'l': print(a['l'])
         if letter == 'm': print(a['m'])
         if letter == 'n': print(a['n'])
         if letter == 'o': print(a['o'])
         if letter == 'p': print(a['p'])
         if letter == 'q': print(a['q'])
         if letter == 'r': print(a['r'])
         if letter == 's': print(a['s'])
         if letter == 't': print(a['t'])
         if letter == 'u': print(a['u'])
         if letter == 'v': print(a['v'])
         if letter == 'w': print(a['w'])
         if letter == 'x': print(a['x'])
         if letter == 'y': print(a['y'])
         if letter == 'z': print(a['z'])  #Print letter

    print('\nSymbols/whitespaces or not English letter in your word:', not_letters_count)
