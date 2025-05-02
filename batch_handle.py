import os

import tool_kits
import afile

def exec(img_folder, sav_folder, param):
	img_filelist = afile.fileLstMaker(img_folder, filter_=['.jpg', '.png'])
	for fp in img_filelist:
		save_path = os.path.join(sav_folder, os.path.basename(fp))
		save_path_new = afile.filename_extend(save_path, '.hpc')
		img = tool_kits.load_img(fp)
		cprt = tool_kits.CprKit(img)
		cprt.arg_parse(param)
		cprt.save(save_path_new)
		yield save_path_new