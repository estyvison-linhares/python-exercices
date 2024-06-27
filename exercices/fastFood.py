"""
Este exercício foi criado por mim mesmo. A ideia é ter um cardápio com várias categorias de itens.
Um cliente pode selecionar quantos itens do cardápio quiser desde que o restaurante possua a quantidade
de itens e o cliente tenha dinheiro suficiente para pagar todos os itens da lista. 
"""

"""
Melhorias em breve!
"""

from typing import List, Dict

customer1: Dict = {
  'Name': 'Jose',
  'money': 60,
  'shopItems': []
}

menu = [{
    'Category': 'Hamburguer',
    'Items': [{
      'name': 'burguer',
      'price': 25.99,
      'amount': 5
    }, {
      'name': 'x-egg',
      'price': 31.50,
      'amount': 1
    },
    {
      'name': 'x-bacon',
      'price': 49.90,
      'amount': 1
    }]
  }]

listItems: List[Dict] = [] 

def getItemMenu(categoty:str, item:str) -> Dict:
  menuItemsList: List[Dict] = getCategoryItems(categoty)
  
  if(menuItemsList != None):
    for menuItem in menuItemsList:
      menuItemName = menuItem.get('name')
      menuItemAmount = menuItem.get('amount')

      if  menuItemName == item and menuItemAmount == 0:
        print(f"Não temos mais {menuItemName}")
      elif menuItemName == item and menuItemAmount > 0:
        menuItemAmount -= 1
        menuItem.update({
          'amount': menuItemAmount
        })
        return menuItem
    
  return {}

def addItem(category:str, item:str):
  itemMenu = getItemMenu(category, item)
  listItems.append(itemMenu)

def getCategoryItems(category:str) -> List[Dict]:
  for itemMenu in menu:
    if itemMenu.get('Category') == category:
      return itemMenu.get('Items')

def payItemsInTheList(customer: Dict):
  if len(listItems) == 0:
    print('All items has been pay!')
  
  totalValue = calculateValueTotal(listItems)
  newMoneyValue = round(customer.get('money') - totalValue, 2)

  if(newMoneyValue < 0):
    print(f'{customer.get('Name')} não possui dinheiro suficiente para pagar!')
  else:
    print('Valor pago com sucesso!')
    listItems.clear()
    print(listItems)
    customer.update({
    'money': newMoneyValue
  })

def calculateValueTotal(listItems: List[Dict]) -> float:
  totalValue = 0.0

  for item in listItems:
    totalValue += item.get('price')
  
  return totalValue
    
addItem('Hamburguer', 'x-egg')
addItem('Hamburguer', 'burguer')
print(listItems)
payItemsInTheList(customer1)
print(customer1)

