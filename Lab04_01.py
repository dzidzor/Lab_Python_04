#1a
groceries=['banana','strawberries','apples','bread']
item=raw_input("enter item to add to list:")
groceries.append(item)
print groceries
print '_________________________________________________________________________________________________'
#1b
item_1=raw_input("enter item to remove from list:")
groceries.remove(item_1)
print groceries
print '_________________________________________________________________________________________________'
#1c
aisles={'apples':'a','bananas':'b','bread':'b','strawberries':'s'}
item_2=raw_input("enter item name:")
print item_2+" " +"are"+" " +"in" +" "+aisles[item_2]
print '_________________________________________________________________________________________________'
#2a
#Dictionaries

#2b
item_prices={'apples':'SPIC_APPLES','bananas':'SPIC_BANANAS',\
             'bread':'SPIC_BREAD','carrots':'SPIC-CARROTS',\
             'champagne':'SPIC_CHAMPAGNE','strawberries':'SPIC_STRWABERRIES'}
item_3=raw_input("enter an item and get the price displayed")
print item_3+" "+"cost"+" "+item_prices[item_3]
print '_________________________________________________________________________________________________'

#2c
item_4=raw_input("enter name of item :")
price=raw_input("enter new price:")
item_prices[item_4]= price
print "the new price is"+item_prices['item_4']
print '_________________________________________________________________________________________________'

#2d
item_5=raw_input("enter name of item to add to list:")
price_1=raw_input("enter price of item:")
item_prices[item_5]=price_1
print item_prices[item_5]+" "+"costs"+""+ price_1
print '_________________________________________________________________________________________________'
#3a
#the use of tuples

#3b
always_in_stock=('apples','bananas','bread','carrot','champagne','strawberries')

#3c
list_a+list_b


#4a
#dictionaries

#4b
def binary_insert (new_price,price_list):
    price_list.append(new_price)
    price_list.sort()
    return

#4c
def min_cost(groceries, item_price_dict):
    item_price_dict
    
    
#5a
adjacency_dict={'A':['B','C'],'B':['A','D','E'],'C':['A','F','E']\
                    ,'D':['B'].'E':['B'],'F':['C']}
