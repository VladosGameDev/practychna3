a = '''
 *** 
*   *
*   *
*****
*   *
*   *
*   *
'''

b = '''
****
*   *
*   *
****
*   *
*   *
****
'''

c = '''
 ***
*   *
*
*
*
*   *
 ***
'''

d = '''
****         
*   *   
*   *
*   *     
*   *     
*   * 
****
'''

e = '''
*****
*
*
***
*
*
*****
'''

f = '''
*****
*
*
***
*
*
*
'''

g = '''
 ***
*   *
*
*  **
*   *
*   *
 ***
'''

h = '''
*   *           
*   *    
*   *   
*****       
*   *        
*   *    
*   *
'''

i = '''
***
 * 
 * 
 * 
 * 
 * 
***
'''

j = '''
 ***
  * 
  * 
  * 
  * 
  * 
**  
'''

k = '''
*   *
*  * 
* *  
**   
* *  
*  * 
*   *
'''

l = '''
*
*
*
*
*
*
*****
'''

m = '''
*   *
*   *
** **
* * *
*   *
*   *
*   *
'''

n = '''
*   *
*   *
**  *
* * *
*  **
*   *
*   *
'''

o = '''
 *** 
*   *
*   *
*   *
*   *
*   *
 *** 
'''

p = '''
****
*   *
*   *
****
*
*
*
'''

q = '''
 *** 
*   *
*   *
*   *
*   *
*  * 
 ** *
'''

r = '''
**** 
*   *
*   *
**** 
* *  
*  * 
*   *
'''

s = '''
 ****
*    
*    
 *** 
    *
    *
 *** 
'''

t = '''
*****
  *  
  *  
  *  
  *  
  *  
  *  
'''

u = '''
*   *
*   *
*   *
*   *
*   *
*   *
 ***
'''

v = '''
*   *
*   *
*   *
*   *
*   *
 * * 
  *  
'''

w = '''
*   *
*   *
*   *
* * *
** **
*   *
*   *
'''

x = '''
*   *
*   *
 * * 
  *  
 * * 
*   *
*   *
'''

y = '''
*   *
*   *
 * *
  *
  *
  *
  *

'''

z = '''
*****
    *
   *
  *
 *
*
*****
'''


A = '''
 ### 
#   #
#   #
#####
#   #
#   #
#   #
'''

B = '''
####
#   #
#   #
####
#   #
#   #
####
'''

C = '''
 ###
#   #
#
#
#
#   #
 ###
'''

D = '''
####         
#   #   
#   #
#   #     
#   #     
#   # 
####
'''

E = '''
#####
#
#
###
#
#
#####
'''

F = '''
#####
#
#
###
#
#
#
'''

G = '''
 ###
#   #
#
#  ##
#   #
#   #
 ###
'''

H = '''
#   #           
#   #    
#   #   
#####       
#   #        
#   #    
#   #
'''

I = '''
###
 # 
 # 
 # 
 # 
 # 
###
'''

J = '''
 ###
  # 
  # 
  # 
  # 
  # 
##  
'''

K = '''
#   #
#  #
# #  
##   
# #  
#  # 
#   #
'''

L = '''
#
#
#
#
#
#
#####
'''

M = '''
#   #
#   #
## ##
# # #
#   #
#   #
#   #
'''

N = '''
#   #
#   #
##  #
# # #
#  ##
#   #
#   #
'''

O = '''
 ### 
#   #
#   #
#   #
#   #
#   #
 ### 
'''

P = '''
####
#   #
#   #
####
#
#
#
'''

Q = '''
 ### 
#   #
#   #
#   #
#   #
#  # 
 ## #
'''

R = '''
#### 
#   #
#   #
#### 
# # 
#  # 
#   #
'''

S = '''
 ####
#    
#    
 ### 
    #
    #
 ### 
'''

T = '''
#####
  #  
  #  
  #  
  #  
  #  
  #
'''

U = '''
#   #
#   #
#   #
#   #
#   #
#   #
 ###
'''

V = '''
#   #
#   #
#   #
#   #
#   #
 # # 
  #  
'''

W = '''
#   #
#   #
#   #
# # #
## ##
#   #
#   #
'''

X = '''
#   #
#   #
 # # 
  #  
 # # 
#   #
#   #
'''

Y = '''
#   #
#   #
 # #
  #
  #
  #
  #
'''

Z = '''
#####
    #
   #
  #
 #
#
#####
'''


while True:
    not_letters_count = 0   #this variable for not English letter in word

    word = input('Enter English word(or "123" if you want exit): ').lower()        #We ask user for input word that be print

    if word == '123': break    #break 'while' operation if user input '123'
        
    while True: #Check if user input not number
        
        symbol = int(input('You want print this word(s) with "*"(enter any even number) or "#"(enter any odd number)? '))   #Ask for symbol

        try:    #Try choose from which symbols the letters will be composed
            for letter in word:     #Go through the letters in the word -->
                if letter == ' ' or not letter.isalpha():   #Check the word for whitespaces/numbers/symbols and if they are, don't print them
                    not_letters_count += 1   #count not English letter
                    continue
                if symbol % 2 == 0:
                    if letter == 'a': print(a)
                    if letter == 'b': print(b)
                    if letter == 'c': print(c)
                    if letter == 'd': print(d)
                    if letter == 'e': print(e)
                    if letter == 'f': print(f)
                    if letter == 'g': print(g)
                    if letter == 'h': print(h)
                    if letter == 'i': print(i)
                    if letter == 'j': print(j)
                    if letter == 'k': print(k)
                    if letter == 'l': print(l)
                    if letter == 'm': print(m)
                    if letter == 'n': print(n)
                    if letter == 'o': print(o)
                    if letter == 'p': print(p)
                    if letter == 'q': print(q)
                    if letter == 'r': print(r)
                    if letter == 's': print(s)
                    if letter == 't': print(t)
                    if letter == 'u': print(u)
                    if letter == 'v': print(v)
                    if letter == 'w': print(w)
                    if letter == 'x': print(x)
                    if letter == 'y': print(y)
                    if letter == 'z': print(z)
                if symbol % 2 > 0:
                    if letter == 'a': print(A)
                    if letter == 'b': print(B)
                    if letter == 'c': print(C)
                    if letter == 'd': print(D)
                    if letter == 'e': print(E)
                    if letter == 'f': print(F)
                    if letter == 'g': print(G)
                    if letter == 'h': print(H)
                    if letter == 'i': print(I)
                    if letter == 'j': print(J)
                    if letter == 'k': print(K)
                    if letter == 'l': print(L)
                    if letter == 'm': print(M)
                    if letter == 'n': print(N)
                    if letter == 'o': print(O)
                    if letter == 'p': print(P)
                    if letter == 'q': print(Q)
                    if letter == 'r': print(R)
                    if letter == 's': print(S)
                    if letter == 't': print(T)
                    if letter == 'u': print(U)
                    if letter == 'v': print(V)
                    if letter == 'w': print(W)
                    if letter == 'x': print(X)
                    if letter == 'y': print(Y)
                    if letter == 'z': print(Z)
            break
        except Exception:   #if any error -->
            print('You enter wrong data, try again:')
            continue

      #Print letter

    print('\nSymbols/whitespaces or not English letter in your word:', not_letters_count)
