import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

# Se crea un arbol a partir del XML
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)  # Saco el text
print('Attr:', tree.find('email').get('hide'))  # Saco un attribute del tag. En este caso 'hide'
print('Phone:', tree.find('phone').text.strip())
print('Phone type:', tree.find('phone').get("type"))
