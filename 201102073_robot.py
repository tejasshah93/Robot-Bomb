import curses
import random
#import menu
#import options
#import levels
#import display

class play:
#  def f1(self):
    curses.initscr()
    curses.start_color()
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
    curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)
    def main(self):
    	scr = curses.initscr()
	row,col = scr.getmaxyx()
    	curses.start_color()
    	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
    	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
    	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)
	curses.use_default_colors()
	self.go()

	curses.curs_set(0)
	#curses.cbreak()
	#robot = [7,7]

	wi = curses.newwin(row,col,0,0)          #y,x
	wi.box(124,45)
	wi.bkgd(' ',curses.color_pair(2))
	wi.refresh()
	win = wi.subwin(31,135,4,8)             #y,x
	win.border('|','|','-','-','J','O','H','N')
	win.addstr(0,50,'Select mode of play')
	win.bkgd(' ',curses.color_pair(1))
	win.refresh()
	choices = ["Quick Play","Custom Play","Help","Quit"]
	mode = 0
	inr = 3
	c = self.menu(wi,win,choices,mode,55,8,inr)
	#print c
	while c != 4:
		if c == 1:
			self.quick()
			ret = self.my(35,100,3,7,2)
			self.done(ret[0],ret[1])
		elif c == 2:
			a = self.cusplay()
			ret = self.my(a[0],a[1],a[2],a[3],a[4])
			self.done(ret[0],ret[1])
		elif c == 3:
			h = self.helpy()
			if h == 2:
				wi.clear()
				wi.refresh()
				break
		c = self.menu(wi,win,choices,mode,55,8,inr)
	
	if c == 4 or h == 2:
		curses.endwin()	

    def my(self,fb,fl,rs,cs,lev):
    	scr = curses.initscr()
	row,col = scr.getmaxyx()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	

#	curses.cbreak()
	bx = ((col - fl)/2)
	by = ((row - fb)/2)
	inv = curses.newwin(row,col,0,0)
	inv.box(32,32)
	inv.bkgd(curses.KEY_LEFT,curses.color_pair(1))
	inv.refresh()
	win = curses.newwin(fb,fl,by,bx)     #y,x
	win.keypad(1)
	win.nodelay(1)
	win.border('|','|','-','-','J','O','H','N')
#	win.bkgd(curses.KEY_RIGHT,curses.color_pair(2))
	win.refresh()
#	curses.doupdate()
	y = fb/2-2
	x = fl/2-4 
#	win.addstr(y2+0,x,'+++') 	  ^^        _O_      __		 _i_i_
#	win.addstr(y2+1,x,'+ +')	  !!   	    /|\	    /OO\	 [@ @]				
#	win.addstr(y2+2,x,'+++')	            / \	    |!!|	 /|-|\
#					  		    \--/	 ||_||
#					  		  		 _d_b_	

	x2 = [[x,y],[x+1,y],[x,y],[x,y+1],[x,y+1],[x+1,y+1],[x+1,y],[x+1,y+1]]
	
	x3 = [[x,y],[x+1,y],[x+2,y],[x,y],[x,y+1],[x,y+2],[x,y+2],[x+1,y+2],[x+2,y+2],[x+2,y],[x+2,y+1],[x+2,y+2],[x+1,y+1]]
	
	x4 = [[x,y],[x+1,y],[x+2,y],[x+3,y],  [x,y],[x,y+1],[x,y+2],[x,y+3],  [x,y+3],[x+1,y+3],[x+2,y+3],[x+3,y+3],  
	      [x+3,y],[x+3,y+1],[x+3,y+2],[x+3,y+3],  [x+1,y+1],[x+2,y+1],  [x+1,y+2],[x+2,y+2]]

	x5 = [[x,y],[x+1,y],[x+2,y],[x+3,y],[x+4,y],  [x,y],[x,y+1],[x,y+2],[x,y+3],[x,y+4],  [x,y+4],[x+1,y+4],[x+2,y+4],[x+3,y+4],[x+4,y+4],  
	      [x+4,y],[x+4,y+1],[x+4,y+2],[x+4,y+3],[x+4,y+4],  [x+1,y+1],[x+2,y+1],[x+3,y+1],  [x+1,y+2],[x+2,y+2],[x+3,y+2],
	      [x+1,y+3],[x+2,y+3],[x+3,y+3]]

	robot = []
	r = []
	p2 = ['^','^','^','!','!','!','^','!']
	
	p3 = [' ','O',' ',' ','/','/','/',' ','\\',' ','\\','\\','|']	
	
	p4 = [' ','_','_',' ',' ','/','|','\\','\\','-','-','/',' ','\\','|','/','O','O','!','!']

	p5 = [' ','i',' ','i',' ',' ','[','/','|',' ',' ','d',' ','b',' ',' ',']','\\','|',' ','@',' ','@','|','-','|','|','_','|'] 
	
	if rs == 2:
		robot = x2
		r = p2
	elif rs == 3:
		robot = x3
		r = p3
	elif rs == 4:
		robot = x4
		r = p4
	elif rs == 5:
		robot = x5
		r = p5

	for i in range(len(robot)):
		win.addstr(robot[i][1],robot[i][0],str(r[i]))
		win.refresh()
	
	il = int(fl/3)
	ib = int(fb/3)
	
	if lev == 1:
		win = self.lvl1(inv,win,fb,fl)
	
	elif lev == 2:
		prev1 = [il+1,3]     #x,y
		prev2 = [2*il+1,fb-4]     #x,y
		win = self.lvl2(inv,win,fb,fl)
		win.addstr(prev1[1],prev1[0],'/|\\',curses.color_pair(4))
		win.addstr(prev2[1],prev2[0],'\|/',curses.color_pair(4))

	elif lev == 3:
		prev2 = [fl/2-2,fb-4]     #x,y
		prev3 = [6,3]
		prev4 = [fl-9,3]
		prevx1 = [il/2,fb-4]
		win = self.lvl3(inv,win,fb,fl)
		win.addstr(prev2[1],prev2[0],'###',curses.color_pair(4))
		win.addstr(prev3[1],prev3[0],'###',curses.color_pair(4))
		win.addstr(prev4[1],prev4[0],'###',curses.color_pair(4))
	c=[]
	l = cs + 1
	z = [n for n in [[random.randrange(1,fl-1,1),random.randrange(1,fb-1,1)] for x in range(5*l)] if n not in robot]  #x,y
