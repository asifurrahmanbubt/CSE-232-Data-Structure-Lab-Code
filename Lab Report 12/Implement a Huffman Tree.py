class HuffmanNode:
def __init__(self, char, freq):
self.char = char
self.freq = freq
self.left = None
self.right = None
def build_huffman_tree(data):
frequency = {}
for char in data:
if char in frequency:
frequency[char] += 1
else:
frequency[char] = 1
nodes = [HuffmanNode(char, freq) for char, freq in frequency.items()]
while len(nodes) > 1:
nodes = sorted(nodes, key=lambda x: x.freq)
left = nodes.pop(0)
right = nodes.pop(0)
internal_node = HuffmanNode('$', left.freq + right.freq)
internal_node.left = left
internal_node.right = right
nodes.append(internal_node)
return nodes[0]
def generate_huffman_codes(node, code, codes):
if node is not None:
if node.char != '$':
codes[node.char] = code
print(f"{node.char}: {code}")
generate_huffman_codes(node.left, code + '0', codes)
generate_huffman_codes(node.right, code + '1', codes)
def huffman_codes(data):
root = build_huffman_tree(data)
codes = {}
generate_huffman_codes(root, '', codes)
if __name__ == "__main__":
input_data = "abracadabra"
print("Huffman Codes:")
huffman_codes(input_data)
