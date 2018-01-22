
"""
This will read xml using minidom and get the value of node by its name
xml_text = <root>
	<node>
		<name id="key">Hello</name>
	</node>
</root>
OR
above contents in /dir_of_file/file_name
"""
import xml.dom.minidom as minidom
import os

loader_config = minidom.parse(os.path.join(dir_of_file,file_name))
# to load xml string
# loader_config = mindom.parseString(xml_text)
node = loader_config.getElementsByTagName("node")
elem = node.getElementsByTagName("name")
print(elem[0].firstChild.data) # fetches node value - Hello
node = loader_config.getElementsByTagName("name")
print(elem.attributes['id'].value) # fetches node attribute - key