#	print z
	i = 0
	j = 0
	for i in range(5*l):
		if j == l: 
			break
		if win.inch(z[i][1],z[i][0]) & 255 == 32 and z[i] not in c:
			c.append(z[i])
			j = j + 1
	
#	print c

	win.addch(c[0][1],c[0][0],'B')#,curses.color_pair(3))
	t = 1
	while t != l:
		win.addch(c[t][1],c[t][0],"C")#,curses.color_pair(4))
		t = t + 1
	key = curses.KEY_RIGHT
	score = 0
	ctr = 0
	flag = s1 = s2 = s3 = s4 = sx1 = -1
#	win.addstr(prevx1[1],prevx1[0],'XXXXXXXX',curses.color_pair(4))
	
	while key != 27:                                                    # ESC = 27	
		if lev == 2:
			if ctr != 0:
				if prev1[1] == 3:			
					win.addstr(prev1[1],prev1[0],'/|\\',curses.color_pair(4))
					s1 = 1
			
			if ctr != 0:
				if prev2[1] == fb-4:    
					win.addstr(prev2[1],prev2[0],'|||',curses.color_pair(4))
					s2 = 1
				
		elif lev == 3:	
			if prev4[1] == fb/2:
				if prev2[1] == fb-4:    
					win.addstr(prev2[1],prev2[0],'###',curses.color_pair(4))
					s2 = 1
			if ctr != 0:
				if prev3[1] == 3 and prev3[0] == 6:
					win.addstr(prev3[1],prev3[0],'###',curses.color_pair(4))
					s3 = 1
		
			if prev3[1] == 2*ib-1:	
				if prev4[1] == 3 and prev4[0] == fl-9:
					win.addstr(prev4[1],prev4[0],'###',curses.color_pair(4))
					s4 = 1

#		if prev4[1] == fb/2:
#			if prevx1[1] == fb-4:    
#				win.addstr(prevx1[1],prevx1[0],'XXXXXXXX',curses.color_pair(4))
#				sx1 = 1
#		if ctr != 0:
#			if prevx1[1] == fb-4:
#				win.addstr(prevx1[1],prevx1[0],'XXXXXXXX',curses.color_pair(4))
#				sx1 = 1
		
		win.addstr(0,2,' Score: ' + str(ctr*10) + ' ')
		win.timeout(150 - ctr*8)
		pre = key
		getkey = win.getch()
		curses.noecho()
		if getkey == -1:
			key = key
		else:
			key = getkey
		if key == ord('p'): #or key == 112:
			key = -1
			while key != ord('p'): #or key != 112:
				try:
					key = win.getch()
					curses.noecho()
				except KeyboardInterrupt:
					curses.endwin()
					exit(1)				
			key = pre
		if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, 27]: 
			key = pre
		curses.doupdate()

		if s1 == 1:
		   win.addstr(prev1[1],prev1[0],'   ')
		if s2 == 1:
			win.addstr(prev2[1],prev2[0],'   ')
		if s3 == 1:
			win.addstr(prev3[1],prev3[0],'   ')
		if s4 == 1:
			win.addstr(prev4[1],prev4[0],'   ')
		if sx1 == 1:
			win.addstr(prevx1[1],prevx1[0],'        ') 

		if s1 == 1:
			res = self.nex(win,prev1,0,flag,fb,fl,3)
			prev1 = res[1]
			flag = res[0]
			win.addstr(prev1[1],prev1[0],'###',curses.color_pair(4))		
			if prev1[1] == fb-2:
				win.addstr(prev1[1],prev1[0],'   ')
			 	prev1[1] = 3
		
