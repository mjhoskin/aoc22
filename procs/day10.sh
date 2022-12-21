sed -- 's/noop/noop,/g' ../data/d10.txt | tr " " "," | nl -w2 -s','| nl -w2 -s',' -v 0 > ../out_data/d10_3.txt     
