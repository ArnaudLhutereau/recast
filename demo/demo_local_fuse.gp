set term postscript color eps enhanced 22
set output "demo_local_fuse.eps"
load "styles.inc"
set size 1,0.65
set bmargin 3
set tmargin 2
set lmargin 9
set rmargin 5
set title "Local Redis cluster, Fuse, RS (10,4)" offset 0,-0.5
set ylabel "Latency (sec)"
set xlabel "Requests"
set grid y
#set ytics 0,20,100
set yrange [0:0.6]
set xrange [0:]
set key top right samplen 1 width 1

plot \
 	'data/1024_data.txt'  u ($1):($3)\
 		 w l ls 5 notitle '1024',\
 	'data/1024_data.txt'  u ($1):($3)\
 		 w p ls 5 notitle '1024',\
   	'data/131072_data.txt'  u ($1):($3)\
   		 w l ls 7 notitle '131072',\
   	'data/131072_data.txt'  u ($1):($3)\
   		 w p ls 7 notitle '131072',\
	'data/4194304_data.txt'  u ($1):($3)\
		 w l ls 8 notitle '4194304',\
	'data/4194304_data.txt'  u ($1):($3)\
		 w p ls 8 notitle '4194304',\
   	10000\
 		w lp ls 5 title '1kB',\
   	10000\
 		w lp ls 7 title '256kB',\
   	10000\
 		w lp ls 8 title '4MB'
		
	

!epstopdf "demo_local_fuse.eps"
!rm "demo_local_fuse.eps"
quit