#		d = 0 verdown
#		d = 1 hor
#		d = 2 diag_right
#		d = 3 verup
#		d = 4 diag_left
		x = fl/fb
		y = (fl%fb)%5

		if s2 == 1:
			res = self.nex(win,prev2,3,flag,fb,fl,3)
			prev2 = res[1]
			flag = res[0]
			win.addstr(prev2[1],prev2[0],'###',curses.color_pair(4))
			if prev2[1] == 1:
				win.addstr(prev2[1],prev2[0],'   ')
			 	prev2[1] = fb-4

		if s3 == 1:
			res = self.nex(win,prev3,2,flag,fb,fl,3)
			prev3 = res[1]
			flag = res[0]
			win.addstr(prev3[1],prev3[0],'###',curses.color_pair(4))
			if prev3[1] == fb-3 and prev3[0] < fl-4: 
				win.addstr(prev3[1],prev3[0],'   ')
				prev3[0] = 6
				prev3[1] = 3
		
		if s4 == 1:
			res = self.nex(win,prev4,4,flag,fb,fl,3)
			prev4 = res[1]
			flag = res[0]
			win.addstr(prev4[1],prev4[0],'###',curses.color_pair(4))
			if prev4[1] == fb-3 and prev4[0] > x + 1: 
				win.addstr(prev4[1],prev4[0],'   ')
				prev4[0] = fl-9
				prev4[1] = 3
		
#		if sx1 == 1:
#			res = self.nex(win,prevx1,3,flag,fb,fl,3)
#			prevx1 = res[1]
#			flag = res[0]
#			win.addstr(prevx1[1],prevx1[0],'XXXXXXXX',curses.color_pair(4))
#			if prevx1[1] == 2:
#				win.addstr(prevx1[1],prevx1[0],'        ')
#			 	prevx1[1] = fb-4
	
#		if sx1 == 1:
#			res = self.nex(win,prevx1,3,flag,fb,fl,8)
#			prevx1 = res[1]
#			flag = res[0]
#			win.addstr(prevx1[1],prevx1[0],'XXXXXXXX',curses.color_pair(4))
#			if prevx1[1] == 2:
#				win.addstr(prevx1[1],prevx1[0],'        ')
#				prevx1[1] == fb-4
					

#	infront = [robot[0]+(key==curses.KEY_RIGHT and 1 or key==curses.KEY_LEFT and -1),robot[1]+(key==curses.KEY_DOWN and 1 or key==curses.KEY_UP and -1)]
		infront =[]
		for i in range(len(robot)):	   
			infront.append([robot[i][0]+(key==curses.KEY_RIGHT and 1 or key==curses.KEY_LEFT and -1),robot[i][1]+(key==curses.KEY_DOWN and 1 or key==curses.KEY_UP and -1)])		#x,y
	
	#	win.addch(robot[1],robot[0],' ')
	#	print infront	
		for i in range(len(robot)): 
#			if(rs == 3)
#				win.addstr(robot[i][1],robot[i][0],'   ')
#			if(rs == 5)
			win.addstr(robot[i][1],robot[i][0],' ')
		curses.doupdate()
	

		if key == curses.KEY_UP:
			s = 0
		elif key == curses.KEY_LEFT:
			s = 0 + rs
		elif key == curses.KEY_DOWN:
			s = 0 + 2*rs
		elif key == curses.KEY_RIGHT:
			s = 0 + 3*rs


		for i in range(rs):
			if win.inch(infront[s+i][1],infront[s+i][0]) & 255 == 32:
				pass
			elif win.inch(infront[s+i][1],infront[s+i][0]) & 255== ord('C'):
				ctr = ctr + 1
			elif win.inch(infront[s+i][1],infront[s+i][0]) & 255 == ord('B'):
				if ctr == cs:
					flag = 1
					break
				else:
					flag = 0
					break
			else:
			 	flag = 2
				break

		if flag != -1:
			curses.beep()
			curses.flash()
			break
	#	win.addch(infront[1],infront[0],'R')

	#	robot[0] = infront[0]
	#	robot[1] = infront[1]
	
		for i in range(len(robot)):
			robot[i][0] = infront[i][0]
			robot[i][1] = infront[i][1]

		for i in range(len(robot)):
			win.addstr(robot[i][1],robot[i][0],str(r[i]))

	win.clear()
	win.refresh()
