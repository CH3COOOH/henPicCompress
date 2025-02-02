import sys
import astd_tui
import batch_handle

if __name__ == '__main__':
	if len(sys.argv) == 1:
		img_folder = astd_tui.ask_input_line('Folder')
		sav_folder = astd_tui.ask_input_line('Saveto')
		param = astd_tui.ask_input_line('Operation', 'Supported: -gray, -maxlen=, -sratio, -q=')
	else:
		img_folder = sys.argv[1]
		sav_folder = sys.argv[2]
		param = ' '.join(sys.argv[3:])
		print(f"Param: {param}")

	for save_path in batch_handle.exec(img_folder, sav_folder, param):
		print('-> ' + save_path)