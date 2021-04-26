# python3
from gooey import *
import os
import sys
# import arguments
@Gooey(required_cols=2, program_name='split multi-fasta to single-fasta', header_bg_color= '#DCDCDC', terminal_font_color= '#DCDCDC', terminal_panel_color= '#DCDCDC')
def main(): 
    ap = GooeyParser(description="Split multi fasta file into individual files using sequence ids as their file names")
    ap.add_argument("-m", "--multifasta", widget='FileChooser', help="Input multi fasta file")
    ap.add_argument("-out", "--outputdir", widget='DirChooser', help="directory of output fasta files")
    args = vars(ap.parse_args())
    # reading user inut file
    in_file = args['multifasta']
    file_path = args['outputdir']
    try:
        with open(in_file, "r") as fa:
            lines=fa.read().split('>')
            lines = lines[1:]
            lines=['>'+ seq for seq in lines]
            for name in lines:
                # extracting sequence Id to use it for file name
                file_name=name.split('\n')[0][1:]  
                out_file=open(file_path+"/"+file_name+".fasta", "w")
                out_file.write(name)
                out_file.close()
        print ("\nSucessfully splited "+os.path.basename(in_file)+" into single fasta files")
    except:
        sys.exit("Opps..either file is not present or file format is not correct")

if __name__ == '__main__':
    main()

