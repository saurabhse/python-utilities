
"""
This will read xml using minidom and get the value of node by its name
<root>
	<node>
		<name>Hello</name>
	</node>
</root>
"""
import xml.dom.minidom as minidom
import os

loader_config = minidom.parse(os.path.join(dir_of_file,file_name))
node = loader_config.getElementsByTagName("node")
elem = node.getElementsByTagName("name")
print(elem[0].firstChild.data)