#	curses.endwin()
	if flag == 1:
		pass
	else:
		pass
	ret = [flag,ctr]
	return ret


    def menu(self,wi,win,choices,mode,x,y,inr):
    	curses.initscr()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	

	win.bkgd(' ',curses.color_pair(1))	
	curses.curs_set(0)
	win.keypad(1)
#	win.nodelay(1)
#	curses.cbreak()
#	choices = ["Quick Play","Custom Play","Help","Quit"]
	n = len(choices)
	highlight = 1
	c = h = 0
	save = [x,y]
	self.pmenu(win,choices,highlight,n,save,inr,mode)
	while 1:
		key = win.getch()
		if mode == 0:
			if key == curses.KEY_UP:
				if highlight == 1:
					highlight = n
				else:
					highlight = highlight - 1

			elif key == curses.KEY_DOWN:
				if highlight == n:
					highlight = 1
				else:
					highlight = highlight + 1
		
			self.pmenu(win,choices,highlight,n,save,inr,mode)
			
			if key == 10:
				c = highlight
			
			if c != 0:
				break
		elif mode == 1:
			if key == curses.KEY_LEFT:
				if highlight == 1:
					highlight = n
				else:
					highlight = highlight - 1

			elif key == curses.KEY_RIGHT:
				if highlight == n:
					highlight = 1
				else:
					highlight = highlight + 1
		
			self.pmenu(win,choices,highlight,n,save,inr,mode)
			if key == 10:
				win.attroff(curses.A_REVERSE)
				h = highlight
			
			if h != 0:
				break

	win.refresh()	
	curses.delay_output(500)
#	print c
#	wi.clear()
#	wi.refresh()
#	win.refresh()
#	win.clear()
#	win.refresh()
	if mode == 0:
		wi.clear()
		wi.refresh()
		return c
	elif mode == 1:
#		wi.clear()
#		wi.refresh()
		return h

    def pmenu(self,win,choices,highlight,n,save,inr,mode):	
	x = save[0]
	y = save[1]
	for i in range(n):
		if highlight == i + 1:
#			win.attron(curses.A_REVERSE)
			win.addstr(y,x,choices[i],curses.A_REVERSE)
#			win.attroff(curses.A_REVERSE)
		else:
			win.addstr(y,x,choices[i],curses.A_BLINK)
		if mode == 0:
			y = y + inr
		elif mode == 1:
			x = x + inr
		i = i + 1
	
	win.refresh()


    class myex(Exception):
	def __init__(self):
		pass

#curses.initscr()
#curses.start_color()
 
#curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
#curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
#curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
#curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)

    def forex(self,win,flag):
    	curses.initscr()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	
	win.clrtoeol()
	win.refresh()
	flag = 0
	curses.curs_set(0)
	w = curses.newwin(5,35,15,55)            #y,x
	w.border('|','|','-','-','+','+','+','+')
	w.addstr(2,2,'Please enter a valid integer!')
	w.bkgd(' ',curses.color_pair(3))
	w.refresh()
	curses.napms(1500)
	w.clear()
	win.bkgd(' ',curses.color_pair(1))
	win.refresh()
	win.refresh()
	return flag

    def load(self,wi):
    	curses.initscr()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	
