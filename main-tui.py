import os

import tool_kits
import astd_tui
import afile
import batch_handle

if __name__ == '__main__':
	img_folder = astd_tui.ask_input_line('Folder')
	sav_folder = astd_tui.ask_input_line('Saveto')
	param = astd_tui.ask_input_line('Operation', 'Supported: -gray, -maxlen=, -sratio, -q=')

	# img_filelist = afile.fileLstMaker(img_folder, filter_=['.jpg', '.png'])
	# for fp in img_filelist:
	# 	save_path = os.path.join(sav_folder, os.path.basename(fp))
	# 	img = tool_kits.load_img(fp)
	# 	cprt = tool_kits.CprKit(img)
	# 	cprt.arg_parse(param)
	# 	cprt.save(save_path)
	# 	print('-> ' + save_path)
	for save_path in batch_handle.exec(img_folder, sav_folder, param):
		print('-> ' + save_path)

