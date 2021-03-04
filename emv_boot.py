# -*- coding: utf-8 -*-

import empro.toolkit.adv as adv

def main():
	path=r"C:/Users/hr193/ads/Anatinae"
	lib=r"Anatinae_lib"
	subst=r"Anatinae_lib/tech.subst"
	substlib=r"Anatinae_lib"
	substname=r"tech"
	cell=r"main"
	view=r"layout"
	libS3D=r"simulation/Anatinae_lib/main/_3%D%Viewer/extra/0/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	adv.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, cell=cell, view=view, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary)