#	wine = wi.subwin(5,35,15,55)            #y,x
	wine = curses.newwin(5,35,15,55)            #y,x
	wine.border('|','|','-','-','+','+','+','+')
	wine.addstr(2,8,'Loading')
	wine.bkgd(' ',curses.color_pair(4))
	wine.refresh()
	curses.napms(400)
	wine.addstr(2,8,'Loading.')
	wine.bkgd(' ',curses.color_pair(4))
	wine.refresh()
	curses.napms(400)
	wine.addstr(2,8,'Loading..')
	wine.bkgd(' ',curses.color_pair(4))
	wine.refresh()
	curses.napms(400)
	wine.addstr(2,8,'Loading...')
	wine.bkgd(' ',curses.color_pair(4))
	wine.refresh()
	curses.napms(400)
	wine.addstr(2,8,'Loading....')
	wine.bkgd(' ',curses.color_pair(4))
	wine.refresh()
	curses.napms(1200)
	wine.clear()
	wine.refresh()

    def quick(self):
    	scr = curses.initscr()
	row,col = scr.getmaxyx()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	
	
	curses.curs_set(0)
	wi = curses.newwin(row,col,0,0)          #y,x
	wi.box(124,45)
	wi.bkgd(' ',curses.color_pair(1))
	wi.refresh()
	self.load(wi)
	wi.clear
	wi.refresh()
	curses.napms(100)

    def cusplay(self):
    	scr = curses.initscr()
	row,col = scr.getmaxyx()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	
	
	curses.curs_set(0)
	wi = curses.newwin(row,col,0,0)          #y,x
	wi.box(124,45)
	wi.bkgd(' ',curses.color_pair(2))
	wi.refresh()
	win = wi.subwin(31,135,4,8)            #y,x
	win.border('|','|','=','=','*','*','*','*')
	win.bkgd(' ',curses.color_pair(1))
	win.refresh()
	win.addstr(4,10,'Select Field Size: ')
	win.addstr(8,10,'Select grid size of your robot: ')
	win.addstr(12,10,'Enter no. of codes: ')
	win.addstr(13,10,'[Value: 0 < codes < 20]')
	win.addstr(16,10,'Select Level: ')
	curses.echo()
	win.refresh()
	flag = -1
	choices = ["Small","Moderate","Large"]
	mode = 1
	inr = 20
	c = self.menu(wi,win,choices,mode,42,4,inr)
	if c == 1:
		fl,fb = 70,25
	elif c == 2:
		fl,fb = 100,35
	elif c == 3:
		fl,fb = col,row
#	win.addstr(8,10,'Enter grid size of your robot: ')
	choices = ["2 X 2","3 X 3","4 X 4","5 X 5"]
	mode = 1
	inr = 20
	c = self.menu(wi,win,choices,mode,42,8,inr)
	if c == 1:
		rs = 2
	elif c == 2:
		rs = 3
	elif c == 3:
		rs = 4
	elif c == 4:
		rs = 5

#	win.addstr(10,10,'Enter no. of codes: ')
	curses.echo()
	win.refresh()
	flag = -1
	while 1:
		try:
			curses.curs_set(1)
			cs = int(win.getstr(12,30))
			if cs < 0 or cs > 20:
				raise myex
			flag = 1
			curses.curs_set(0)
		except:
			win.delch(16,30)
			flag = forex(win,flag)
		if flag != 0:
			break
	
	choices = ["1","2","3"]
	mode = 1
	inr = 20
	c = self.menu(wi,win,choices,mode,42,16,inr)
	if c == 1:
		lev = 1
	if c == 2:
		lev = 2
	elif c == 3:
		lev = 3
	
	ans = [fb,fl,rs,cs,lev]
	curses.endwin()		
	self.load(wi)
	win.clear()
	win.refresh()
	wi.clear()
	wi.refresh()
	return ans


    def helpy(self):
    	scr = curses.initscr()
	row,col = scr.getmaxyx()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	
	
	curses.curs_set(0)
	wi = curses.newwin(row,col,0,0)          #y,x
	wi.box(124,45)
	wi.refresh()
	win = wi.subwin(20,100,10,25)            #y,x
	win.border('|','|','=','=','*','*','*','*')
	win.refresh()
	win.addstr(4,12,'ROBOT BOMB DEFUSER (by Tejas Shah)')
	win.refresh()
	win.addstr(6,12,'Controls:  Left,Right,Up,Down - move')
	win.refresh()
	win.addstr(8,12,'p - Pause  ESC -quit while playing the game')
	win.addstr(10,12,'Note: In levels 2,3: The bullets will be activated')
	win.addstr(11,18,'when u start collecting decodes')
	win.addstr(13,12,'C - Decodes , B - Bomb')
	win.bkgd(' ',curses.color_pair(1))
	win.refresh()

	choices = ["Back","Quit"]
	mode = 1
	x = 12
	y = 16
	inr = 10
	h = self.menu(wi,win,choices,mode,x,y,inr)
	win.refresh()
	win.clear()
	win.refresh()
	return h


    def done(self,flag,ctr):
    	scr = curses.initscr()
	row,col = scr.getmaxyx()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	
	wi = curses.newwin(row,col,0,0)          #y,x
	wi.box(124,45)
	wi.refresh()
	w = curses.newwin(8,35,15,55)            #y,x
	w.keypad(1)
	w.border('|','|','-','-','+','+','+','+')
	w.bkgd(' ',curses.color_pair(3))
	w.refresh()
	if flag == 1:
		w.addstr(2,2,'!!CONGRATULATIONS!! :)')
		w.addstr(3,2,'You\'ve won the game')
		w.addstr(4,2,'Score:  ' + str(ctr*10))
		w.addstr(5,2,'Press any key to continue')
		w.refresh()
	else:
		w.addstr(2,2,'!!Sorry!! :(')
		w.addstr(3,2,'You\'ve lost the game')
		w.addstr(4,2,'Score:  ' + str(ctr))
		w.addstr(5,2,'Press Enter to continue')
		w.refresh()
	w.refresh()
	wi.refresh()
	key = w.getch()
	while key != 10:
		key = w.getch()
	
	w.clear()
	wi.bkgd(' ',curses.color_pair(1))
	wi.refresh()



    def nex(self,win,prev,d,flag,fb,fl,w):
