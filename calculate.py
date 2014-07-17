import urllib

def url_get(urlstr):
	f = urllib.urlopen(urlstr);
	return f.read()


content = ""

item_count = 280
item_per_page = 30

page_count = int(item_count / item_per_page) + 1

game_id = 445371


for page_seq in range(page_count):
	print page_seq

	urlstr = "http://odds.500.com/fenxi1/ouzhi.php?id=" + str(game_id) + "&ctype=1&start="+str(1 + item_per_page * page_seq)+"&r=1&style=0&guojia=0&chupan=0"
	
	print urlstr
	
	content = content + url_get(urlstr)

bigest_win = 0
bigest_draw = 0
bigest_lose = 0

win_name = ""
draw_name = ""
lose_name = ""

import re
p = re.compile(r'(xls="row"[\s\S]*?)<tr class="tr\d"')
for m in p.finditer(content):
	    oneitem =  m.group(1)
	    #print oneitem
	    namepattern = re.compile(r'class="tb_plgs" title="(.*?)"')
	    match = namepattern.search(oneitem)

   	    name = ""
	    if match:
		    name = match.group(1)
	    perpattern = re.compile(r'style="cursor:pointer" >(.*?)</td>')
	    
	    seq = 0
	    for p in perpattern.finditer(oneitem):
		    seq = seq + 1
		    per = float(p.group(1))
		    if seq == 4 and per > bigest_win:
			    bigest_win = per
			    win_name = name
		    if seq == 5 and per > bigest_draw:
			    bigest_draw = per
			    draw_name = name
		    if seq == 6 and per > bigest_lose:
		 	    bigest_lose = per
			    lose_name = name

print "win\t",win_name,bigest_win
print "draw\t",draw_name,bigest_draw
print "lose\t",lose_name,bigest_lose



def get_min_pay(win, draw, lose):

	paycount = 0

	winper = 1
	drawper = 1
	loseper = 1

	def minpay(w,d,l,wp,dp,lp):
		if w * wp <= d * dp and w * wp <= l * lp:
			return w * wp
		if d * dp <= w * wp and d * dp <= l * lp:
			return d * dp
		else:
			return l * lp
		

	for i in range(100):
		for j in range(100-i):

			mincount = minpay(win, draw, lose, i ,j ,100 - i -j)
		
			if mincount > paycount:
				paycount = mincount
				winper = i
				drawper = j
				loseper = 100 - i - j

	print winper,drawper,loseper,paycount


get_min_pay(bigest_win, bigest_draw, bigest_lose)
