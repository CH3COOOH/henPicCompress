import astd_tui
import batch_handle

if __name__ == '__main__':
	img_folder = astd_tui.ask_input_line('Folder')
	sav_folder = astd_tui.ask_input_line('Saveto')
	param = astd_tui.ask_input_line('Operation', 'Supported: -gray, -maxlen=, -sratio=, -q=')

	for save_path in batch_handle.exec(img_folder, sav_folder, param):
		print('-> ' + save_path)