#    	curses.initscr()
#   	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	
	for i in range(0,w):
		e = -1
		#  d = 0 verdown
		#  d = 1 hor
		#  d = 2 diag_right
		#  d = 3 verup
		#  d = 4 diag_left

		if d == 0:
			if win.inch(prev[1]+1,prev[0]+i) & 255 == 32:
				pass
			elif win.inch(prev[1]+1,prev[0]+i) & 255 == ord('C'):
				e = 1
				win.addstr(prev[1]+1,prev[0]+i,'C')	
			elif win.inch(prev[1]+1,prev[0]+i) & 255 == ord('B'):
				e = 1
				win.addstr(prev[1]+1,prev[0]+i,'B')	
			elif win.inch(prev[1]+1,prev[0]+i) & 255 == ord('='):		#            __\\\
				e = 1
				win.addstr(prev[1]+1,prev[0]+i,'=',curses.A_REVERSE)		#
			elif win.inch(prev[1]+1,prev[0]+i) & 255 == ord('#'):
				e = 1
#				win.addstr(prev[1]+1,prev[0]+i,'#')	
			else:
 				flag = 2
 				break
			if i == w-1:
			  	if e == 1:
					new = ([prev[0],prev[1]+2])			  	
				else:
					new = ([prev[0],prev[1]+1])
#				win.addstr(new[1],new[0],'|||',curses.color_pair(4))
				prev = new

		elif d == 1:
			if win.inch(prev[1],prev[0]+3) & 255 == 32:
				pass
			elif win.inch(prev[1],prev[0]+3) & 255 == ord('C'):
				e = 1
				win.addstr(prev[1],prev[0]+3,'C')	
			elif win.inch(prev[1],prev[0]+3) & 255 == ord('B'):
				e = 1
				win.addstr(prev[1],prev[0]+3,'B')	
			elif win.inch(prev[1],prev[0]+3) & 255 == ord('='):		#            __\\\
				e = 1
				win.addstr(prev[1],prev[0]+3,'=',curses.A_REVERSE)		#
			elif win.inch(prev[1],prev[0]+3) & 255 == ord('#'):
				e = 1
#				win.addstr(prev[1],prev[0]+3,'#')	
			else:
 				flag = 2
 				break
			if i == w-1:	
			  	if e == 1:
					new = ([prev[0]+4,prev[1]])			  	
				else:
					new = ([prev[0]+3,prev[1]])
	#			win.addstr(new[1],new[0],'===',curses.color_pair(4))
				prev = new

		elif d == 2:
			x = fl/fb+1
			if win.inch(prev[1]+1,prev[0]+x+i) & 255 == 32:                   #      \\\
				pass						#                   \\\
			elif win.inch(prev[1]+1,prev[0]+x+i) & 255 == ord('C'):		#              \\\
				e = 1
				win.addstr(prev[1]+1,prev[0]+x+i,'C')		#
			elif win.inch(prev[1]+1,prev[0]+x+i) & 255 == ord('B'):
				e = 1
				win.addstr(prev[1]+1,prev[0]+x+i,'B')	
			elif win.inch(prev[1]+1,prev[0]+x+i) & 255 == ord('='):		#            __\\\
				e = 1
				win.addstr(prev[1]+1,prev[0]+x+i,'=',curses.A_REVERSE)		#
			elif win.inch(prev[1]+1,prev[0]+x+i) & 255 == ord('#'):
				e = 1
#				win.addstr(prev[1]+1,prev[0]+x+i,'#')	
			else:
 				flag = 2
 				break
			if i == w-1:	
			  	if e == 1:
					new = ([prev[0]+x,prev[1]+2])			  	
				else:
					new = ([prev[0]+x,prev[1]+1])
	#			win.addstr(new[1],new[0],'###',curses.color_pair(4))
				prev = new
		elif d == 3:
			if win.inch(prev[1]-1,prev[0]+i) & 255 == 32:
				pass
			elif win.inch(prev[1]-1,prev[0]+i) & 255 == ord('C'):
				e = 1
				win.addstr(prev[1]-1,prev[0]+i,'C')	
			elif win.inch(prev[1]-1,prev[0]+i) & 255 == ord('B'):
				e = 1
				win.addstr(prev[1]-1,prev[0]+i,'B')	
			elif win.inch(prev[1]-1,prev[0]+i) & 255 == ord('='):		#            __\\\
				e = 1
				win.addstr(prev[1]-1,prev[0]+i,'=',curses.A_REVERSE)		#
			elif win.inch(prev[1]-1,prev[0]+i) & 255 == ord('#'):
				e = 1
