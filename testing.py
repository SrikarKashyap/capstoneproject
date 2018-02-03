data = 'Wavpath: telugu_70.wav<b hidden="hidden"><audio autoplay="autoplay" src="telugu_70.wav" controls="controls"></audio><b>'
import re

print(re.search('[a-z]+_\d+.wav',data).match)