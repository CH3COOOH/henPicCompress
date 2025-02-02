# henPicCompress
For saving pictures with low-capacity disks.

## Usage

### GUI mode
Nothig to say, so easy.  
![](/img/hpc_gui.jpg)

### CLI mode
You can compress images with CLI prompt by run it directly:
```shell
hpc-tui
```

or use parameters:  
```shell
hpc-tui <src_dir> <des_dir> <params>
```

#### Parameters
| Key | Value | Description |
| --- | ----- |------------ |
| -q=  | 0 - 100 | Image quality |
| -sratio= | 0.0 - 1.0 | Resize ratio |
| -gray | - | If grayscale is needed, add this |

For example:  
```shell
hpc-tui /home/xxx/src /home/xxx/des -q=90 -sratio=0.5
# The images in /home/xxx/src will be 0.5x resized, and saved in /home/xxx/des with quality 90.
```