#				win.addstr(prev[1]-1,prev[0]+i,'#')	
			else:
	 			flag = 2
	 			break
			if i == w-1:	
			  	if e == 1:
					new = ([prev[0],prev[1]-2])			  	
				else:
					new = ([prev[0],prev[1]-1])
	#			win.addstr(new[1],new[0],'\|/',curses.color_pair(4))
				prev = new
		
		elif d == 4:
			x = fl/fb+1
			if win.inch(prev[1]+1,prev[0]-x+i) & 255 == 32:                   #     ///
				pass						#            /// 
			elif win.inch(prev[1]+1,prev[0]-x+i) & 255 == ord('C'):    #      ///
				e = 1
				win.addstr(prev[1]+1,prev[0]-x+i,'C')		#
			elif win.inch(prev[1]+1,prev[0]-x+i) & 255 == ord('B'):
				e = 1
				win.addstr(prev[1]+1,prev[0]-x+i,'B')	
			elif win.inch(prev[1]+1,prev[0]-x+i) & 255 == ord('='):		#            __\\\
				e = 1
				win.addstr(prev[1]+1,prev[0]-x+i,'=',curses.A_REVERSE)		#
			elif win.inch(prev[1]+1,prev[0]-x+i) & 255 == ord('#'):
				e = 1
				win.addstr(prev[1]+1,prev[0]-x+i,'#')	
			else:
 				flag = 2
 				break
			if i == w-1:	
			  	if e == 1:
					new = ([prev[0]-x,prev[1]+2])			  	
				else:
					new = ([prev[0]-x,prev[1]+1])
#				win.addstr(new[1],new[0],'###',curses.color_pair(4))
				prev = new

	res = [flag,prev]
	return res
				 

    def lvl1(self,inv,win,fb,fl):
    	curses.initscr()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)	

	il = int(fl/3)
	ib = int(fb/3)
	i = 0
	j = 1
	for i in range(fl/4): 
		win.addch(ib,j,'=',curses.A_REVERSE)
		j = j + 1
	
	i = 0
	for i in range((2*fl)/4):
		win.addch(2*ib,j,'=',curses.A_REVERSE)
		j = j + 1

	i = 0
	j = 3*fl/4
	for i in range(fl/4):
		win.addch(ib,j,'=',curses.A_REVERSE)
		j = j + 1


	win.refresh()
	return win
	
    def lvl2(self,inv,win,fb,fl):
    	curses.initscr()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)

	il = int(fl/3)
	ib = int(fb/3)
	i = 0
	j = 1
	for i in range(fl/4): 
		win.addch(ib,j,'=',curses.color_pair(4))
		win.addch(2*ib,j,'=',curses.color_pair(4))
		j = j + 1
	
	i = 0
	j = 3*fl/4
	for i in range(fl/4):
		win.addch(ib,j,'=',curses.color_pair(4))
		win.addch(2*ib,j,'=',curses.color_pair(4))
		j = j + 1

	win.refresh()

	win.addstr(1,il,'\###/',curses.color_pair(4))
	win.addstr(2,il,'`\#/`',curses.color_pair(4))
	win.addstr(3*ib-2,2*il,'`/#\\`',curses.color_pair(4))
	win.addstr(3*ib-1,2*il,'/###\\',curses.color_pair(4))
	win.refresh()
	return win

    def lvl3(self,inv,win,fb,fl):
    	curses.initscr()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)

	il = int(fl/3)
	ib = int(fb/3)
	i = 0
	j = 1
	for i in range(fl/4): 
		win.addch(ib,j,'=',curses.A_REVERSE)
		j = j + 1
	
	i = 0
	for i in range((2*fl)/4):
		win.addch(2*ib,j,'=',curses.A_REVERSE)
		j = j + 1

	i = 0
	j = 3*fl/4
	for i in range(fl/4):
		win.addch(ib,j,'=',curses.A_REVERSE)
		j = j + 1

	win.addstr(1,1,'##\\',curses.color_pair(4))
  	win.addstr(2,1,'###\\',curses.color_pair(4))
	win.addstr(3,1,'----',curses.color_pair(4))
	win.refresh()

	win.addstr(1,fl-4,'/##',curses.color_pair(4))
	win.addstr(2,fl-5,'/###',curses.color_pair(4))
	win.addstr(3,fl-5,'----',curses.color_pair(4))
	win.addstr(fb-3,fl/2-2,'/#\\',curses.color_pair(4))
	win.addstr(fb-2,fl/2-3,'/###\\',curses.color_pair(4))
	win.refresh()
	return win



