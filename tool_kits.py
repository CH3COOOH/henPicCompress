from PIL import Image

def load_img(fpath):
	return Image.open(fpath)

class CprKit:
	def __init__(self, img_obj):
		self.img = img_obj
		self.exif = img_obj.info.get('exif')
		self.save_quality = 80

	def arg_parse(self, parameters):
	## All supported args:
	## -gray -maxlen=xxx -q=80 -sratio=0.5
		if type(parameters) == str:
			parameters = parameters.split(' ')
		for p in parameters:
			if p == '-gray':
				self.toGrayscale()
			elif '-maxlen=' in p:
				_, max_len = p.split('=')
				self.resize(int(max_len))
			elif '-sratio=' in p:
				_, ratio = p.split('=')
				self.resize_ratio(float(ratio))
			elif '-q=' in p:
				_, quality = p.split('=')
				self.save_quality = int(quality)
			else:
				print('**Unknown argument \"%s\"' % p)

	def toGrayscale(self):
		self.img = self.img.convert('L')

	def resize(self, max_len_limit):
		self.img.thumbnail((max_len_limit, max_len_limit))

	def resize_ratio(self, ratio):
		max_edge = max(self.img.size)
		self.img.thumbnail((max_edge * ratio, max_edge * ratio))

	def save(self, fpath):
		self.img.save(fpath, quality=self.save_quality, exif=self.exif)