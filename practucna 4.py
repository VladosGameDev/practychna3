def a():
    print('''
 *** 
*   *
*   *
*****
*   *
*   *
*   *
''')

def b():
    print('''
****
*   *
*   *
****
*   *
*   *
****
''')

def c():
    print('''
 ***
*   *
*
*
*
*   *
 ***
''')

def d():
    print('''
****         
*   *   
*   *
*   *     
*   *     
*   * 
****
''')

def e():
    print('''
*****
*
*
***
*
*
*****
''')

def f():
    print('''
*****
*
*
***
*
*
*
''')

def g():
    print('''
 ***
*   *
*
*  **
*   *
*   *
 ***
''')

def h():
    print('''
*   *           
*   *    
*   *   
*****       
*   *        
*   *    
*   *
''')

def i():
    print('''
***
 * 
 * 
 * 
 * 
 * 
***
''')

def j():
    print('''
***
  * 
  * 
  * 
  * 
  * 
**  
''')

def k():        
    print('''
*   *
*  * 
* *  
**   
* *  
*  * 
*   *
''')

def l():
    print('''
*
*
*
*
*
*
*****
''')

def m():
    print('''
*   *
*   *
** **
* * *
*   *
*   *
*   *
''')

def n():
    print('''
*   *
*   *
**  *
* * *
*  **
*   *
*   *
''')

def o():
    print('''
 *** 
*   *
*   *
*   *
*   *
*   *
 *** 
''')

def p():
    print('''
****
*   *
*   *
****
*
*
*
''')

def q(): 
    print('''
 *** 
*   *
*   *
*   *
*   *
*  * 
 ** *
''')

def r(): 
    print('''
**** 
*   *
*   *
**** 
* *  
*  * 
*   *
''')

def s(): 
    print('''
 ****
*    
*    
 *** 
    *
    *
 *** 
''')

def t():
    print('''
*****
  *  
  *  
  *  
  *  
  *  
  *  
''')

def u():
    print('''
*   *
*   *
*   *
*   *
*   *
*   *
 ***
''')

def v(): 
    print('''
*   *
*   *
*   *
*   *
*   *
 * * 
  *  
''')

def w(): 
    print('''
*   *
*   *
*   *
* * *
** **
*   *
*   *
''')

def x(): 
    print('''
*   *
*   *
 * * 
  *  
 * * 
*   *
*   *
''')

def y():
    print('''
*   *
*   *
 * *
  *
  *
  *
  *
''')

def z():
    print('''
*****
    *
   *
  *
 *
*
*****
''')




def a2():
    print('''
 ### 
#   #
#   #
#####
#   #
#   #
#   #
''')

def b2():
    print('''
####
#   #
#   #
####
#   #
#   #
####
''')

def c2():
    print('''
 ###
#   #
#
#
#
#   #
 ###
''')

def d2():
    print('''
####         
#   #   
#   #
#   #     
#   #     
#   # 
####
''')

def e2():
    print('''
#####
#
#
###
#
#
#####
''')

def f2():
    print('''
#####
#
#
###
#
#
#
''')

def g2():
    print('''
 ###
#   #
#
#  ##
#   #
#   #
 ###
''')

def h2():
    print('''
#   #          
#   #    
#   #   
#####       
#   #        
#   #    
#   #
''')

def i2():
    print('''
###
 # 
 # 
 # 
 # 
 # 
###
''')

def j2():
    print('''
###
  # 
  # 
  # 
  # 
  # 
##  
''')

def k2():        
    print('''
#   #
#  # 
# #  
##   
# #  
#  # 
#   #
''')

def l2():
    print('''
#
#
#
#
#
#
#####
''')

def m2():
    print('''
#   #
#   #
## ##
# # #
#   #
#   #
#   #
''')

def n2():
    print('''
#   #
#   #
##  #
# # #
#  ##
#   #
#   #
''')

def o2():
    print('''
 ### 
#   #
#   #
#   #
#   #
#   #
 ### 
''')

def p2():
    print('''
####
#   #
#   #
####
#
#
#
''')

def q2(): 
    print('''
 ### 
#   #
#   #
#   #
#   #
#  # 
 ## #
''')

def r2(): 
    print('''
#### 
#   #
#   #
####
# #  
#  # 
#   #
''')

def s2(): 
    print('''
 ####
#    
#    
 ### 
    #
    #
 ### 
''')

def t2():
    print('''
#####
  #  
  #  
  #  
  #  
  #  
  *  
''')

def u2():
    print('''
#   #
#   #
#   #
#   #
#   #
#   #
 ###
''')

def v2(): 
    print('''
#   #
#   #
#   #
#   #
#   #
 # # 
  #  
''')

def w2(): 
    print('''
#   #
#   #
#   #
# # #
## ##
#   #
#   #
''')

def x2(): 
    print('''
#   #
#   #
 # # 
  #  
 # # 
#   #
#   #
''')

def y2():
    print('''
#   #
#   #
 # #
  #
  #
  #
  #
''')

def z2():
    print('''
#####
    #
   #
  #
 #
#
#####
''')

user_data = input('Enter data: ').lower()

while True:
    try:
        symbol = int(input('Enter number(even if want with "*", odd if want with "#"): '))
        break
    except Exception:
        print('enter number')
    
for letter in user_data:
    if symbol % 2 == 0:
        if letter == 'a': a()
        if letter == 'b': b()
        if letter == 'c': c()
        if letter == 'd': d()
        if letter == 'e': e()
        if letter == 'f': f()
        if letter == 'g': g()
        if letter == 'h': h()
        if letter == 'i': i()
        if letter == 'j': j()
        if letter == 'k': k()
        if letter == 'l': l()
        if letter == 'm': m()
        if letter == 'n': n()
        if letter == 'o': o()
        if letter == 'p': p()
        if letter == 'q': q()
        if letter == 'r': r()
        if letter == 's': s()
        if letter == 't': t()
        if letter == 'u': u()
        if letter == 'v': v()
        if letter == 'w': w()
        if letter == 'x': x()
        if letter == 'y': y()
        if letter == 'z': z()
    else:
        if letter == 'a': a2()
        if letter == 'b': b2()
        if letter == 'c': c2()
        if letter == 'd': d2()
        if letter == 'e': e2()
        if letter == 'f': f2()
        if letter == 'g': g2()
        if letter == 'h': h2()
        if letter == 'i': i2()
        if letter == 'j': j2()
        if letter == 'k': k2()
        if letter == 'l': l2()
        if letter == 'm': m2()
        if letter == 'n': n2()
        if letter == 'o': o2()
        if letter == 'p': p2()
        if letter == 'q': q2()
        if letter == 'r': r2()
        if letter == 's': s2()
        if letter == 't': t2()
        if letter == 'u': u2()
        if letter == 'v': v2()
        if letter == 'w': w2()
        if letter == 'x': x2()
        if letter == 'y': y2()
        if letter == 'z': z2()