#class cgo:

 # def __init__(self):
    def go(self):
    	scr = curses.initscr()
	row,col = scr.getmaxyx()
    	curses.start_color()	
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)
#	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
#	curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
#	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_RED)
#	curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)

	win = curses.newwin(row,col,0,0)
	win.box(32,32)
	win.bkgd(curses.color_pair(1))
#	win.bkgd(curses.KEY_LEFT,curses.color_pair(1))
	win.refresh()
	win.keypad(1)
	
	win.addstr(7,20,'		          __-::.. ')
       	win.refresh()
	curses.napms(100)
	win.addstr(8,20,'		        _/ _/ _/ :. ')
       	win.refresh()
       	curses.napms(100)
	win.addstr(9,20,'		      / // // /  :. ')
       	win.refresh()
       	curses.napms(100)
	win.addstr(10,20,'		     / // // /   :: ')
       	win.refresh()
       	curses.napms(100)
	win.addstr(11,20,'          	    =========     :: ')
       	win.refresh()
       	curses.napms(100)
	win.addstr(12,20,'          	   / // // /      ***')
       	win.refresh()
       	curses.napms(100)
	win.addstr(13,20,'          	  / // // /')
       	win.refresh()
       	curses.napms(100)
	win.addstr(14,20,'         	 (_)(_)(_)')
       	win.refresh()
       	curses.napms(100)
	win.addstr(15,20,'         	  (_)(_)')
       	win.refresh()
       	curses.napms(100)
	win.addstr(16,20,'         	   (_)')
       	win.refresh()
       	curses.napms(100)
	
	win.refresh()
	curses.flash()
	curses.napms(200)
#	x = 90
#	for i in range(50):
	win.addstr(4,50,'				/[-])//  ___')
	win.addstr(5,50,'	                     __ --\ `_/~--|  / \\')
	win.addstr(6,50,'	                   /_-/~~--~~ /~~~\\_\ /\\')
	win.addstr(7,50,'	                   |  |___|===|_-- | \ \ \\')
	win.addstr(8,50,'	 _/~~~~~~~~|~~\,   ---|---\___/----|  \/\-\\')
	win.addstr(9,50,'	 ~\________|__/   / // \__ |  ||  / | |   | |')
	win.addstr(10,50,'	          ,~-|~~~~~\--, | \|--|/~|||  |   | |')
	win.addstr(11,50,'        	  [3-|____---~~ _--''==;/ _,   |   |_|')
	win.addstr(12,50,'                	      /   /\__|_/  \  \__/--/')
	win.addstr(13,50,'	                     /---/_\  -___/ |  /,--|')
	win.addstr(14,50,'	                     /  /\/~--|   | |  \///')
	win.addstr(15,50,'	                    /  / |-__ \    |/')
	win.addstr(16,50,'	                   |--/ /      |-- | \\')
	win.addstr(17,50,'	                  \^~~\/\      \   \/- ')
	win.addstr(18,50,'        	           \    |  \     |~~\~~| \\')
	win.addstr(19,50,'                	    \    \  \     \   \ \\')
	win.addstr(20,50,'                    	     \    \ |     \   \\')
	win.addstr(21,50,'       	      	     |~~|\/\|     \   \|')
	win.addstr(22,50,'                          /   |/         \_-_|')
	win.addstr(23,50,'                    	    |  /           /   //')
	win.addstr(24,50,'                    	     ~~           /  //')
	win.addstr(25,50,'                    	                 |__/')
													
	win.refresh()
	
	w = curses.newwin(4,35,30,55)
	w.border('|','|','-','-','+','+','+','+')
	w.bkgd(' ',curses.color_pair(4))
	w.refresh()
	w.addstr(1,2,'The game is about to begin..')
	w.refresh()
	curses.napms(1000)
	w.addstr(2,2,'Press "Enter" to continue')
	w.refresh()
	curses.flash()
	key = win.getch()
	t = 1
	w.timeout(100)
	while key != 10:
		w.timeout(100)
		key = win.getch()
		if t%2 == 0:
			win.addstr(12,20,'          	   / // // /    ***')
			win.refresh()
#			curses.napms(100)
		else:
			win.addstr(12,20,'          	   / // // /    ---')
			win.refresh()
#			curses.napms(100)
		t = t + 1
		key = win.getch()
	w.clear()
	win.clear()
	win.refresh()


#a = cgo()
now = play()
now.main()

