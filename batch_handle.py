import os

import tool_kits
import afile

def exec(img_folder, sav_folder, param):
	img_filelist = afile.fileLstMaker(img_folder, filter_=['.jpg', '.png'])
	for fp in img_filelist:
		save_path = os.path.join(sav_folder, os.path.basename(fp))
		img = tool_kits.load_img(fp)
		cprt = tool_kits.CprKit(img)
		cprt.arg_parse(param)
		cprt.save(save_path)
		yield save_path