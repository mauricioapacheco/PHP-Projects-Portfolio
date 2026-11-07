/*
 * FCKeditor - The text editor for internet
 * Copyright (C) 2003-2005 Frederico Caldeira Knabben
 * 
 * Licensed under the terms of the GNU Lesser General Public License:
 * 		http://www.opensource.org/licenses/lgpl-license.php
 * 
 * For further information visit:
 * 		http://www.fckeditor.net/
 * 
 * "Support Open Source software. What about a donation today?"
 * 
 * File Name: dialogue.js
 * 	Scripts for the fck_universalkey.html page.
 * 
 * File Authors:
 * 		Michel Staelens (contato@example.invalid)
 * 		Bernadette Cierzniak
 * 		Abdul-Aziz Al-Oraij (contato@example.invalid)
 * 		Frederico Caldeira Knabben (contato@example.invalid)
 */

function afficher(txt)
{
	document.getElementById( 'uni_area' ).value = txt ;
}

function rechercher()
{
	return document.getElementById( 'uni_area' ).value ;
}