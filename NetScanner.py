
import scapy.all as scapy
import optparse

def get_range():
	parse_object=optparse.OptionParser()
	parse_object.add_option("-r","--range",help="google chei bruh")
	parse_object.add_option("-k","--kavali")

	return parse_object.parse_args()

(input,args)=get_range()
r=input.range
k=input.kavali

def main(r):

	arp_req_packt=scapy.ARP(pdst=r)
	brdcst_pkt=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	#scapy.ls(scapy.Ether())
	comb_pack=brdcst_pkt/arp_req_packt
	(ans_lst,uns_lst)=scapy.srp(comb_pack,timeout=1)
	ans_lst.summary()
	print("INKA KAVALAA then try -k --kavali")
	if k=='kavali':
		uns_lst.summary()

main(r)

